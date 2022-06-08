import bpy
import random
import math 
from array import *
from math import pi

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
                
                if mat1[0] > mat2[0]:
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

Matrix, count = setup_array(32)

#shell_sort every array
for i in range(count):
    shell_sort(Matrix[i], count)