import bpy
import random
import math 
from array import *
from math import pi

############################################################
# Quick Sort Algorithm
############################################################

# function to find the partition position
def partition(seed, array, low, high):
    
    global iframe
    
    # choose the rightmost element as pivot
    pivot = array[(high + low) // 2]
    
    # pointer for greater element
    i = low 
    j = high
    while True:

        mat1 = array[i].active_material.diffuse_color
        mat2 = pivot.active_material.diffuse_color
        
        while mat1[0] < mat2[0]:
            i += 1
            mat1 = array[i].active_material.diffuse_color
            mat2 = pivot.active_material.diffuse_color
        
        mat3 = array[j].active_material.diffuse_color
        mat4 = pivot.active_material.diffuse_color
        
        while mat3[0] > mat4[0]:
            j -= 1
            mat3 = array[j].active_material.diffuse_color
            mat4 = pivot.active_material.diffuse_color
        
        if i >= j:
            return j
        
        else:
            iframe += 1
            for plane in Matrix[seed]:
                plane.keyframe_insert(data_path="location", frame=iframe)
        
        array[i].location.x = j * 2
        array[j].location.x = i * 2
            
        array[i].keyframe_insert(data_path="location", frame=iframe)
        array[j].keyframe_insert(data_path="location", frame=iframe)
                
        # swapping element at i with element at j
        array[i], array[j] = array[j], array[i]

# function to perform quicksort
def quick_sort(seed, array, low, high):
    if low < high: 
        # find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pivot = partition(seed, array, low, high)

        # recursive call on the left of pivot
        quick_sort(seed, array, low, pivot)

        # recursive call on the right of pivot
        quick_sort(seed, array, pivot + 1, high)
        
        
############################################################
# Setup Random Colors + Array to be sorted
############################################################

def setup_array(count):
    
    global Matrix
    
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

Matrix, count = setup_array(30)

#quick_sort every array
for i in range(count):
    iframe= 0
    quick_sort(i, Matrix[i], 0, count - 1)
