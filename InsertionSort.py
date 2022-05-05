import bpy
import random 
count = 50
cubes=[]
locationList=[]
scaleList=[]
i = 1
while i < count+1:
    locationList.append(i)
    scaleList.append(i)
    i += 1
random.shuffle(locationList)
random.shuffle(scaleList)
i = 0
while i < count:
    cube = bpy.ops.mesh.primitive_cube_add(location=(locationList[i], 0, 0), scale=(0.25, 0.25, 0.25))  
    i+=1
i = 0
for ob in bpy.data.objects:
    if ob.type == 'MESH':    
        ob.scale.z = scaleList[i]
        cubes.append(ob)
        i += 1
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