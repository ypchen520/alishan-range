# Create Sorted Array through Instructions

## Description

* Given an integer array instructions, you are asked to create a sorted array from the elements in instructions. You start with an empty container nums. For each element from left to right in instructions, insert it into nums. The cost of each insertion is the minimum of the following:
  * The number of elements currently in nums that are strictly less than instructions[i]
  * The number of elements currently in nums that are strictly greater than instructions[i]

## Solution

* This problem is closely related to finding the number of inversions in an array
* If I know the position in which I will insert the i-th element in I can find the minimum cost to insert it

### Binary indexed tree (Fenwick tree)

* a data structure that can efficiently update elements and **calculate prefix sums** in a table of numbers
* consider the following problem: We have an array arr[0 . . . n-1]. We would like to
  1. Compute the sum of the first i elements.
  2. Modify the value of a specified element of the array arr[i] = x where 0 <= i <= n-1
* Binary indexed tree and Segment tree perform both operations in **O(logn) time**
  * Binary indexed tree requires less space and is easier to implement
* Binary Indexed Tree is represented as an array
  * the size of the Binary Indexed Tree is equal to the size of the input array (n)
  * Each node stores the sum of some elements of the input array
  * the idea is based on the fact that
    * all positive integers can be represented as the sum of powers of 2
  * Every node
    * stores the sum of n elements where n is a power of 2
  * we traverse at-most O(Logn) nodes in both getSum() and update() operations. The time complexity of the construction is O(nLogn) as it calls update() for all n elements
* implementation 
  * constructBIT()
    * for i in range(n):
      * updateBIT()
  * updateBIT()
    * index of parent can be obtained using the following formula
      * parent = i + i & (-i)
        * &: bitwise AND operator
        * negative value: two's complement
        * Adding to the last (rightmost) bit that equals 1 (set)
  * get_sum()
    * index of parent can be obtained using the following formula
      * parent = i - i & (-i)
        * removing the last (rightmost) bit that equals 1 (set)
* https://www.topcoder.com/community/competitive-programming/tutorials/binary-indexed-trees/
* https://www.krammerliu.com/blog/leetcode-1649-create-sorted-array-through-instructions/

### Segment tree

### Binary Search (Time Limit Exceeded)

* We create a new array and insert the first element if it’s empty.
* Now for every new element, we find the correct position for the element in the new array using binary search 
* and then insert that element at the corresponding index in the new array.
* mid = start + (end - start) // 2

### Python

#### list

* .insert(index, val)
