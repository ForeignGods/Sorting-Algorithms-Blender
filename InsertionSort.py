import bpy
from random import randint
count = 50
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
for i in range(1, n):
    key_item = cubes[i]
    key_item.location.x = i
    j = i - 1
    while j >= 0 and cubes[j].scale.z > key_item.scale.z:
        cubes[j + 1] = cubes[j]
        cubes[j + 1].location.x = j 
        cubes[j].location.x = j + 1  
        j -= 1
    cubes[j + 1] = key_item
    cubes[j + 1].location.x = i
    key_item.location.x = j + 1