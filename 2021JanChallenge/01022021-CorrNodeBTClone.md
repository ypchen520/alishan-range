# Find a Corresponding Node of a Binary Tree in a Clone of That Tree

## Description

* Given two binary trees original and cloned and given a reference to a node target in the original tree
* Return a reference to the same node in the cloned tree
* Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree
* Constraints:
  * The number of nodes in the tree is in the range [1, 10^4].
  * The values of the nodes of the tree are unique.
  * target node is a node from the original tree and is not null.

## Solution

* BFS
  * use queue (FIFO)
  * enqueue the root
  * while queue.isEmpty() == False // is not empty
    * pop
    * examine
    * enqueue the left subtree and the right subtree
* create a new class to hold both the original tree and the cloned tree.
