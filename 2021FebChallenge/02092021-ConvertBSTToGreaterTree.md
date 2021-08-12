# Convert BST to Greater Tree

## Description

* Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

## Solution

### Recursion

* Traverse the right subtree first so that sum of all greater nodes is stored at the summation pointer
* add the root key to the summation
* update the root key to the summation
* traverse the left subtree
