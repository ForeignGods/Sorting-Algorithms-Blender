import bpy
import random
import math 
from array import *
from math import pi
import numpy as np

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
        
        #get R value of both materials
        r1 = mat1[0]
        r2 = mat2[0]
        
        #get G value of both materials
        g1 = mat1[1]
        g2 = mat2[1]
     
        # R + G = value for comparison
        rg1 = r1 + g1
        rg2 = r2 + g2
        
        while rg1 < rg2:
            i += 1
            mat1 = array[i].active_material.diffuse_color
            mat2 = pivot.active_material.diffuse_color
            
            #get R value of both materials
            r1 = mat1[0]
            r2 = mat2[0]
            
            #get G value of both materials
            g1 = mat1[1]
            g2 = mat2[1]
         
            # R + G = value for comparison
            rg1 = r1 + g1
            rg2 = r2 + g2
        
        mat3 = array[j].active_material.diffuse_color
        mat4 = pivot.active_material.diffuse_color
        
        #get R value of both materials
        r3 = mat3[0]
        r4 = mat4[0]
        
        #get G value of both materials
        g3 = mat3[1]
        g4 = mat4[1]
     
        # R + G = value for comparison
        rg3 = r3 + g3
        rg4 = r4 + g4
        
        while rg3 > rg4:
            j -= 1
            mat3 = array[j].active_material.diffuse_color
            mat4 = pivot.active_material.diffuse_color
            
            #get R value of both materials
            r3 = mat3[0]
            r4 = mat4[0]
            
            #get G value of both materials
            g3 = mat3[1]
            g4 = mat4[1]
         
            # R + G = value for comparison
            rg3 = r3 + g3
            rg4 = r4 + g4
        
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

    #fill array with numbers between 0 & count - 1
    index = list(range(count))

    #initialize 2d array
    Matrix = [[0 for x in range(count)] for y in range(count)] 
    
    #initialize plane array
    planes = [0 for i in range(count*count)]
    
    #initialize material array
    materials = [0 for i in range(count)]
    
    #create arrays for each color value (RGB) to generate the sunset gradient
    
    #first half 0 --> 255, second half 255 --> 255
    colors_r = [0 for i in range(count)]
    colors_r1 = np.linspace(0, 255, count//2)
    colors_r2 = np.linspace(255, 255, count//2)
    for i in range(count):  
        if(i < count//2):
            colors_r[i]=colors_r1[i]
        else:
            colors_r[i]=colors_r2[i-count//2]
    
    #first half 0 --> 0, second half 0 --> 200
    colors_g = [0 for i in range(count)]
    colors_g1 = np.linspace(0, 0, count//2)
    colors_g2 = np.linspace(1, 200, count//2)
    for i in range(count):  
        if(i < count//2):
            colors_g[i]=colors_g1[i]
        else:
            colors_g[i]=colors_g2[i-count//2]
    
    #first half 200 --> 0, secondhalf 0 --> 100
    colors_b = [0 for i in range(count)]
    colors_b1 = np.linspace(200, 0, count//2)
    colors_b2 = np.linspace(0, 100, count//2)
    for i in range(count):  
        if(i < count//2):
            colors_b[i]=colors_b1[i]
        else:
            colors_b[i]=colors_b2[i-count//2]
        
    #delete every existing object
    for ob in bpy.data.objects:   
        bpy.data.objects.remove(ob)
        
    #delete all existing materials
    for material in bpy.data.materials:
            bpy.data.materials.remove(material, do_unlink=True)
    
    #creating count * count planes with location.x = j * 2 and location.z = i * 2
    for i in range(count):
        for j in range(count):
            bpy.ops.mesh.primitive_plane_add(location=(j*2, 0, i*2), rotation=(pi / 2, 0, 0), scale=(0.1, 0.1, 0.1)) 
    
    #adding all planes to an array
    i=0
    for ob in bpy.data.objects:
           planes[i]= ob
           i+=1
    
    #sorts list of all objects based primary on their location.x and secondary on their location.z
    planes.sort(key = lambda obj: obj.location.z + obj.location.x/(count*count))
    
    #adding materials to array and set colorgradient 
    for i in range(count):
        for j in range(count):
                material = bpy.data.materials.new(name="")
                material.diffuse_color = (colors_r[i], colors_g[i], colors_b[i], 255)
                materials[i] = material  
    
    #add materials to planes and planes to 2d array              
    for i in range(count):
        #randomize distribution of colors for every row
        random.shuffle(materials)
        for j in range(count):
                planes[j+i*count].data.materials.append(materials[j]) #add the material to the object
                Matrix[i][j] = planes[j+i*count]
     
    return(Matrix, count)


############################################################
# Call Functions
############################################################

Matrix, count = setup_array(12)

#quick_sort every array
for i in range(count):
    iframe= 0
    quick_sort(i, Matrix[i], 0, count - 1)