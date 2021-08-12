# Binary Tree Pruning

## Description

* Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has been removed.
* A subtree of a node node is node plus every node that is a descendant of node.

## Solution

### Recursion

* subtree
  * if
    * root == 1 or
    * root.left (keep searching the left subtree) or
    * root.right (keep searching the right subtree)
