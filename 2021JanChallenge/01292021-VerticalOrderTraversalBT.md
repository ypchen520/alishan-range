# Vertical Order Traversal of a Binary Tree

## Description

* Given the root of a binary tree, calculate the vertical order traversal of the binary tree.
* For each node at position (x, y), its left and right children will be at positions (x - 1, y - 1) and (x + 1, y - 1) respectively.
* The vertical order traversal of a binary tree is a list of non-empty reports for each unique x-coordinate from left to right. 
  * Each report is a list of all nodes at a given x-coordinate. 
  * The report should be primarily sorted by y-coordinate from highest y-coordinate to lowest. 
  * If any two nodes have the same y-coordinate in the report, the node with the smaller value should appear earlier.

## Solution

### Level Order/Preorder Traversal

* create an empty **map** with each key representing the horizontal distance from a node to the root node. 
* the value of the **map** maintains all nodes present at the same horizontal distance from the root node
* have to use level order since the lists should be ordered by the y-coordinate

### Python

```python
if not node:
    return
```

* deque
  * Deque is preferred over list in the cases where we need quicker append and pop operations from both the ends of container, as deque provides an O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity