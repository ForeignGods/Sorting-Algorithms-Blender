import bpy
import random 
from mathutils import Vector, Matrix
#variables
count = 50 
cubes=[]
locations=[]
scales=[]
#delete every existing node_group 
for grp in bpy.data.node_groups:
    bpy.data.node_groups.remove(grp)
#add counter object 
bpy.ops.mesh.primitive_cube_add(location = (-2.5, 0, -3.375))
bpy.context.active_object.name = 'Counter'
#add geometry node modifier
bpy.ops.object.modifier_add(type='NODES')
#get, rename and clear node_group
node_grp = bpy.data.node_groups[-1] 
node_grp.name = "Counter" 
node_grp.nodes.clear()
#add nodes
stringToCurves = node_grp.nodes.new("GeometryNodeStringToCurves")
fillCurve = node_grp.nodes.new("GeometryNodeFillCurve")
transform = node_grp.nodes.new("GeometryNodeTransform")
joinStrings = node_grp.nodes.new("GeometryNodeStringJoin")
comparisonString = node_grp.nodes.new("FunctionNodeInputString")
counter1String = node_grp.nodes.new("FunctionNodeValueToString")
arrayString = node_grp.nodes.new("FunctionNodeInputString")
counter2String = node_grp.nodes.new("FunctionNodeValueToString")
groupOutput = node_grp.nodes.new('NodeGroupOutput')
#set default values of some nodes
transform.inputs[2].default_value[0] = 1.5708
comparisonString.string = "Comparisons:"
arrayString.string = "Array Accesses:"
stringToCurves.inputs[1].default_value = 2
joinStrings.inputs[0].default_value = " "
#connect nodes to eachother
node_grp.links.new(fillCurve.outputs[0], groupOutput.inputs[0])
node_grp.links.new(transform.outputs[0], fillCurve.inputs[0])
node_grp.links.new(stringToCurves.outputs[0], transform.inputs[0])
node_grp.links.new(joinStrings.outputs[0], stringToCurves.inputs[0])
node_grp.links.new(counter1String.outputs[0], joinStrings.inputs[1])
node_grp.links.new(comparisonString.outputs[0], joinStrings.inputs[1])
node_grp.links.new(counter2String.outputs[0], joinStrings.inputs[1])
node_grp.links.new(arrayString.outputs[0], joinStrings.inputs[1])
#fill arrays with numbers between 1 & count
i = 1
while i < count+1:
    locations.append(i)
    scales.append(i)
    i += 1
#randomize array order
random.shuffle(locations)
random.shuffle(scales)
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
i = 0
while i < count:
    cube = bpy.ops.mesh.primitive_cube_add(location=(locations[i], 0, 0), scale=(0.25, 0.25, 0.25))     
    i+=1
#assign random scale to all cubes and add them to array
i = 0
for ob in bpy.data.objects:
    if ob.type == 'MESH' and ob.name != "Counter":    
        origin_to_bottom(ob)
        ob.scale.z = scales[i]
        cubes.append(ob)
        i += 1
#insert keyframes on starting location for all cubes 
i=0
while i < count:
    cubes[i].keyframe_insert(data_path="location", frame=0)
    i += 1
#bubble sort
n = len(cubes)
for i in range(n):    
    #insert keyframe for every cube on every frame
    for cube in cubes:
        cube.keyframe_insert(data_path="location", frame=i) 
    already_sorted = True
    for j in range(n - i - 1):
        if cubes[j].scale.z > cubes[j + 1].scale.z: 
            #add 1 to comparison counter
            counter1String.inputs[0].default_value += 1
            counter1String.inputs[0].keyframe_insert(data_path='default_value', frame=i)
            #add 6 to array counter
            counter2String.inputs[0].default_value += 6
            counter2String.inputs[0].keyframe_insert(data_path='default_value', frame=i)
            #change location & insert keyframes based on bubble sort
            cubes[j].location.x = j
            cubes[j].keyframe_insert(data_path="location", frame=i)
            cubes[j+1].location.x = j-1
            cubes[j+1].keyframe_insert(data_path="location", frame=i)          
            #rearrange arrays
            cubes[j], cubes[j + 1] = cubes[j + 1], cubes[j]
            already_sorted = False
    if already_sorted:
        break