import bpy
import random
import math 
from array import *
from math import pi
import numpy as np

############################################################
# Insertion Sort Algorithm
############################################################

def insertion_sort(arr, count):
    
    #start at frame 0
    iframe=0
    originFrame = 0 

    for i in range(count):
        
        #defines key_item that is compared until correct location
        key_item = arr[i]
        key_item.location.x = i / 2
        
        j = i - 1
        
        #get materials before loop
        mat1 = arr[j].active_material.diffuse_color
        mat2 = key_item.active_material.diffuse_color
        
        #get R value of both materials
        r1 = mat1[0]
        r2 = mat2[0]
        
        #get G value of both materials
        g1 = mat1[1]
        g2 = mat2[1]
     
        # R + G = value for comparison
        rg1 = r1 + g1
        rg2 = r2 + g2
        
        while j >= 0 and rg1 > rg2:

            #sets position of item in array
            arr[j + 1] = arr[j]
            
            #sets location
            arr[j + 1].location.x = j * 2
            arr[j].location.x = (j + 1) * 2 
            
            j -= 1
            
            #get materials during loop
            mat1 = arr[j].active_material.diffuse_color
            mat2 = key_item.active_material.diffuse_color
            
            #get R value of both materials
            r1 = mat1[0]
            r2 = mat2[0]
            
            #get G value of both materials
            g1 = mat1[1]
            g2 = mat2[1]
         
            # R + G = value for comparison
            rg1 = r1 + g1
            rg2 = r2 + g2
            
            #adding keyframes to all planes whenever one position/location is shifted
            for plane in arr:
                plane.keyframe_insert(data_path="location", frame=iframe)       
            
            #next frame
            iframe+=1  
     
        #place key_item into correct position/location
        arr[j + 1] = key_item
        arr[j + 1].location.x = i * 2
        
        #origin and target index of key_item in array
        origin = i
        target = j + 1
        
        #set location/position for key_item + add keyframes
        x = 0
        while x <= (origin-target):
            key_item.location.x = (origin - x) * 2
            key_item.keyframe_insert(data_path="location", frame= originFrame + x - 1)
            
            x += 1
        
        originFrame = iframe
        
############################################################
# Setup Random Cubes + Array to be sorted
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
    colors_g2 = np.linspace(0, 200, count//2)
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

Matrix, count = setup_array(30)#only even numbers are valid

#insertion_sort every array
for i in range(count):
    insertion_sort(Matrix[i], count)