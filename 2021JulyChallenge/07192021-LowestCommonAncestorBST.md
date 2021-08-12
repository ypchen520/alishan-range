# Lowest Common Ancestor of a Binary Search Tree

## Description

* Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
* According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

## Solution

### [Recursive](https://aaronice.gitbook.io/lintcode/trees/lowest-common-ancestor-of-a-binary-search-tree)

* BST
  * right.val > root.val > left.val
* three cases
  * if both p and q are larger than root.val
    * recursively search the right subtree
  * if both p and q are smaller than root.val
    * recursively search the left subtree
  * else
    * root is the split point and we've found the answer

### Iterative Approach

```Java
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {

        // Value of p
        int pVal = p.val;

        // Value of q;
        int qVal = q.val;

        // Start from the root node of the tree
        TreeNode node = root;

        // Traverse the tree
        while (node != null) {

            // Value of ancestor/parent node.
            int parentVal = node.val;

            if (pVal > parentVal && qVal > parentVal) {
                // If both p and q are greater than parent
                node = node.right;
            } else if (pVal < parentVal && qVal < parentVal) {
                // If both p and q are lesser than parent
                node = node.left;
            } else {
                // We have found the split point, i.e. the LCA node.
                return node;
            }
        }
        return null;
    }
}
```
