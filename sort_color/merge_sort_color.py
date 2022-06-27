import bpy
import random
import math 
from array import *
from math import pi
import numpy as np

############################################################
# Merge Sort Algorithm
############################################################

def merge(seed, arr, l, m, r):
    
    global Matrix
    global iframe

    n1 = m - l + 1
    n2 = r - m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
    
    while i < n1 and j < n2:
        
        mat1 = L[i].active_material.diffuse_color
        mat2 = R[j].active_material.diffuse_color
         
        #get RG values from materials
        rg1, rg2 = get_rg(mat1, mat2)
        
        if rg1 <= rg2:
            arr[k] = L[i]
         
            L[i].location.x = k * 2

            i += 1
        else:
            arr[k] = R[j]
            
            R[j].location.x = k * 2
            
            j += 1
        k += 1

        for cube in Matrix[seed]:
            cube.keyframe_insert(data_path="location", frame=iframe) 
        for cube in L:
            cube.keyframe_insert(data_path="location", frame=iframe)
        for cube in R:
            cube.keyframe_insert(data_path="location", frame=iframe)

        iframe += 1

    # Copy the remaining elements of L[], if there are any
    while i < n1:
        arr[k] = L[i]
        L[i].location.x = k * 2
        
        x=0
        for cube in Matrix[seed]:
            cube.keyframe_insert(data_path="location", frame=iframe) 
        for cube in L:
            cube.keyframe_insert(data_path="location", frame=iframe)
        for cube in R:
            cube.keyframe_insert(data_path="location", frame=iframe)
        iframe += 1
   
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there are any
    while j < n2:
        arr[k] = R[j]
        
        R[j].location.x = k * 2
        for cube in Matrix[seed]:
            cube.keyframe_insert(data_path="location", frame=iframe) 
        for cube in L:
            cube.keyframe_insert(data_path="location", frame=iframe)
        for cube in R:
            cube.keyframe_insert(data_path="location", frame=iframe)
        iframe+=1
 
        j += 1
        k += 1
        
# l is for left index and r is right index of the sub-array of arr to be sorted
def merge_sort(seed, iframe,arr, l, r):
    if l < r:
 
        # Same as (l+r)//2, but avoids overflow for large l and h
        m = l+(r-l)//2
        
        # Sort first and second halves
        merge_sort(seed, iframe,arr, l, m)
        merge_sort(seed, iframe, arr, m+1, r)
        merge(seed, arr, l, m, r)
        
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
    
    #add red values to array
    colors_r = [0 for i in range(count)]
    colors_r1 = np.linspace(0, 225, count//2)
    colors_r2 = np.linspace(230, 255, count//2)
    for i in range(count):  
        if(i < count//2):
            colors_r[i]=colors_r1[i]
        else:
            colors_r[i]=colors_r2[i-count//2]
    
    #add green values to array
    colors_g = [0 for i in range(count)]
    colors_g1 = np.linspace(0, 0, count//2)
    colors_g2 = np.linspace(20, 200, count//2)
    for i in range(count):  
        if(i < count//2):
            colors_g[i]=colors_g1[i]
        else:
            colors_g[i]=colors_g2[i-count//2]
    
    #add blue values to array
    colors_b = [0 for i in range(count)]
    colors_b1 = np.linspace(200, 20, count//2)
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
    
    #set optimal color managment setting 
    bpy.context.scene.view_settings.exposure = -3.75
    bpy.context.scene.view_settings.gamma = 0.7
    bpy.context.scene.view_settings.look = 'Medium Contrast'

    return(Matrix, count)

############################################################
# Get R and G Values from Material
############################################################

def get_rg(mat1, mat2):
    #get R value of both materials
    r1 = mat1[0]
    r2 = mat2[0]
    
    #get G value of both materials
    g1 = mat1[1]
    g2 = mat2[1]
    
    # R + G = value for comparison
    rg1 = r1 + g1
    rg2 = r2 + g2

    return rg1, rg2

############################################################
# Call Functions
############################################################

#setup_array(number of planes)
Matrix, count = setup_array(24)#only even numbers are valid

#merge_sort + visualisation
for i in range(count):
    iframe = 0
    merge_sort(i,iframe,Matrix[i],  0, count-1)