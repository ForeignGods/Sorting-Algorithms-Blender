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