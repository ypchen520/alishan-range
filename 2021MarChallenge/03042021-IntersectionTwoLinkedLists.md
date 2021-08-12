# Intersection of Two Linked Lists

## Description

* Write a program to find the node at which the intersection of two singly linked lists begins.
* Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
* Output: Reference of the node with value = 8
* Notes
  * If the two linked lists have no intersection at all, return null.
  * The linked lists must retain their original structure after the function returns.
  * You may assume there are no cycles anywhere in the entire linked structure.
  * Each value on each linked list is in the range [1, 10^9].
  * Your code should preferably run in O(n) time and use only O(1) memory.

## Solution

### Hash Table

### Using distance from intersection point

* observation
  * number of nodes in List A + distance from the head of List B to the intersection point = number of nodes in List B + distance from the head of List A to the intersection point
* Time complexity: O(M+N)