# Count of Smaller Numbers After Self

## Description

* You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

## Solution

### Binary Search

* create an empty array
* start from the end of the input array
  * insert the element into the new empty array using **binary search**
    * whenever an element ```x``` is inserted into the new array
      * the **current** index of ```x``` will be the number of elements that are to the right of ```x``` and are smaller than ```x``` in the original array
      * notes
        * now the smaller elements will be to the left of ```x``` in the new array
        * only the **current** index is the one we want

### Insertion Sort
