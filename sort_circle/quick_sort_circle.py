import bpy
import random
import math 
from array import *
from math import pi
from mathutils import Vector, Matrix
import numpy as np
import colorsys

############################################################
# Quick Sort Algorithm
############################################################

# function to find the partition position
def partition(array, low, high):
    
    global iframe
           
    pivot = array[(high + low) // 2]
    
    # pointer for greater element
    i = low 
    j = high
    while True:
        
        hsv1 = mat_to_hsv(array[i])
        hsv2 = mat_to_hsv(pivot)
        
        while hsv1 < hsv2:
            i += 1
            hsv1 = mat_to_hsv(array[i])
            hsv2 = mat_to_hsv(pivot)
        
        hsv3 = mat_to_hsv(array[j])
        hsv4 = mat_to_hsv(pivot)
        
        while hsv3 > hsv4:
            j -= 1
            hsv3 = mat_to_hsv(array[j])
            hsv4 = mat_to_hsv(pivot)
                    
        if i >= j:
            return j
        
        else:
            iframe += 1
            for cube in planes:
                cube.keyframe_insert(data_path="rotation_euler", frame=iframe)
        
        array[i].rotation_euler.y = math.radians(j * 2)
        array[j].rotation_euler.y = math.radians(i * 2)
            
        array[i].keyframe_insert(data_path="rotation_euler", frame=iframe)
        array[j].keyframe_insert(data_path="rotation_euler", frame=iframe)
                            
        # swapping element at i with element at j
        array[i], array[j] = array[j], array[i]
        i+=1;
        j-=1;

# function to perform quicksort
def quick_sort(array, low, high):
    if low < high: 
        # find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        piv = partition(array, low, high)
        
        # recursive call on the left of pivot
        quick_sort(array, low, piv)

        # recursive call on the right of pivot
        quick_sort(array, piv + 1, high)

###########################################################
# Convert RGB to single HSV from Material 
###########################################################

def mat_to_hsv(ob):

    #get materials
    mat = ob.active_material.diffuse_color
      
    #get R value 
    r = mat[0]
    
    #get G value 
    g = mat[1]
    
    #get b value
    b = mat[2]

    hsv = colorsys.rgb_to_hsv(r, g, b)
    
    return hsv

###########################################################
# #Set origin of cube to bottom of mesh
###########################################################

def origin_to_bottom(ob, matrix=Matrix()):
    me = ob.data
    mw = ob.matrix_world
    local_verts = [matrix @ Vector(v[:]) for v in ob.bound_box]
    o = sum(local_verts, Vector()) / 8
    o.z = min(v.z for v in local_verts)
    o = matrix.inverted() @ o
    me.transform(Matrix.Translation(-o))
    mw.translation = mw @ o
        
###########################################################
# Setup Random Colors + Array of Cubes to be sorted
###########################################################

def setup_array(count):
    
    #set optimal color managment setting 
    bpy.context.scene.view_settings.exposure = -3.75
    bpy.context.scene.view_settings.gamma = 0.5
    bpy.context.scene.view_settings.look = 'Medium Contrast'
    bpy.context.scene.view_settings.view_transform = 'Standard'
    
    #fill array with numbers between 0 & count - 1
    index = list(range(count))

    #initialize plane array
    planes = [0 for i in range(count)]

    #initialize material array
    materials = [0 for i in range(count)]

    #create all r values for hsv circle
    colors_r = [0 for i in range(count)]
    colors_r1 = np.linspace(0, 255, count//6)
    colors_r2 = np.linspace(255, 255, count//6)
    colors_r3 = np.linspace(255, 255, count//6)
    colors_r4 = np.linspace(255, 0, count//6)
    colors_r5 = np.linspace(0, 0, count//6)
    colors_r6 = np.linspace(0, 0, count//6)
    
    for i in range(count):  
        if(i < count//6):
            colors_r[i]=colors_r1[i]
        elif(i < count//6 * 2):
            colors_r[i]=colors_r2[i-count//6]
        elif(i < count//6 * 3):
            colors_r[i]=colors_r3[i-count//6 * 2]
        elif(i < count//6 * 4):
            colors_r[i]=colors_r4[i-count//6 * 3]
        elif(i < count//6 * 5):
            colors_r[i]=colors_r5[i-count//6 * 4]
        elif(i < count//6 * 6):
            colors_r[i]=colors_r6[i-count//6 * 5]

    #create all g values for hsv circle
    colors_g = [0 for i in range(count)]
    colors_g1 = np.linspace(0, 0, count//6)
    colors_g2 = np.linspace(0, 0, count//6)
    colors_g3 = np.linspace(0, 255, count//6)
    colors_g4 = np.linspace(255, 255, count//6)
    colors_g5 = np.linspace(255, 255, count//6)
    colors_g6 = np.linspace(255, 0, count//6)
    for i in range(count):  
        if(i < count//6):
            colors_g[i]=colors_g1[i]
        elif(i < count//6 * 2):
            colors_g[i]=colors_g2[i-count//6]
        elif(i < count//6 * 3):
            colors_g[i]=colors_g3[i-count//6 * 2]
        elif(i < count//6 * 4):
            colors_g[i]=colors_g4[i-count//6 * 3]
        elif(i < count//6 * 5):
            colors_g[i]=colors_g5[i-count//6 * 4]
        elif(i < count//6 * 6):
            colors_g[i]=colors_g6[i-count//6 * 5]

    #create all b values for hsv circle
    colors_b = [0 for i in range(count)]
    colors_b1 = np.linspace(255, 255, count//6)
    colors_b2 = np.linspace(255, 0, count//6)
    colors_b3 = np.linspace(0, 0, count//6)
    colors_b4 = np.linspace(0, 0, count//6)
    colors_b5 = np.linspace(0, 255, count//6)
    colors_b6 = np.linspace(255, 255, count//6)
    for i in range(count):  
        if(i < count//6):
            colors_b[i]=colors_b1[i]
        elif(i < count//6 * 2):
            colors_b[i]=colors_b2[i-count//6]
        elif(i < count//6 * 3):
            colors_b[i]=colors_b3[i-count//6 * 2]
        elif(i < count//6 * 4):
            colors_b[i]=colors_b4[i-count//6 * 3]
        elif(i < count//6 * 5):
            colors_b[i]=colors_b5[i-count//6 * 4]
        elif(i < count//6 * 6):
            colors_b[i]=colors_b6[i-count//6 * 5]

    #delete every existing object
    for ob in bpy.data.objects:   
        bpy.data.objects.remove(ob)

    #delete all existing materials
    for material in bpy.data.materials:
        bpy.data.materials.remove(material, do_unlink=True)

    #creating count * count planes with location.x = j * 2 and location.z = i * 2
    for i in range(count):
        bpy.ops.mesh.primitive_cube_add(location=(0, -i/count, 0), rotation=(0, 0, 0), scale=(1, 1, 1)) 

    #adding all planes to an array
    i=0
    for ob in bpy.data.objects:
       planes[i]= ob
       origin_to_bottom(ob)
       ob.scale = (0.04525, 0.1, 1.25)
       ob.rotation_euler = (0, math.radians(i*2), 0)
       i+=1

    #adding materials to array and set colorgradient 
    for i in range(count):
        material = bpy.data.materials.new(name="")
        material.diffuse_color = (colors_r[i], colors_g[i], colors_b[i], 255)
        materials[i] = material  
    
    random.shuffle(index)
    #add materials to planes and planes to 2d array              
    for i in range(count):
        #randomize distribution of colors for every row
        planes[i].rotation_euler.y = math.radians(index[i]*2)
        planes[i].data.materials.append(materials[i]) #add the material to the object
    
    #sorts list of all objects based primary on their location.x and secondary on their location.z
    planes.sort(key = lambda obj: obj.rotation_euler.y)
    
    #add cone to cover up overlapping center planes
    bpy.ops.mesh.primitive_cone_add(location=(0, -1, -1), rotation=(math.radians(-90),0,0), scale =(2,2,1)) 
    
    return(planes, count)

############################################################
# Call Functions
############################################################

#setup_array(number of planes)
planes, count = setup_array(180)

iframe = 0
quick_sort(planes, 0, count - 1)     