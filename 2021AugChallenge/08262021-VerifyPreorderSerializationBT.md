# Verify Preorder Serialization of a Binary Tree

## Description

* One way to serialize a binary tree is to use preorder traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as '#'
* For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where '#' represents a null node.
* Given a string of comma-separated values preorder, return true if it is a correct preorder traversal serialization of a binary tree.
* It is guaranteed that each comma-separated value in the string must be either an integer or a character '#' representing null pointer.
* You may assume that the input format is always valid.
  * For example, it could never contain two consecutive commas, such as "1,,3".
* Note: You are not allowed to reconstruct the tree.

## Solution

### Outdegree and Indegree

* if we consider null as leaves, then
  * all non-null node provides 2 outdegree and 1 indegree (2 children and 1 parent), except root
  * all null node provides 0 outdegree and 1 indegree (0 child and 1 parent).
* record the difference between out degree and in degree diff = outdegree - indegree
  * When the next node comes, we then decrease diff by 1, because the node provides an in degree. If the node is not null, we increase diff by 2, because it provides two out degrees
  * **If a serialization is correct, diff should never be negative and diff will be zero when finished**

### Stack
