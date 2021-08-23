# Maximum Product of Splitted Binary Tree

## Description

* Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.
* Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.
* Note that you need to maximize the answer before taking the mod and not after taking it.

## Solution

### Hint

* If we know the sum of a subtree, the answer is max( (total_sum - subtree_sum) * subtree_sum) in each node.

### [Two-Pass](https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/discuss/496549/JavaC%2B%2BPython-Easy-and-Concise)
