import bpy
from random import randint
count = 100
cubes=[]
i = 0
while i < count:
    x = randint(1,10) 
    cube = bpy.ops.mesh.primitive_cube_add(location=(x, 0, 0), scale=(0.25, 0.25, 0.25))  
    i += 1
for ob in bpy.data.objects:
    z = randint(1,10)
    if ob.type == 'MESH':
        ob.scale.z = z
        cubes.append(ob)
n = len(cubes)
for i in range(n):
    already_sorted = True
    for j in range(n - i - 1):
        if cubes[j].scale.z > cubes[j + 1].scale.z:
            cubes[j].location = (j, 0.0, 0.0)
            cubes[j].keyframe_insert(data_path="location", frame=i)
            cubes[j+1].location = (j-1, 0.0, 0.0)
            cubes[j+1].keyframe_insert(data_path="location", frame=i)
            cubes[j], cubes[j + 1] = cubes[j + 1], cubes[j]
            already_sorted = False
    if already_sorted:
        break