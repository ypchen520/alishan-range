## Maximum Depth of Binary Tree
* A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node
# Solution
* If the tree is empty then return 0
* Else
  * Get the max depth of left subtree **recursively**  i.e., call maxDepth(tree->left-subtree)
  * Get the max depth of right subtree **recursively**  i.e., call maxDepth(tree->right-subtree)
  * Get the max of max depths of left and right subtrees and add 1 to it for the current node
# Solution - Python (Top down)
* return None
# Solution - Python (Bottom up)
* if not root:
  * return 0
* left_depth = self.maxDepth(root.left)
* right_depth = self.maxDepth(root.right)
* depth = max(left_depth, right_depth) + 1
* return depth
