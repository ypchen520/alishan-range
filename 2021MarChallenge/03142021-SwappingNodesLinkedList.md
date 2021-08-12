# Swapping Nodes in a Linked List

## Description

* You are given the head of a linked list, and an integer k.
* Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

## Solution

### Hint

* We can transform the linked list to an array this should ease things up
* After transforming the linked list to an array it becomes as easy as swapping two integers in an array then rebuilding the linked list

### Explanation

* As it's not asked to swap the actual node with its address so we can simply just swap the values of the nodes instead of swapping the nodes
* Step 1: Point to k-th node from the beginning
* Step 2: Point to k-th node from the end
  * this would be the (n-k)the node from the beginning, where n is the length of the list
* Step-3: Swap values of both the nodes.
