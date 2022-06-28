import bpy
import random 
from mathutils import Vector, Matrix

############################################################
# Merge Sort Algorithm
############################################################

def merge(arr, l, m, r, arrayCounter, comparisonCounter):
    
    global cubes
    global iframe

    n1 = m - l + 1
    n2 = r - m
 
    #create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
    
    #add 2 to array counter
    arrayCounter.inputs[0].default_value += 2
    arrayCounter.inputs[0].keyframe_insert(data_path='default_value', frame=iframe)
    
    #copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        
        #add 2 to array counter
        arrayCounter.inputs[0].default_value += 2
        arrayCounter.inputs[0].keyframe_insert(data_path='default_value', frame=iframe)
        L[i] = arr[l + i]

    for j in range(0, n2):
        #add 2 to array counter
        arrayCounter.inputs[0].default_value += 2
        arrayCounter.inputs[0].keyframe_insert(data_path='default_value', frame=iframe)
        R[j] = arr[m + 1 + j]

    #merge the temp arrays back into arr[l..r]
    i = 0     #initial index of first subarray
    j = 0     #initial index of second subarray
    k = l     #initial index of merged subarray
    
    while i < n1 and j < n2:
        #add 2 to array counter
        arrayCounter.inputs[0].default_value += 2
        arrayCounter.inputs[0].keyframe_insert(data_path='default_value', frame=iframe)
        
        #add 1 to comparison counter
        comparisonCounter.inputs[0].default_value += 1
        comparisonCounter.inputs[0].keyframe_insert(data_path='default_value', frame=iframe)
        if L[i].scale.z <= R[j].scale.z:
            arr[k] = L[i]
            
            L[i].location.x = k 
            
            #add 2 to array counter
            arrayCounter.inputs[0].default_value += 2
            arrayCounter.inputs[0].keyframe_insert(data_path='default_value', frame=iframe)
            
            i += 1
        else:
            arr[k] = R[j]
            
            R[j].location.x = k 
            
            #add 3 to array counter
            arrayCounter.inputs[0].default_value += 2
            arrayCounter.inputs[0].keyframe_insert(data_path='default_value', frame=iframe)
            
            j += 1
        k += 1

        for cube in cubes:
            cube.keyframe_insert(data_path="location", frame=iframe) 
        for cube in L:
            cube.keyframe_insert(data_path="location", frame=iframe)
        for cube in R:
            cube.keyframe_insert(data_path="location", frame=iframe)

        iframe += 1

    #copy the remaining elements of L[], if there are any
    while i < n1:
        arr[k] = L[i]
        
        L[i].location.x = k 
        
        #add 2 to array counter
        arrayCounter.inputs[0].default_value += 2
        arrayCounter.inputs[0].keyframe_insert(data_path='default_value', frame=iframe)
        
        x=0
        for cube in cubes:
            cube.keyframe_insert(data_path="location", frame=iframe) 
        for cube in L:
            cube.keyframe_insert(data_path="location", frame=iframe)
        for cube in R:
            cube.keyframe_insert(data_path="location", frame=iframe)
        iframe += 1
   
        i += 1
        k += 1
 
    #copy the remaining elements of R[], if there are any
    while j < n2:
        arr[k] = R[j]
        
        R[j].location.x = k 
        
        #add 2 to array counter
        arrayCounter.inputs[0].default_value += 2
        arrayCounter.inputs[0].keyframe_insert(data_path='default_value', frame=iframe)
        
        for cube in cubes:
            cube.keyframe_insert(data_path="location", frame=iframe) 
        for cube in L:
            cube.keyframe_insert(data_path="location", frame=iframe)
        for cube in R:
            cube.keyframe_insert(data_path="location", frame=iframe)
        iframe+=1
 
        j += 1
        k += 1

#l is for left index and r is right index of the sub-array of arr to be sorted    
def merge_sort(arr, l, r, arrayCounter, comparisonCounter):
    if l < r:
 
        #same as (l+r)//2, but avoids overflow for large l and h
        m = l+(r-l)//2
        
        #sort first and second halves
        merge_sort(arr, l, m, arrayCounter, comparisonCounter)
        merge_sort(arr, m+1, r, arrayCounter, comparisonCounter)
        merge(arr, l, m, r, arrayCounter, comparisonCounter)
        
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
merge_sort(cubes, 0, len(cubes)-1, arrayCounter, comparisonCounter)