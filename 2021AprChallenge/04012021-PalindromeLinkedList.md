# Palindrome Linked List

## Description

* Given the head of a singly linked list, return true if it is a palindrome.

## [Solution](https://www.geeksforgeeks.org/function-to-check-if-a-singly-linked-list-is-palindrome/)

### Stack

* Traverse the given list from head to tail and push every visited node to stack.
* Traverse the list again. For every visited node, pop a node from stack and compare data of popped node with currently visited node.
* If all nodes matched, then return true, else false.

### Reversing the list

### Recursion
