import bpy
import random
import math 
from array import *
from math import pi

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
        
        arr[i].location.x = min_idx * 2
        arr[min_idx].location.x = i * 2
        
        iframe +=1
        arr[i].keyframe_insert(data_path="location", frame= iframe)
        arr[min_idx].keyframe_insert(data_path="location", frame= iframe)
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

############################################################
# Setup Random Colors + Array to be sorted
############################################################

def setup_array(count):

    #fill array with numbers between 0 & count - 1
    index = list(range(count))

    #initialize 2d array
    Matrix = [[0 for x in range(count)] for y in range(count)] 
    
    #initialize object and material array
    planes = [0 for i in range(count*count)]
    materials = [0 for i in range(count)]
    
    #delete every existing object
    for ob in bpy.data.objects:   
        bpy.data.objects.remove(ob)
        
    #delete all existing materials
    for material in bpy.data.materials:
            bpy.data.materials.remove(material, do_unlink=True)
        
    for i in range(count):
        for j in range(count):
            bpy.ops.mesh.primitive_plane_add(location=(j*2, 0, i*2), rotation=(pi / 2, 0, 0), scale=(0.1, 0.1, 0.1)) 
    
    i=0
    for ob in bpy.data.objects:
           planes[i]= ob
           i+=1
    
    #sorts list of all objects based primary on their location.z and secondary on their location.x
    planes.sort(key = lambda obj: obj.location.z + obj.location.x/(count*count))
    
    for i in range(count):
            material = bpy.data.materials.new(name="")
            material.diffuse_color = (index[i]/3, 255, 255, 255)
            materials[i] = material  
                      
    for i in range(count):
        random.shuffle(materials)
        for j in range(count):
                planes[j+i*count].data.materials.append(materials[j]) #add the material to the object
                Matrix[i][j] = planes[j+i*count]
     
    return(Matrix, count)

############################################################
# Call Functions
############################################################

Matrix, count = setup_array(31)

#selection_sort every array
for i in range(count):
    selection_sort(Matrix[i], count)