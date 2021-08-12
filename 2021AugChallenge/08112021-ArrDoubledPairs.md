# Array of Doubled Pairs

## Description

* Given an integer array of even length arr, return true if it is possible to reorder arr such that arr[2 * i + 1] = 2 * arr[2 * i] for every 0 <= i < len(arr) / 2, or false otherwise.

## Solution

### Greedy

* sort the array by the absolute values of the elements
  * check a pair of x, 2x at a time
    * among the unchecked elements, the current element with the least absolute value x must be paired with an element with the value 2x, otherwise we return false
      * use a map to keep track of duplicate values

### Java

* Map<Integer, Integer> count = new HashMap();
  * put()
  * getOrDefault
* **Arrays.sort(arr, Comparator.comparingInt(Math::abs))**
