import bpy
import random
import math 
from array import *
from math import pi
import numpy as np

############################################################
# Selection Sort Algorithm
############################################################

def selection_sort(arr, count, iframe):
    
    for i in range(0, count): 
        min_idx = i  
        
        for cube in arr:
            cube.keyframe_insert(data_path="location", frame= iframe)
        
        for j in range(i , count):
            
            #get materials for color comparison
            mat1 = arr[min_idx].active_material.diffuse_color
            mat2 = arr[j].active_material.diffuse_color
            
            #get RG values from materials
            rg1, rg2 = get_rg(mat1, mat2)
            
            if rg1 > rg2:   
                min_idx = j
        
        arr[i].location.x = min_idx * 2
        arr[min_idx].location.x = i * 2
        
        iframe +=1
        arr[i].keyframe_insert(data_path="location", frame= iframe)
        arr[min_idx].keyframe_insert(data_path="location", frame= iframe)
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
    return iframe

############################################################
# Quick Sort Algorithm
############################################################

# function to find the partition position
def partition(seed, array, low, high):
    
    global iframe
    
    #choose the rightmost element as pivot
    pivot = array[(high + low) // 2]
    
    #pointer for greater element
    i = low 
    j = high
    while True:

        mat1 = array[i].active_material.diffuse_color
        mat2 = pivot.active_material.diffuse_color
        
        #get RG values from materials
        rg1, rg2 = get_rg(mat1, mat2)
        
        while rg1 < rg2:
            i += 1
            mat1 = array[i].active_material.diffuse_color
            mat2 = pivot.active_material.diffuse_color
            
            #get RG values from materials
            rg1, rg2 = get_rg(mat1, mat2)
        
        mat1 = array[j].active_material.diffuse_color
        mat2 = pivot.active_material.diffuse_color
        
        #get RG values from materials
        rg1, rg2 = get_rg(mat1, mat2)
        
        while rg1 > rg2:
            j -= 1
            mat1 = array[j].active_material.diffuse_color
            mat2 = pivot.active_material.diffuse_color
            
            #get RG values from materials
            rg1, rg2 = get_rg(mat1, mat2)
        
        if i >= j:
            return j
        
        else:
            iframe += 1
            for plane in Matrix4[seed]:
                plane.keyframe_insert(data_path="location", frame=iframe)
        
        array[i].location.x = j * 2
        array[j].location.x = i * 2
            
        array[i].keyframe_insert(data_path="location", frame=iframe)
        array[j].keyframe_insert(data_path="location", frame=iframe)
                
        #swapping element at i with element at j
        array[i], array[j] = array[j], array[i]

#function to perform quicksort
def quick_sort(seed, array, low, high):
    if low < high: 
        #find pivot element such that
        #element smaller than pivot are on the left
        #element greater than pivot are on the right
        pivot = partition(seed, array, low, high)

        #recursive call on the left of pivot
        quick_sort(seed, array, low, pivot)

        #recursive call on the right of pivot
        quick_sort(seed, array, pivot + 1, high)
    
############################################################
# Merge Sort Algorithm
############################################################

def merge(seed, arr, l, m, r):
    
    global Matrix6
    global iframe

    
    n1 = m - l + 1
    n2 = r - m
 
    #create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    #copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    #merge the temp arrays back into arr[l..r]
    i = 0     #initial index of first subarray
    j = 0     #initial index of second subarray
    k = l     #initial index of merged subarray
    
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

        for cube in Matrix6[seed]:
            cube.keyframe_insert(data_path="location", frame=iframe) 
        for cube in L:
            cube.keyframe_insert(data_path="location", frame=iframe)
        for cube in R:
            cube.keyframe_insert(data_path="location", frame=iframe)

        iframe += 1

    #copy the remaining elements of L[], if there are any
    while i < n1:
        arr[k] = L[i]
        L[i].location.x = k * 2
        
        x=0
        for cube in Matrix6[seed]:
            cube.keyframe_insert(data_path="location", frame=iframe) 
        for cube in L:
            cube.keyframe_insert(data_path="location", frame=iframe)
        for cube in R:
            cube.keyframe_insert(data_path="location", frame=iframe)
        iframe += 1
   
        i += 1
        k += 1
 
    #copy the remaining elements of R[], if there are any
    while j < n2:
        arr[k] = R[j]
        
        R[j].location.x = k * 2
        for cube in Matrix6[seed]:
            cube.keyframe_insert(data_path="location", frame=iframe) 
        for cube in L:
            cube.keyframe_insert(data_path="location", frame=iframe)
        for cube in R:
            cube.keyframe_insert(data_path="location", frame=iframe)
        iframe+=1
 
        j += 1
        k += 1

#l is for left index and r is right index of the sub-array of arr to be sorted
def merge_sort(seed,arr, l, r):
    if l < r:
 
        #same as (l+r)//2, but avoids overflow for large l and h
        m = l+(r-l)//2
        #sort first and second halves
        merge_sort(seed, arr, l, m)
        merge_sort(seed, arr, m+1, r)
        merge(seed, arr, l, m, r)

############################################################
# Insertion Sort Algorithm
############################################################
        
def insertion_sort(arr, count, iframe):
    
    #start at frame 0
    originFrame = iframe

    for i in range(count):
        
        #defines key_item that is compared until correct location
        key_item = arr[i]
        key_item.location.x = i / 2
        
        j = i - 1
        
        #get materials before loop
        mat1 = arr[j].active_material.diffuse_color
        mat2 = key_item.active_material.diffuse_color
        
        #get RG values from materials
        rg1, rg2 = get_rg(mat1, mat2)
        
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
            
            #get RG values from materials
            rg1, rg2 = get_rg(mat1, mat2)
            
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
        
    return iframe

############################################################
# Bubble Sort Algorithm
############################################################
        
def bubble_sort(arr, count, iframe):
    for i in range(count):    
        
        #insert keyframe for every cube on every frame
        for cube in arr:
            cube.keyframe_insert(data_path="location", frame=iframe) 
        iframe += 1
        already_sorted = True
        for j in range(count - i -1):
            
            #get materials
            mat1 = arr[j].active_material.diffuse_color
            mat2 = arr[j + 1].active_material.diffuse_color
            
            #get RG values from materials
            rg1, rg2 = get_rg(mat1, mat2)
            
            #compare first colorarray values
            if rg1 > rg2: 
            
                #change location & insert keyframes based on bubble sort
                arr[j].location.x = (j+1)*2
                arr[j].keyframe_insert(data_path="location", frame=iframe+1)

                arr[j+1].location.x = j*2
                arr[j+1].keyframe_insert(data_path="location", frame=iframe+1)       
                
                #rearrange arrays
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                already_sorted = False
                
        if already_sorted:
            break
        
    return iframe

############################################################
# Shell Sort Algorithm
############################################################

def shell_sort(arr, count, iframe):
    
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
                
                #compare RG values
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
    return iframe

############################################################
# Setup Random Colors + Array to be sorted
############################################################

def setup_array(count, variation):

    print(str(variation)+ "/6 start setup_array") 

    #fill array with numbers between 0 & count - 1
    index = list(range(count))

    #initialize 2d array
    Matrix = [[0 for x in range(count)] for y in range(count)] 
    
    #initialize plane array
    planes = [0 for i in range(count*count)]
    
    #initialize material array
    materials = [0 for i in range(count)]
    
    #transform every parent to create a cube made of planes
    offset = 0
    rotationX = 0
    rotationZ = 0
    moveX = 0
    moveY = 0
    moveZ = 0
    if variation == 1:
        offset = -0.1
    if variation == 2:
        offset = 0.1
        rotationX = 90
    if variation == 3:
        offset = 0.1
        moveY = count * -2
    if variation == 4:
        offset = -0.1
        rotationX = 90
        moveZ = count * 2
    if variation == 5:
        offset = 0.1
        rotationZ = -90
    if variation == 6:
        offset = -0.1
        rotationZ = -90
        moveX = count * 2  
    
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
    
    print("variables initialized and color arrays created")     
   
    #creating count * count planes with location.x = j * 2 and location.z = i * 2
    for i in range(count):
        for j in range(count):
            bpy.ops.mesh.primitive_plane_add(location=(j*2, 0, i*2), rotation=(pi / 2, 0, 0), scale=(0.1, 0.1, 0.1)) 
            planes[j+i*count] = bpy.context.active_object
    
    print("planes created and added to array") 
    
    #create parent for pivot point
    bpy.ops.mesh.primitive_plane_add(location=(0, offset, 0), rotation=(pi / 2, 0, 0), scale=(0.1, 0.1, 0.1))
    
    #name parent object to Parent
    bpy.context.active_object.name = "Parent"+str(variation)
    
    #set background material for merge sort
    materialParent = bpy.data.materials.new(name="Parent")
    materialParent.diffuse_color = (255, 0, 0, 255)
    bpy.data.objects["Parent"+str(variation)].data.materials.append(materialParent)
    
    #set cursor location
    bpy.context.scene.cursor.location = (-1, 0, -1)
    
    #set origin to cursor
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
    bpy.ops.transform.resize(value=(count, 1, count))
        
    #adding all planes to an array and parenting
    for plane in planes:
        #set parent and apply transform to avoid distortion
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
        parent = bpy.data.objects["Parent"+str(variation)]
        plane.parent = parent
        
    print("added planes to parent")
        
    #set origin to cursor again
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
    
    #rotationX
    bpy.context.active_object.rotation_euler[0] = math.radians(rotationX)
    
    #rotationZ
    bpy.context.active_object.rotation_euler[2] = math.radians(rotationZ)
    
    bpy.data.objects["Parent"+str(variation)].location = (moveX,moveY,moveZ)

    #sorts list of all objects based primary on their location.x and secondary on their location.z
    planes.sort(key = lambda obj: obj.location.z + obj.location.x/(count*count))
    
    #adding materials to array and set colorgradient 
    for i in range(count):
        for j in range(count):
                material = bpy.data.materials.new(name="")
                material.diffuse_color = (colors_r[i], colors_g[i], colors_b[i], 255)
                materials[i] = material  
    
    print("material array created")
    
    #add materials to planes and planes to 2d array              
    for i in range(count):
        #randomize distribution of colors for every row
        random.shuffle(materials)
        for j in range(count):
                planes[j+i*count].data.materials.append(materials[j]) #add the material to the object
                Matrix[i][j] = planes[j+i*count]
                
    print("appended materials to planes")
     
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

#size of cube(only whole numbers are valid)
size = 10

#delete every existing object
for ob in bpy.data.objects:   
    bpy.data.objects.remove(ob)    
    
#delete all existing materials
for material in bpy.data.materials:
        bpy.data.materials.remove(material, do_unlink=True)

#start at frame 0
main_frame = 0
Matrix1, count1 = setup_array(size, 1)

#shell_sort every array
print("starting shell_sort")
highest_1_iframe = 0
for i in range(count1):
    iframe = shell_sort(Matrix1[i], count1, main_frame)
    if iframe > highest_1_iframe:  
        highest_1_iframe = iframe
print("shell_sort completed")
print("---------------------------------------")
highest_1_iframe += 25       
main_frame = highest_1_iframe 

Matrix2, count2 = setup_array(size, 2)

#insertion_sort every array
print("starting inertion_sort")
highest_2_iframe = 0
for i in range(count2):
    iframe = insertion_sort(Matrix2[i], count2, main_frame)
    if iframe > highest_2_iframe:  
        highest_2_iframe = iframe     
print("insertion_sort completed")
print("---------------------------------------")
highest_2_iframe += 25      
main_frame = highest_2_iframe 

Matrix3, count3 = setup_array(size, 3)

#bubble_sort every array
print("starting bubble_sort")
highest_3_iframe = 0
for i in range(count3):
    iframe = bubble_sort(Matrix3[i], count3, main_frame)
    if iframe > highest_3_iframe:  
        highest_3_iframe = iframe
print("bubble_sort completed")
print("---------------------------------------")
highest_3_iframe += 25  
main_frame = highest_3_iframe

Matrix4, count4 = setup_array(size, 4)

#quick_sort every array
highest_4_iframe = 0
print("starting quick_sort")
for i in range(count4):
    iframe = main_frame
    quick_sort(i, Matrix4[i], 0, count4 - 1)
    if iframe > highest_4_iframe:  
        highest_4_iframe = iframe
print("quick_sort completed")
print("---------------------------------------")
highest_4_iframe += 25      
main_frame = highest_4_iframe    

Matrix5, count5 = setup_array(size, 5)

#selection_sort every array
print("starting selection shell_sort")
highest_5_iframe = 0
for i in range(count5):
    iframe = selection_sort(Matrix5[i], count5, main_frame)
    if iframe > highest_5_iframe:  
        highest_5_iframe = iframe
print("selection_sort completed")
print("---------------------------------------")
highest_5_iframe += 25  
main_frame = highest_5_iframe

Matrix6, count6 = setup_array(size, 6)

#merge_sort every array
print("starting merge_sort")
for i in range(count6):
    iframe = main_frame
    merge_sort(i,Matrix6[i],  0, count6-1)
print("merge_sort completed")

#rename every parent to the belonging sorting algorithm
bpy.data.objects["Parent1"].name = "shell_sort"
bpy.data.objects["Parent2"].name = "insertion_sort"
bpy.data.objects["Parent3"].name = "bubble_sort"
bpy.data.objects["Parent4"].name = "quick_sort"
bpy.data.objects["Parent5"].name = "selection_sort"
bpy.data.objects["Parent6"].name = "merge_sort"

#create pivot object
bpy.ops.mesh.primitive_cube_add(location=(size, -size, size), rotation=(0, 0, 0), scale=(0.1, 0.1, 0.1))
middle_pivot = bpy.data.objects["Cube"]
middle_pivot.name = "middle_pivot"

bpy.data.objects["shell_sort"].parent = middle_pivot
bpy.data.objects["shell_sort"].matrix_parent_inverse = middle_pivot.matrix_world.inverted()

bpy.data.objects["insertion_sort"].parent = middle_pivot
bpy.data.objects["insertion_sort"].matrix_parent_inverse = middle_pivot.matrix_world.inverted()

bpy.data.objects["bubble_sort"].parent = middle_pivot
bpy.data.objects["bubble_sort"].matrix_parent_inverse = middle_pivot.matrix_world.inverted()

bpy.data.objects["quick_sort"].parent = middle_pivot
bpy.data.objects["quick_sort"].matrix_parent_inverse = middle_pivot.matrix_world.inverted()

bpy.data.objects["selection_sort"].parent = middle_pivot
bpy.data.objects["selection_sort"].matrix_parent_inverse = middle_pivot.matrix_world.inverted()

bpy.data.objects["merge_sort"].parent = middle_pivot
bpy.data.objects["merge_sort"].matrix_parent_inverse = middle_pivot.matrix_world.inverted()

middle_pivot.rotation_euler[0] = math.radians(0)
middle_pivot.keyframe_insert(data_path="rotation_euler", frame= highest_1_iframe-25)

middle_pivot.rotation_euler[0] = math.radians(90)
middle_pivot.keyframe_insert(data_path="rotation_euler", frame= highest_1_iframe)

middle_pivot.keyframe_insert(data_path="rotation_euler", frame= highest_2_iframe-25)
middle_pivot.rotation_euler[0] = math.radians(180)
middle_pivot.keyframe_insert(data_path="rotation_euler", frame= highest_2_iframe)

middle_pivot.keyframe_insert(data_path="rotation_euler", frame= highest_3_iframe-25)
middle_pivot.rotation_euler[0] = math.radians(270)
middle_pivot.keyframe_insert(data_path="rotation_euler", frame= highest_3_iframe)

middle_pivot.keyframe_insert(data_path="rotation_euler", frame= highest_4_iframe-25)
middle_pivot.rotation_euler[2] = math.radians(-90)
middle_pivot.keyframe_insert(data_path="rotation_euler", frame= highest_4_iframe)

middle_pivot.keyframe_insert(data_path="rotation_euler", frame= highest_5_iframe-25)
middle_pivot.rotation_euler[2] = math.radians(90)
middle_pivot.keyframe_insert(data_path="rotation_euler", frame= highest_5_iframe)