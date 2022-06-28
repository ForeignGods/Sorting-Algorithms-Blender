import bpy
import random 
from mathutils import Vector, Matrix

############################################################
# Heap Sort Algorithm
############################################################

def heapify(arr, n, i):
    
    global iframe
    
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
    
    #add 2 to arrayCounter
    arrayCounter.inputs[0].default_value += 2
    arrayCounter.inputs[0].keyframe_insert(data_path='default_value', frame=iframe)
    #add 1 to comparisonCounter
    comparisonCounter.inputs[0].default_value += 2
    comparisonCounter.inputs[0].keyframe_insert(data_path='default_value', frame=iframe)
    # See if left child of root exists and is greater than root
    if l < n and arr[largest].scale.z - 1 < arr[l].scale.z - 1:
        largest = l
    
    #add 2 to arrayCounter
    arrayCounter.inputs[0].default_value += 2
    arrayCounter.inputs[0].keyframe_insert(data_path='default_value', frame=iframe)
    #add 1 to comparisonCounter
    comparisonCounter.inputs[0].default_value += 2
    comparisonCounter.inputs[0].keyframe_insert(data_path='default_value', frame=iframe)
    # See if right child of root exists and is greater than root
    if r < n and arr[largest].scale.z - 1 < arr[r].scale.z - 1:
        largest = r
    
    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] #swap
        
        a = arr[i].location.x
        b = arr[largest].location.x
        
        arr[i].location.x = b
        arr[largest].location.x = a
    
        #add 4 to arrayCounter
        arrayCounter.inputs[0].default_value += 4
        arrayCounter.inputs[0].keyframe_insert(data_path='default_value', frame=iframe)
        
        for cube in cubes:
            cube.keyframe_insert(data_path="location", frame=iframe) 
        iframe += 1
        
        # Heapify the root.
        heapify(arr, n, largest)
  
# The main function to sort an array of given size
def heap_sort(arr):
   
    global iframe
    
    n = len(arr)
    
    # Build a maxheap.
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
  
    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] #swap
        
        a = arr[i].location.x
        b = arr[0].location.x
        
        arr[i].location.x = b
        arr[0].location.x = a
        
        #add 4 to arrayCounter
        arrayCounter.inputs[0].default_value += 4
        arrayCounter.inputs[0].keyframe_insert(data_path='default_value', frame=iframe)
        
        for cube in cubes:
            cube.keyframe_insert(data_path="location", frame=iframe) 
        iframe += 1
        
        heapify(arr, i, 0)

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
    
    print(len(cubes))

    return (cubes, arrayCounter, comparisonCounter)

############################################################
# Call Functions
############################################################

cubes, arrayCounter, comparisonCounter = setup_array(50)

iframe = 1
heap_sort(cubes)