import bpy
import random
import math 
from array import *
from math import pi

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
                arr[j].location.x = (j+1)*2
                arr[j].keyframe_insert(data_path="location", frame=i+1)

                arr[j+1].location.x = j*2
                arr[j+1].keyframe_insert(data_path="location", frame=i+1)       
                
                #rearrange arrays
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                already_sorted = False
                
        if already_sorted:
            break
        
############################################################
# Setup Random Cubes + Array to be sorted
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
    
    #sorts list of all objects based primary on their location.x and secondary on their location.z
    planes.sort(key = lambda obj: obj.location.z + obj.location.x/(count*count))
    
    for i in range(count):
            material = bpy.data.materials.new(name="")
            material.diffuse_color = (index[i], 255, 255, 255)
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

Matrix, count = setup_array(50)

for i in range(count):
    bubble_sort(Matrix[i], count)