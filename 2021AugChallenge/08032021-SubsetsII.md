# Subsets II

## Description

* Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
* The solution set must not contain duplicate subsets. Return the solution in any order.

## Solution

### [Recursion (DFS)](https://zxi.mytechroad.com/blog/searching/leetcode-90-subsets-ii/)

* [Java](https://zxi.mytechroad.com/blog/searching/leetcode-90-subsets-ii/)
* Sort the array first
* Start from each element
  * recursively add the next element to the current array while **avoid duplicates at the same time**
  * after the recursive call of the function, pop the last element of the current array to search with the next starting point
* DFS
  * For each recursive call of the helper function, add the current array to the result list first
    * in Java, we have to allocate memory for the current array as the following since we are going to remove the last element of the current array to search for other combinations

      ```Java
      res.add(new ArrayList<Integer>(curr))
      ```
  
      ```Java
      res.add(curr)
      ```
