# Minimize Deviation in Array

## Description

* given an array nums of n positive integers
* You can perform two types of operations on any element of the array any number of times:
  * If the element is even, divide it by 2.
  * If the element is odd, multiply it by 2.
* The deviation of the array is the maximum difference between any two elements in the array.
* Return the minimum deviation the array can have after performing some number of operations.

## Solution

### Hint

* Assume you start with the minimum possible value for each number so you can only multiply a number by 2 till it reaches its maximum possible value.
* If there is a better solution than the current one, then it must have either its maximum value less than the current maximum value, or the minimum value larger than the current minimum value.
* Since that we only increase numbers (multiply them by 2), we cannot decrease the current maximum value, so we must multiply the current minimum number by 2.

### Priority Queue (Max Heap)

* Python: 
  * [heapq](https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/)
    * will result in TLE if heapq.nsmallest() is used