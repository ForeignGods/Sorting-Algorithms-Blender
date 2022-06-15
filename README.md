Table of contents
=================

<!--ts-->
   * [Introduction](#installation)
   * [Sorting Algorithms](#sorting-algorithms-blender)
      * [Bubble Sort](#bubble-sort)
      * [Insertion Sort](#insertion-sort)
      * [Selection Sort](#selection-sort)
      * [Shell Sort](#shell-sort)
      * [Merge Sort](#merge-sort)
      * [Quick Sort](#quick-sort)
   * [Big O](#sorting-algorithms-blender)
<!--te-->

# Sorting-Algorithms-Blender

Bubble Sort
===========

Bubble sort is one of the most straightforward sorting algorithms. Its name comes from the way the algorithm works: With every new pass, the largest element in the list “bubbles up” toward its correct position. 

Bubble sort consists of making multiple passes through a list, comparing elements one by one, and swapping adjacent items that are out of order. 

![bubble](https://user-images.githubusercontent.com/78089013/167689895-ba7e3ddd-6ea9-41e0-8767-0700b12b6664.gif)

Insertion Sort
===========

Like bubble sort, the insertion sort algorithm is straightforward to implement and understand. But unlike bubble sort, it builds the sorted list one element at a time by comparing each item with the rest of the list and inserting it into its correct position. This “insertion” procedure gives the algorithm its name.
![Inerstio](https://user-images.githubusercontent.com/78089013/170041841-1c114899-1ada-4278-9865-6939774f373f.gif)

Selection Sort
==============

The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.
<ul>
<li>The subarray which is already sorted.</li>
<li>Remaining subarray which is unsorted.</li>
</ul>
In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray. 

![SelectionSort](https://user-images.githubusercontent.com/78089013/171057662-f1bc5c22-5dcf-4242-ab0f-fe5a08bf4e1a.gif)

Shell Sort
==========

The shell sort algorithm extends the insertion sort algorithm and is very efficient in sorting widely unsorted arrays. The array is divided into sub-arrays and then insertion sort is applied. The algorithm is:
<ul>
<li>Calculate the value of the gap.</li>
<li>Divide the array into these sub-arrays.</li>
<li>Apply the insertion sort.</li>
<li>Repeat this process until the complete list is sorted.</li>
</ul>

![ShellSort](https://user-images.githubusercontent.com/78089013/171215871-4579c50c-f4ca-4f72-971c-1ebb644dfcb0.gif)

Merge Sort
==========

Merge sort uses the divide and conquer approach to sort the elements. It is one of the most popular and efficient sorting algorithm. It divides the given list into two equal halves, calls itself for the two halves and then merges the two sorted halves. We have to define the merge() function to perform the merging.

The sub-lists are divided again and again into halves until the list cannot be divided further. Then we combine the pair of one element lists into two-element lists, sorting them in the process. The sorted two-element pairs is merged into the four-element lists, and so on until we get the sorted list.

Quick Sort
==========

Like Merge Sort, QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways. 
<ul>
<li>Always pick first element as pivot.</li>
<li>Always pick last element as pivot.</li>
<li>Pick a random element as pivot.</li>
<li>Pick median as pivot. (implemented below)</li>
</ul>

The key process in quickSort is partition(). Target of partitions is, given an array and an element x of array as pivot, put x at its correct position in sorted array and put all smaller elements (smaller than x) before x, and put all greater elements (greater than x) after x. All this should be done in linear time.

![QuickSorty](https://user-images.githubusercontent.com/78089013/171415241-9cf86f0f-eff6-4f70-adaf-7f3e8687d1fa.gif)

Big O
=====

Big O notation is the language we use for talking about how long an algorithm takes to run. It's how we compare the efficiency of different approaches to a problem.
With Big O notation we express the runtime in terms of **how quickly it grows relative to the input, as the input gets arbitrarily large.**

Let's break that down:
<ul>
<li><strong>how quickly the runtime grows</strong>

It's hard to pin down the exact runtime of an algorithm. It depends on the speed of the processor, what else the computer is running, etc. So instead of talking about the runtime directly, we use big O notation to talk about how quickly the runtime grows.</li>
    
<li><strong>relative to the input</strong>

If we were measuring our runtime directly, we could express our speed in seconds. Since we're measuring how quickly our runtime grows, we need to express our speed in terms of...something else. With Big O notation, we use the size of the input, which we call "n". So we can say things like the runtime grows "on the order of the size of the input" (O(n)) or "on the order of the square of the size of the input" (O(n^2)).</li>
    
<li><strong>as the input gets arbitrarily</strong>

Our algorithm may have steps that seem expensive when "n" is small but are eclipsed eventually by other steps as "n" gets huge. For big O analysis, we care most about the stuff that grows fastest as the input grows, because everything else is quickly eclipsed as "n" gets very large. (If you know what an asymptote is, you might see why "big O analysis" is sometimes called "asymptotic analysis.")</li>
</ul>

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
