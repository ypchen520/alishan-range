# Search in an Array

* More often than not, it comes down to **the speed of searching for an element** in a data structure that helps programmers make design choices for their codebases.
* Searching
  * find an occurrence of a particular element in the Array and return its position
    * whether or not an element is present
    * determing which index to insert a new element at
  * If we know the **index** in the Array that may contain the element we're looking for, then the search becomes a **constant time** operation

## Linear Search

* check every element in the Array.
* We continue checking elements until we find the element we're looking for, or we reach the end of the Array.
* In the worst case, a linear search ends up checking the entire Array.
  * time complexity is O(N)

## [Binary Search](https://leetcode.com/explore/learn/card/binary-search/)

* If the elements in the Array are in **sorted order**, then we can use binary search
* repeatedly look at the middle element
  * determine whether the element we're looking for must be to the left, or to the right
    * halve the number of elements we still need to search each time
* If we're going to be performing **a lot of searches**, it is often worth **sorting the data first** (O(nlogn)) so that we can use binary search for the repeated searches.
