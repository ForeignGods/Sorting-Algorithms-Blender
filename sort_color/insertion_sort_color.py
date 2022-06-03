import bpy
import random 
from array import *

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
            arr[j + 1].location.x = j / 2
            arr[j].location.x = (j + 1) / 2 
            
            j -= 1
            
            #get materials during loop
            mat1 = arr[j].active_material.diffuse_color
            mat2 = key_item.active_material.diffuse_color
            
            #adding keyframes to all cubes whenever one position/location is shifted
            for cube in arr:
                cube.keyframe_insert(data_path="location", frame=iframe)       
            
            #next frame
            iframe+=1  
     
        #place key_item into correct position/location
        arr[j + 1] = key_item
        arr[j + 1].location.x = i / 2
        
        #origin and target index of key_item in array
        origin = i
        target = j + 1
        
        #set location/position for key_item + add keyframes
        x = 0
        while x <= (origin-target):
            key_item.location.x = (origin - x) / 2
            key_item.keyframe_insert(data_path="location", frame= originFrame + x - 1)
            
            x += 1
        
        originFrame = iframe
        
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
    
    #fill arrays with numbers between 1 & count
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

#insertion_sort every array
for i in range(count):
    insertion_sort(Matrix[i], count)