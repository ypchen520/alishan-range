# Count Good Nodes in Binary Tree

## Description

* Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
* Return the number of good nodes in the binary tree.

## Solution

### Hint

* Use DFS (Depth First Search) to traverse the tree, and constantly keep track of the current path maximum.

### DFS

```Java
class Solution {
    public int goodNodes(TreeNode root) {
        return helper(root, Integer.MIN_VALUE);
    }
    private int helper(TreeNode node, int maxVal){
        if(node == null) return 0;
        int res = node.val >= maxVal ? 1 : 0;
        res += helper(node.left, Math.max(node.val, maxVal));
        res += helper(node.right, Math.max(node.val, maxVal));
        return res;
    }
}
```