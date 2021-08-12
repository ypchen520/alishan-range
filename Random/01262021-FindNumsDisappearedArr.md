# Find All Numbers Disappeared in an Array

## Description

* Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
* Find all the elements of [1, n] inclusive that do not appear in this array.
* Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

## Solution

* utilize the index

### Python

* return the non-zero element among a list
  * return [i for i in ans if i != 0]
