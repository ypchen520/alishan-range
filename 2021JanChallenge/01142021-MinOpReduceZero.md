# Minimum Operations to Reduce X to Zero

## Description

* You are given an integer array nums and an integer x. 
* In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x.
* Note that this modifies the array for future operations.

* Return the minimum number of operations to reduce x to exactly 0 if it's possible, otherwise, return -1.

## Solution

### Hint

* Think in reverse; instead of finding the minimum prefix + suffix, find the maximum subarray.
* Finding the maximum subarray is standard and can be done greedily.

### maximum subarray

* Compute the sum of the array
* the target for the maximum subarray would be the sum minus the target value
* finding the length of the maximum subarray is equal to finding the answer to the question
  * sliding window

### Python

* sum(List)

### JAVA

* Java 8
  * int sum = Arrays.stream(arr).sum();
* Math.max()
* print
  * System.out.print
