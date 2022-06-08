from random import randint
import bpy
import random 
from mathutils import Vector, Matrix

#variables
count = 150
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

#90 degree rotation of the counter object
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

#fill arrays with numbers between 1 & count
ran = list(range(0,count))

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
for i in range(count):
    bpy.ops.mesh.primitive_cube_add(location=(ran[i], 0, 0), scale=(0.25, 0.25, 0.25))   
    
#shuffle array
random.shuffle(ran)
  
#assign random scale to all cubes and add them to array
i = 0
for ob in bpy.data.objects:
    if ob.type == 'MESH' and ob.name != "Counter":    
        origin_to_bottom(ob)
        ob.scale.z = ran[i]+1
        cubes.append(ob)
        i += 1

#sort array based on location.x        
cubes.sort(key = lambda obj: obj.location.x)

def merge(arr, l, m, r):
    
    global array
    global iframe

    
    n1 = m - l + 1
    n2 = r - m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
    
    while i < n1 and j < n2:
        if L[i].scale.z <= R[j].scale.z:
            arr[k] = L[i]
         
            L[i].location.x = k 

            i += 1
        else:
            arr[k] = R[j]
            
            R[j].location.x = k 
            
            j += 1
        k += 1

        for cube in array:
            cube.keyframe_insert(data_path="location", frame=iframe) 
        for cube in L:
            cube.keyframe_insert(data_path="location", frame=iframe)
        for cube in R:
            cube.keyframe_insert(data_path="location", frame=iframe)

        iframe += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        L[i].location.x = k 
        
        x=0
        for cube in array:
            cube.keyframe_insert(data_path="location", frame=iframe) 
        for cube in L:
            cube.keyframe_insert(data_path="location", frame=iframe)
        for cube in R:
            cube.keyframe_insert(data_path="location", frame=iframe)
        iframe += 1
   
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        
        R[j].location.x = k 
        for cube in array:
            cube.keyframe_insert(data_path="location", frame=iframe) 
        for cube in L:
            cube.keyframe_insert(data_path="location", frame=iframe)
        for cube in R:
            cube.keyframe_insert(data_path="location", frame=iframe)
        iframe+=1
 
        j += 1
        k += 1
# l is for left index and r is right index of the
# sub-array of arr to be sorted

def mergeSort(arr, l, r):
    if l < r:
 
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2
        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)

iframe = 0
array = cubes
mergeSort(cubes, 0, count-1)