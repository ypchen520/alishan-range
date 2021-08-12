## Construct Binary Tree from Inorder and Postorder Traversal
* Given inorder and postorder traversal of a tree, construct the binary tree.
  * return a TreeNode (root)
* You may assume that duplicates do not exist in the tree.
# Solution
* Start with **the last item in the postorder sequence**, which is the root
* and then find the boundary of its left and right subtrees in the preorder sequence
  * all elements before the root node in the preorder sequence belong to the left subtree and
  * all elements that come after the root node belong to the right subtree
* We repeat this recursively for all nodes in the tree
  * base case: if start > end
  * right subtree first and then left subtree
    * need to keep track of the post order index
# Implementation
* use element to find index through a hash map
* Python
  * enumerate to get the index information
  * map **list** element to index and return as a **dictionary** in Python: 
    * DICT = {x:i for i,x in enumerate(LIST)}

