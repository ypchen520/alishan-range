# Valid Triangle Number

## Description

* Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

## Solution

### Two-pointer

* sort the array
* for i from n-1 to 2
  * left = 0 and right = i - 1
    * while left < right
