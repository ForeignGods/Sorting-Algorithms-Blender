Sorting-Algorithms-Blender
==========================

Sorting algorithms visualized using the Blender Python API.

Table of contents
=================

<!--ts-->
   * [Description](#description)
   * [Sorting Algorithms](#sorting-algorithms)
      * [Bubble Sort](#bubble-sort)
      * [Insertion Sort](#insertion-sort)
      * [Selection Sort](#selection-sort)
      * [Shell Sort](#shell-sort)
      * [Merge Sort](#merge-sort)
      * [Quick Sort](#quick-sort)
   * [Big O](#big-o)
      * [What is Big O Notation?](#what-is-big-o-notation)
      * [Time Complexity Notations](#time-complexity-notations)
      * [Table of Sorting Algorithms](#table-of-sorting-algorithms)
<!--te-->

Description
===========
Running one of the scripts in this project generates primitive meshes in Blender, wich are animated to visualize various sorting algorithms.<br>
The three folders <strong>(sort_color, sort_combined, sort_scale)</strong> contain three different types of visualisation.

<ul>
<li><a href="https://github.com/ForeignGods/Sorting-Algorithms-Blender/blob/main/sort_color" target="_blank"><strong>sort_color: </strong></a>2D array of planes arragned into a square sorted based on color </li>
<li><a href="https://github.com/ForeignGods/Sorting-Algorithms-Blender/blob/main/sort_combined" target="_blank"><strong>sort_combined: </strong></a>multiple 2D arrays of planes arragned into a cube sorted based on color</li>
<li><a href="https://github.com/ForeignGods/Sorting-Algorithms-Blender/blob/main/sort_scale" target="_blank"><strong>sort_scale: </strong></a>array of cuboids sorted based on height + array access and comparison counter</li>
</ul>

[comment]: <> (Why you used the technologies you usedSome of the challenges you faced and features you hope to implement in the future4. How to Install and Run the ProjectIf you are working on a project that a user needs to install or run locally in a machine like a "POS", you should include the steps required to install your project and also the required dependencies if any.Provide a step-by-step description of how to get the development environment set and running.)

Sorting Algorithms
==================

## Bubble Sort

Bubble sort is one of the most straightforward sorting algorithms.<br>
Its name comes from the way the algorithm works: With every new pass, the largest element in the list “bubbles up” toward its correct position. 

Bubble sort consists of making multiple passes through a list, comparing elements one by one, and swapping adjacent items that are out of order. 
| <a href="https://github.com/ForeignGods/Sorting-Algorithms-Blender/blob/main/sort_scale/bubble_sort_scale.py" target="_blank">bubble_sort_scale.py</a>|<a href="https://github.com/ForeignGods/Sorting-Algorithms-Blender/blob/main/sort_color/bubble_sort_color.py" target="_blank">bubble_sort_color.py</a>| 
| ------------- |:-------------:| 
| ![BubbleSort2](https://user-images.githubusercontent.com/78089013/174035707-e1475bd4-a3c6-4e74-ba9f-30b57335adfe.gif)|![BubbleColor2](https://user-images.githubusercontent.com/78089013/174149862-2ed3c492-0987-4194-834f-fc5276299bcc.gif)| 

## Insertion Sort

Like bubble sort, the insertion sort algorithm is straightforward to implement and understand.<br>
But unlike bubble sort, it builds the sorted list one element at a time by comparing each item with the rest of the list and inserting it into its correct position.
This “insertion” procedure gives the algorithm its name.

| <a href="https://github.com/ForeignGods/Sorting-Algorithms-Blender/blob/main/sort_scale/insertion_sort_scale.py" target="_blank">insertion_sort_scale.py</a>|<a href="https://github.com/ForeignGods/Sorting-Algorithms-Blender/blob/main/sort_color/insertion_sort_color.py" target="_blank">insertion_sort_color.py</a>| 
| ------------- |:-------------:| 
|![InsertionSort2](https://user-images.githubusercontent.com/78089013/174035509-714265d2-4d27-4d77-b809-997f4e233feb.gif)|![InsertionColor](https://user-images.githubusercontent.com/78089013/174154736-ada0e27f-88d0-4707-ba99-14ed967cce21.gif)| 

## Selection Sort

The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning.<br> The algorithm maintains two subarrays in a given array.
<ul>
<li>The subarray which is already sorted.</li>
<li>Remaining subarray which is unsorted.</li>
</ul>
In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray. 

| <a href="https://github.com/ForeignGods/Sorting-Algorithms-Blender/blob/main/sort_scale/selection_sort_scale.py" target="_blank">selection_sort_scale.py</a>|<a href="https://github.com/ForeignGods/Sorting-Algorithms-Blender/blob/main/sort_color/selection_sort_color.py" target="_blank">selection_sort_color.py</a>| 
| ------------- |:-------------:| 
|![SelectionSort2](https://user-images.githubusercontent.com/78089013/174033035-b6b9527a-3d12-4844-b066-50b4cb9d11ef.gif)|![SelectionSort2](https://user-images.githubusercontent.com/78089013/174156159-605f5121-06c3-4314-a22c-5f7919bb9c44.gif)| 

## Shell Sort

The shell sort algorithm extends the insertion sort algorithm and is very efficient in sorting widely unsorted arrays.<br>
The array is divided into sub-arrays and then insertion sort is applied. The algorithm is:
<ul>
<li>Calculate the value of the gap.</li>
<li>Divide the array into these sub-arrays.</li>
<li>Apply the insertion sort.</li>
<li>Repeat this process until the complete list is sorted.</li>
</ul>

| <a href="https://github.com/ForeignGods/Sorting-Algorithms-Blender/blob/main/sort_scale/shell_sort_scale.py" target="_blank">shell_sort_scale.py</a>|<a href="https://github.com/ForeignGods/Sorting-Algorithms-Blender/blob/main/sort_color/shell_sort_color.py" target="_blank">shell_sort_color.py</a>| 
| ------------- |:-------------:| 
|![ShellSort2](https://user-images.githubusercontent.com/78089013/174032744-6d968c18-8fdb-4268-937f-55e910f8c4d5.gif)|![ShellColor](https://user-images.githubusercontent.com/78089013/174157836-a4571ad7-0fd1-4237-9fb2-dc2d730a64c7.gif)| 

## Merge Sort

Merge sort uses the divide and conquer approach to sort the elements. It is one of the most popular and efficient sorting algorithm.<br>
It divides the given list into two equal halves, calls itself for the two halves and then merges the two sorted halves.<br>
We have to define the merge() function to perform the merging.

The sub-lists are divided again and again into halves until the list cannot be divided further.<br>
Then we combine the pair of one element lists into two-element lists, sorting them in the process.<br>
The sorted two-element pairs is merged into the four-element lists, and so on until we get the sorted list.

| <a href="https://github.com/ForeignGods/Sorting-Algorithms-Blender/blob/main/sort_scale/merge_sort_scale.py" target="_blank">merge_sort_scale.py</a>|<a href="https://github.com/ForeignGods/Sorting-Algorithms-Blender/blob/main/sort_color/merge_sort_color.py" target="_blank">merge_sort_color.py</a>| 
| ------------- |:-------------:| 
|![MergeSort2](https://user-images.githubusercontent.com/78089013/174032376-9b9768aa-5891-468e-a7a9-1d494374c5a4.gif)|![MergeColor2](https://user-images.githubusercontent.com/78089013/174161064-3fff2b70-90db-425c-acab-0d87040ec205.gif)| 

## Quick Sort

Like Merge Sort, QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways. 
<ul>

<li>Always pick first element as pivot.</li>
<li>Always pick last element as pivot.</li>
<li>Pick a random element as pivot.</li>
<li>Pick median as pivot. (implemented below)</li>
</ul>

The key process in quickSort is partition(). Target of partitions is, given an array and an element x of array as pivot, put x at its correct position in sorted array and put all smaller elements (smaller than x) before x, and put all greater elements (greater than x) after x.<br>
All this should be done in linear time.

| <a href="https://github.com/ForeignGods/Sorting-Algorithms-Blender/blob/main/sort_scale/quick_sort_scale.py" target="_blank">quick_sort_scale.py</a>|<a href="https://github.com/ForeignGods/Sorting-Algorithms-Blender/blob/main/sort_color/quick_sort_color.py" target="_blank">quick_sort_color.py</a>| 
| ------------- |:-------------:| 
|![QuickSort2](https://user-images.githubusercontent.com/78089013/174031317-2c261df1-6786-42e5-be08-1a7f5fccbca6.gif)|![QuickColor](https://user-images.githubusercontent.com/78089013/174161905-a3a2d1bd-0064-4e23-92b3-50da150c6f0c.gif)| 

Big O
=====

### What is Big O Notation?

Big O notation is the language we use for talking about how long an algorithm takes to run.<br>
It's how we compare the efficiency of different approaches to a problem.<br>
With Big O notation we express the runtime in terms of **how quickly it grows relative to the input, as the input gets arbitrarily large.**

Let's break that down:
<ul>
<li><strong>how quickly the runtime grows</strong>

It's hard to pin down the exact runtime of an algorithm.<br> 
It depends on the speed of the processor, what else the computer is running, etc. So instead of talking about the runtime directly, we use big O notation to talk about how quickly the runtime grows.</li>
    
<li><strong>relative to the input</strong>

If we were measuring our runtime directly, we could express our speed in seconds.<br>
Since we're measuring how quickly our runtime grows, we need to express our speed in terms of...something else.<br>
With Big O notation, we use the size of the input, which we call "n".<br>
So we can say things like the runtime grows "on the order of the size of the input" (O(n)) or "on the order of the square of the size of the input" (O(n^2)).</li>
    
<li><strong>as the input gets arbitrarily</strong>

Our algorithm may have steps that seem expensive when "n" is small but are eclipsed eventually by other steps as "n" gets huge.<br> 
For big O analysis, we care most about the stuff that grows fastest as the input grows, because everything else is quickly eclipsed as "n" gets very large.</li>
</ul>

### Time Complexity Notations
 
These are the asymptotic notations that are used for calculating the time complexity of the sorting algorithms:
<ul>
<li>Big O Notation, O:</li>
  
It measures the upper limit of an algorithm's running time or the worst-case time complexity. It is known by O(n) for input size 'n'.

<li>Omega Notation, Ω:</li>

It measures the minimum time taken by algorithms to execute, and calculates the best case time complexity in sorting. It is known by Ω(n) for input size 'n'.

<li>Theta Notation, θ:</li>

It measures the average time taken by an algorithm to execute. Or, the lower bound and upper bound of an algorithm's running time. It is known by θ(n) for input size 'n'.
</ul>
  
### Table of Sorting Algorithms

<table>
    <tr>
      <th>Algorithm</th>
      <th colspan="3">Time Complexity</th>
      <th>Space Complexity</th>
    </tr>
    <tr>
      <th></th>
      <th>Best Case</th>
      <th>Average Case</th>
      <th>Worst Case</th>
      <th>Worst Case</th>
    </tr>
    <tr>
      <td><a href="http://en.wikipedia.org/wiki/Quicksort">Quick Sort</a></td>
      <td><code class="orange">Ω(n log(n))</code><br><img src="./img/bad.png" align="left"></td>
      <td><code class="orange">Θ(n log(n))</code><br><img src="./img/bad.png" align="left"></td>
      <td><code class="red">O(n^2)</code><br><img src="./img/horrible.png" align="left"></td>
      <td><code class="yellow-green">O(log(n))</code><br><img src="./img/good.png" align="left"></td>
    </tr>
    <tr>
      <td><a href="http://en.wikipedia.org/wiki/Merge_sort">Merge Sort</a></td>
      <td><code class="orange">Ω(n log(n))</code><br><img src="./img/bad.png" align="left"></td>
      <td><code class="orange">Θ(n log(n))</code><br><img src="./img/bad.png" align="left"></td>
      <td><code class="orange">O(n log(n))</code><br><img src="./img/bad.png" align="left"></td>
      <td><code class="yellow">O(n)</code><br><img src="./img/fair.png" align="left"></td>
    </tr>
    <tr>
      <td><a href="http://en.wikipedia.org/wiki/Timsort">Tim Sort</a></td>
      <td><code class="yellow">Ω(n)</code><br><img src="./img/fair.png" align="left"></td>
      <td><code class="orange">Θ(n log(n))</code><br><img src="./img/bad.png" align="left"></td>
      <td><code class="orange">O(n log(n))</code><br><img src="./img/bad.png" align="left"></td>
      <td><code class="yellow">O(n)</code><br><img src="./img/fair.png" align="left"></td>
    </tr>
    <tr>
      <td><a href="http://en.wikipedia.org/wiki/Heapsort">Heap Sort</a></td>
      <td><code class="orange">Ω(n log(n))</code><br><img src="./img/bad.png" align="left"></td>
      <td><code class="orange">Θ(n log(n))</code><br><img src="./img/bad.png" align="left"></td>
      <td><code class="orange">O(n log(n))</code><br><img src="./img/bad.png" align="left"></td>
      <td><code class="green">O(1)</code><br><img src="./img/excellent.png" align="left"></td>
    </tr>
    <tr>
      <td><a href="http://en.wikipedia.org/wiki/Bubble_sort">Bubble Sort</a></td>
      <td><code class="yellow">Ω(n)</code><br><img src="./img/fair.png" align="left"></td>
      <td><code class="red">Θ(n^2)</code><br><img src="./img/horrible.png" align="left"></td>
      <td><code class="red">O(n^2)</code><br><img src="./img/horrible.png" align="left"></td>
      <td><code class="green">O(1)</code><br><img src="./img/excellent.png" align="left"></td>
    </tr>
    <tr>
      <td><a href="http://en.wikipedia.org/wiki/Insertion_sort">Insertion Sort</a></td>
      <td><code class="yellow">Ω(n)</code><br><img src="./img/fair.png" align="left"></td>
      <td><code class="red">Θ(n^2)</code><br><img src="./img/horrible.png" align="left"></td>
      <td><code class="red">O(n^2)</code><br><img src="./img/horrible.png" align="left"></td>
      <td><code class="green">O(1)</code><br><img src="./img/excellent.png" align="left"></td>
    </tr>
    <tr>
      <td><a href="http://en.wikipedia.org/wiki/Selection_sort">Selection Sort</a></td>
      <td><code class="red">Ω(n^2)</code><br><img src="./img/horrible.png" align="left"></td>
      <td><code class="red">Θ(n^2)</code><br><img src="./img/horrible.png" align="left"></td>
      <td><code class="red">O(n^2)</code><br><img src="./img/horrible.png" align="left"></td>
      <td><code class="green">O(1)</code><br><img src="./img/excellent.png" align="left"></td>
    </tr>
    <tr>
      <td><a href="https://en.wikipedia.org/wiki/Tree_sort">Tree Sort</a></td>
      <td><code class="orange">Ω(n log(n))</code><br><img src="./img/bad.png" align="left"></td>
      <td><code class="orange">Θ(n log(n))</code><br><img src="./img/bad.png" align="left"></td>
      <td><code class="red">O(n^2)</code><br><img src="./img/horrible.png" align="left"></td>
      <td><code class="yellow">O(n)</code><br><img src="./img/fair.png" align="left"></td>
    </tr>
    <tr>
      <td><a href="http://en.wikipedia.org/wiki/Shellsort">Shell Sort</a></td>
      <td><code class="orange">Ω(n log(n))</code><br><img src="./img/bad.png" align="left"></td>
      <td><code class="red">Θ(n(log(n))^2)</code><br><img src="./img/horrible.png" align="left"></td>
      <td><code class="red">O(n(log(n))^2)</code><br><img src="./img/horrible.png" align="left"></td>
      <td><code class="green">O(1)</code><br><img src="./img/excellent.png" align="left"></td>
    </tr>
    <tr>
      <td><a rel="tooltip" title="Only for integers. k is a number of buckets" href="http://en.wikipedia.org/wiki/Bucket_sort">Bucket Sort</a></td>
      <td><code class="green">Ω(n+k)</code><br><img src="./img/excellent.png" align="left"></td>
      <td><code class="green">Θ(n+k)</code><br><img src="./img/excellent.png" align="left"></td>
      <td><code class="red">O(n^2)</code><br><img src="./img/horrible.png" align="left"></td>
      <td><code class="yellow">O(n)</code><br><img src="./img/fair.png" align="left"></td>
    </tr>
    <tr>
      <td><a rel="tooltip" title="Constant number of digits 'k'" href="http://en.wikipedia.org/wiki/Radix_sort">Radix Sort</a></td>
      <td><code class="green">Ω(nk)</code><br><img src="./img/excellent.png" align="left"></td>
      <td><code class="green">Θ(nk)</code><br><img src="./img/excellent.png" align="left"></td>
      <td><code class="green">O(nk)</code><br><img src="./img/excellent.png" align="left"></td>
      <td><code class="yellow">O(n+k)</code><br><img src="./img/fair.png" align="left"></td>
    </tr>
    <tr>
      <td><a rel="tooltip" title="Difference between maximum and minimum number 'k'" href="https://en.wikipedia.org/wiki/Counting_sort">Counting Sort</a></td>
      <td><code class="green">Ω(n+k)</code><br><img src="./img/excellent.png" align="left"></td>
      <td><code class="green">Θ(n+k)</code><br><img src="./img/excellent.png" align="left"></td>
      <td><code class="green">O(n+k)</code><br><img src="./img/excellent.png" align="left"></td>
      <td><code class="yellow">O(k)</code><br><img src="./img/fair.png" align="left"></td>
    </tr>
    <tr>
      <td><a href="https://en.wikipedia.org/wiki/Cubesort">Cube Sort</a></td>
      <td><code class="yellow">Ω(n)</code><br><img src="./img/fair.png" align="left"></td>
      <td><code class="orange">Θ(n log(n))</code><br><img src="./img/bad.png" align="left"></td>
      <td><code class="orange">O(n log(n))</code><br><img src="./img/bad.png" align="left"></td>
      <td><code class="yellow">O(n)</code><br><img src="./img/fair.png" align="left"></td>
   </tr>

</table>
