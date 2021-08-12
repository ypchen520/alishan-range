# Shortest Unsorted Continuous Subarray

## Description

* Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.
* Return the shortest such subarray and output its length.

## Solution

### Sorting

* We can sort a copy of the given array numsnums, say given by nums_sorted
* Then, if we compare the elements of numsnums and nums_sorted, we can determine the leftmost and rightmost elements which mismatch. 
* The subarray lying between them is, then, the required shorted unsorted subarray.
