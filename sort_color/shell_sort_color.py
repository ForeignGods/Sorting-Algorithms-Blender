import bpy
import random
import math 
from array import *
from math import pi
import numpy as np

############################################################
# Shell Sort Algorithm
############################################################

def shell_sort(arr, count):
    
    iframe = 0
    
    gap=count//2
     
    while gap>0:
        
        j=gap
        
        #check the array in from left to right
        #till the last possible index of j
        while j<count:
            
            #this will keep help in maintain gap value
            i=j-gap
            while i>=0:
                
                for cube in arr:
                    cube.keyframe_insert(data_path="location", frame= iframe)
                
                #if value on right side is already greater than left side value
                #we don't do swap else we swap
                mat1 = arr[i+gap].active_material.diffuse_color
                mat2 = arr[i].active_material.diffuse_color
                
                #get RG values from materials
                rg1, rg2 = get_rg(mat1, mat2)
                
                if rg1 > rg2:
                    break
                
                else:
                    arr[i+gap].location.x = i * 2
                    arr[i].location.x = (i + gap) * 2
                    
                    arr[i+gap].keyframe_insert(data_path="location", frame= iframe)
                    arr[i].keyframe_insert(data_path="location", frame= iframe)
                    iframe += 1
                    
                    arr[i+gap],arr[i] = arr[i],arr[i+gap]
                    
                i=i-gap 
                            
            j+=1
        gap=gap//2

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

Matrix, count = setup_array(24)#only even numbers are valid

#shell_sort every array
for i in range(count):
    shell_sort(Matrix[i], count)