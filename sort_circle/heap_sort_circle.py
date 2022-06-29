import bpy
import random
import math 
from array import *
from math import pi
from mathutils import Vector, Matrix
import numpy as np
import colorsys

############################################################
# Heap Sort Algorithm
############################################################
        
def heapify(arr, n, i):
    
    global iframe
    
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
  
    try:

        hsv1 = mat_to_hsv(arr[largest])
        hsv2 = mat_to_hsv(arr[l])
        
    except:
        print("l to big")
        
    # See if left child of root exists and is greater than root
    if l < n and hsv1 < hsv2:
        largest = l
  
    try:
        hsv1 = mat_to_hsv(arr[largest])
        hsv2 = mat_to_hsv(arr[r])
                
    except:
        print("r to big")

    # See if right child of root exists and is greater than root
    if r < n and hsv1 < hsv2:
        largest = r
  
    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        
        a = arr[i].rotation_euler.y 
        b = arr[largest].rotation_euler.y 
           
        arr[i].rotation_euler.y = b
        arr[largest].rotation_euler.y = a
        
        for cube in planes:
            cube.keyframe_insert(data_path="rotation_euler", frame=iframe) 
        
        iframe += 1
        
        # Heapify the root.
        heapify(arr, n, largest)
  
# The main function to sort an array of given size
def heap_sort(arr):
   
    n = len(arr)

    global iframe
    
    # Build a maxheap.
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
  
    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        
        a = arr[i].rotation_euler.y
        b = arr[0].rotation_euler.y
        
        arr[i].rotation_euler.y = b
        arr[0].rotation_euler.y = a
        
        for cube in planes:
            cube.keyframe_insert(data_path="rotation_euler", frame=iframe) 
        
        iframe += 1
        
        heapify(arr, i, 0)
        
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

iframe= 0
heap_sort(planes)
