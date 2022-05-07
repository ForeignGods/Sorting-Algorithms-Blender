import bpy
import random 
#variables
count = 50
cubes=[]
locations=[]
scales=[]
#fill arrays with numbers between 1 & count
i = 1
while i < count+1:
    locations.append(i)
    scales.append(i)
    i += 1 
#randomize array order
random.shuffle(locations)
random.shuffle(scales)
#create cubes with random location
i = 0
while i < count:
    cube = bpy.ops.mesh.primitive_cube_add(location=(locations[i], 0, 0), scale=(0.25, 0.25, 0.25))  
    i+=1
#assign random scale to all cubes and add them to array
i = 0
for ob in bpy.data.objects:
    if ob.type == 'MESH':    
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
            #insert keyframes based on bubble sort
            cubes[j].location = (j, 0.0, 0.0)
            cubes[j].keyframe_insert(data_path="location", frame=i)
            cubes[j+1].location = (j-1, 0.0, 0.0)
            cubes[j+1].keyframe_insert(data_path="location", frame=i)
            #rearrange arrays
            cubes[j], cubes[j + 1] = cubes[j + 1], cubes[j]
            already_sorted = False
    if already_sorted:
        break