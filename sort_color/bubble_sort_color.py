import bpy
import random 
from array import *

############################################################
# Bubble Sort Algorithm
############################################################
        
def bubble_sort(arr, count):
    for i in range(count):    
        
        #insert keyframe for every cube on every frame
        for cube in arr:
            cube.keyframe_insert(data_path="location", frame=i) 

        already_sorted = True
        for j in range(count - i -1):
            
            #get materials
            mat1 = arr[j].active_material.diffuse_color
            mat2 = arr[j + 1].active_material.diffuse_color
            
            #compare first colorarray values
            if mat1[0] > mat2[0]: 

                #change location & insert keyframes based on bubble sort
                arr[j].location.x = (j+1)/2
                arr[j].keyframe_insert(data_path="location", frame=i)

                arr[j+1].location.x = j/2
                arr[j+1].keyframe_insert(data_path="location", frame=i)       
                
                #rearrange arrays
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                already_sorted = False
                
        if already_sorted:
            break
        
############################################################
# Setup Random Cubes + Array to be sorted
############################################################

def setup_array(count):

    #fill arrays with numbers between 0 & count
    index = list(range(count))

    #randomize array order
    random.shuffle(index)

    #initialize 2d array
    h, w = count, count
    Matrix = [[0 for x in range(w)] for y in range(h)] 

    #delete every existing object
    for ob in bpy.data.objects:   
        bpy.data.objects.remove(ob)
        
    #delete all existing materials
    for material in bpy.data.materials:
            material.user_clear()
            bpy.data.materials.remove(material)

    #add count * count cubes
    for i in range(count):
        for j in range(count):
            bpy.ops.mesh.primitive_cube_add(location=(j/2, 0, i/2), scale=(0.25, 0.25, 0.25))  

    #assign random colors to all cubes and add them to array
    i = 0
    j = 0
    for ob in bpy.data.objects:
        if ob.type == 'MESH':      
            if i == count:
                j += 1
                random.shuffle(index)
                i = 0         
            mat = bpy.data.materials.new(name="MaterialName") #set new material to variable
            mat.diffuse_color = (index[i], 255, 255, 255)
            ob.data.materials.append(mat) #add the material to the object
            Matrix[j].append(ob)
            i += 1
        
    #remove values that are 0 (needs to be solved beforehand)
    for x in range(count):
        for i in range(count):
            Matrix[x].remove(0)

    #presort arrayorder based on location
    for i in range(count):       
        Matrix[i].sort(key = lambda obj: obj.location.x)
        
    return(Matrix, count)

############################################################
# Call Functions
############################################################

#max count = 31 (needs to be fixed)
Matrix, count = setup_array(31)

#bubble_sort every array
for i in range(count):
    bubble_sort(Matrix[i], count)