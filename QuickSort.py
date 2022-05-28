from random import randint

import bpy
import random 
from mathutils import Vector, Matrix

#variables
count = 50 
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
ran = list(range(1,count+1))

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
        ob.scale.z = ran[i]
        cubes.append(ob)
        i += 1

#sort array based on location.x        
cubes.sort(key = lambda obj: obj.location.x)

# Quick sort in Python
# function to find the partition position
def partition(array, low, high):

    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j].scale.z <= pivot.scale.z:
        # if element smaller than pivot is found
        # swap it with the greater element pointed by i
            i = i + 1
            array[i].location.x = j
            array[j].location.x = i
            
            # swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

        
    # swap the pivot element with the greater element specified by i
    array[i + 1].location.x = high
    array[high].location.x = i + 1
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # return the position from where partition is done
    return i + 1

# function to perform quicksort
def quickSort(array, low, high):
    if low < high:

        # find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # recursive call on the left of pivot
        quickSort(array, low, pi - 1)

        # recursive call on the right of pivot
        quickSort(array, pi + 1, high)


