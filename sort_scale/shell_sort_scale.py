import bpy
import random 
from mathutils import Vector, Matrix

############################################################
# Shell Sort Algorithm
############################################################

def shellSort(arr, n, arrayCounter, comparisonCounter):
    
    global iframe
    
    gap=n//2
     
    while gap>0:
        
        j=gap
        
        # Check the array in from left to right
        # Till the last possible index of j
        while j<n:
            
            i=j-gap # This will keep help in maintain gap value
            while i>=0:
                
                for cube in arr:
                    cube.keyframe_insert(data_path="location", frame= iframe)
                
                #add 1 to comparison counter
                comparisonCounter.inputs[0].default_value += 1
                comparisonCounter.inputs[0].keyframe_insert(data_path='default_value', frame=iframe)
            
                #add 2 to array counter
                arrayCounter.inputs[0].default_value += 2
                arrayCounter.inputs[0].keyframe_insert(data_path='default_value', frame=iframe)
                
                # If value on right side is already greater than left side value
                # We don't do swap else we swap
                if arr[i+gap].scale.z > arr[i].scale.z:
 
                    break
                else:
                    arr[i+gap].location.x = i
                    arr[i].location.x = i + gap
                    
                    arr[i+gap].keyframe_insert(data_path="location", frame= iframe)
                    arr[i].keyframe_insert(data_path="location", frame= iframe)
                    iframe += 1
                    
                    arr[i+gap],arr[i] = arr[i],arr[i+gap]
                    
                    #add 4 to array counter
                    arrayCounter.inputs[0].default_value += 4
                    arrayCounter.inputs[0].keyframe_insert(data_path='default_value', frame=iframe)
 
                i=i-gap # To check left side also
                            # If the element present is greater than current element
            j+=1
        gap=gap//2

############################################################
# Setup Random Cubes + Array to be sorted
############################################################

def setup_array(count):

    #initialize array
    cubes=[]

    #delete every existing node_group 
    for grp in bpy.data.node_groups:
        bpy.data.node_groups.remove(grp)

    #delete every existing object
    for ob in bpy.data.objects:   
        bpy.data.objects.remove(ob)
        
    #add counter object, set position of counter object below other cube
    bpy.ops.mesh.primitive_cube_add(location = (-2.5, 0, -3.375)) 
    bpy.context.active_object.name = 'Counter'

    #add geometry node modifier
    bpy.ops.object.modifier_add(type='NODES')

    #get and clear node_group
    node_grp = bpy.data.node_groups[-1] 
    node_grp.nodes.clear()

    #add nodes
    stringToCurves = node_grp.nodes.new("GeometryNodeStringToCurves")
    fillCurve = node_grp.nodes.new("GeometryNodeFillCurve")
    transform = node_grp.nodes.new("GeometryNodeTransform")
    joinStrings = node_grp.nodes.new("GeometryNodeStringJoin")
    comparisonString = node_grp.nodes.new("FunctionNodeInputString")
    comparisonCounter = node_grp.nodes.new("FunctionNodeValueToString")
    arrayString = node_grp.nodes.new("FunctionNodeInputString")
    arrayCounter = node_grp.nodes.new("FunctionNodeValueToString")
    groupOutput = node_grp.nodes.new('NodeGroupOutput')

    #90 degree rotation of the transform node of counter object
    transform.inputs[2].default_value[0] = 1.5708 

    #set default values of some nodes
    comparisonString.string = "Comparisons:"
    arrayString.string = "Array Accesses:"
    stringToCurves.inputs[1].default_value = 2
    joinStrings.inputs[0].default_value = " "

    #connect nodes to eachother
    node_grp.links.new(fillCurve.outputs[0], groupOutput.inputs[0])
    node_grp.links.new(transform.outputs[0], fillCurve.inputs[0])
    node_grp.links.new(stringToCurves.outputs[0], transform.inputs[0])
    node_grp.links.new(joinStrings.outputs[0], stringToCurves.inputs[0])
    node_grp.links.new(comparisonCounter.outputs[0], joinStrings.inputs[1])
    node_grp.links.new(comparisonString.outputs[0], joinStrings.inputs[1])
    node_grp.links.new(arrayCounter.outputs[0], joinStrings.inputs[1])
    node_grp.links.new(arrayString.outputs[0], joinStrings.inputs[1])

    #add keyframe on frame 0 for comparison and array counter
    comparisonCounter.inputs[0].keyframe_insert(data_path='default_value', frame=0)
    arrayCounter.inputs[0].keyframe_insert(data_path='default_value', frame=0)

    #fill arrays with numbers between 1 & count
    ran = list(range(0,count-1))

    #randomize array order
    random.shuffle(ran)

    #sets origin of cube to bottom of mesh
    def origin_to_bottom(ob, matrix=Matrix()):
        me = ob.data
        mw = ob.matrix_world
        local_verts = [matrix @ Vector(v[:]) for v in ob.bound_box]
        o = sum(local_verts, Vector()) / 8
        o.z = min(v.z for v in local_verts)
        o = matrix.inverted() @ o
        me.transform(Matrix.Translation(-o))
        mw.translation = mw @ o
        
    #create cubes with random location
    for i in range(count-1):
        bpy.ops.mesh.primitive_cube_add(location=(ran[i], 0, 0), scale=(0.25, 0.25, 0.25))   
        
    #shuffle array
    random.shuffle(ran)
      
    #assign random scale to all cubes and add them to array
    s = 0
    for ob in bpy.data.objects:
        if ob.type == 'MESH' and ob.name != "Counter":    
            origin_to_bottom(ob)
            ob.scale.z = ran[s]+1
            cubes.append(ob)
            s += 1

    #sort array based on location.x        
    cubes.sort(key = lambda obj: obj.location.x)

    return (cubes, arrayCounter, comparisonCounter)

############################################################
# Call Functions
############################################################

cubes, arrayCounter, comparisonCounter = setup_array(50)

iframe = 1
shellSort(cubes, len(cubes), arrayCounter, comparisonCounter)