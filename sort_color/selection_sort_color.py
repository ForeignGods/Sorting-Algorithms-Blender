import bpy
import random 
from array import *

############################################################
# Selection Sort Algorithm
############################################################

def selection_sort(arr, count):
    
    #start at frame 0
    iframe = 0
    for i in range(0, count): 
        min_idx = i  
        
        for cube in arr:
            cube.keyframe_insert(data_path="location", frame= iframe)
        
        for j in range(i , count):
            
            #get materials for color comparison
            mat1 = arr[min_idx].active_material.diffuse_color
            mat2 = arr[j].active_material.diffuse_color
            
            if mat1[0] > mat2[0]:   
                min_idx = j
        
        arr[i].location.x = min_idx / 2
        arr[min_idx].location.x = i / 2
        
        iframe +=1
        arr[i].keyframe_insert(data_path="location", frame= iframe)
        arr[min_idx].keyframe_insert(data_path="location", frame= iframe)
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

############################################################
# Setup Random Cubes + Array to be sorted
############################################################

def setup_array(count):
    
    #delete all materials
    for material in bpy.data.materials:
        material.user_clear()
        bpy.data.materials.remove(material)
    
    #delete every existing object
    for ob in bpy.data.objects:   
        bpy.data.objects.remove(ob)
    
    #fill arrays with numbers between 0 & count-1
    index = list(range(count))

    #randomize array order
    random.shuffle(index)
    
    #initialize 2d array
    Matrix = [[0 for x in range(count)] for y in range(count)] 
    
    #add count * count cubes
    for i in range(count):
        for j in range(count):
            bpy.ops.mesh.primitive_cube_add(location=(j/2, 0, i/2), scale=(0.25, 0.25, 0.25))  

    #assign random scale to all cubes and add them to array
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

    return (Matrix, count)

############################################################
# Call Functions
############################################################

#max count = 31 (needs to be fixed)
Matrix, count = setup_array(31)

#selection_sort every array
for i in range(count):
    selection_sort(Matrix[i], count)