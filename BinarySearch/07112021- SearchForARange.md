# Search for a Range

## Description

* Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
* If target is not found in the array, return [-1, -1].
* You must write an algorithm with O(log n) runtime complexity.

## Solution

### Binary Search

* two searches
  * find the start of the range
  * find the end of the range

* Keep searching for the leftmost value that is the same as the target value
  
  ```Java
  if(nums[mid] >= target){
      r = mid - 1;
  }else{
      l = mid + 1;
  }
  if(nums[mid] == target) idx = mid;
  ```
  