import bpy
import random
import math 
from array import *
from math import pi

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
        
        while j >= 0 and mat1[0] > mat2[0]:

            #sets position of item in array
            arr[j + 1] = arr[j]
            
            #sets location
            arr[j + 1].location.x = j * 2
            arr[j].location.x = (j + 1) * 2 
            
            j -= 1
            
            #get materials during loop
            mat1 = arr[j].active_material.diffuse_color
            mat2 = key_item.active_material.diffuse_color
            
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

#insertion_sort every array
for i in range(count):
    insertion_sort(Matrix[i], count)