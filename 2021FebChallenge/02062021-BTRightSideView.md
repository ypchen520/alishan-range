# Binary Tree Right Side View

## Description

* Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

## Solution

### Level order traversal

* print the last node in every level

### Recursive traversal

* always traverse the right subtree first
* keep track of the maximum level that is traversed so far
* Python
  * use __init__ to keep track of the maximum value and the list that stores the answer
