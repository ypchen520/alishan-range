# Two Sum IV - Input is a BST

## Description

* Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.

## Solution

### Hash Table

* use a hash table to store the values of the BST nodes.
* each time we insert a new value to the hash table, check if the hash table contains target - value

### Inorder Traversal

* use an inorder traversal to store the values of the nodes in a sorted array
* use two pointers to find out if there's a sum of target
  * if arr[i] + arr[j] < target, i++
  * else, j--

```Java
private void inorderTraversal(TreeNode node, List<Integer> arr){
    if(node == null) return;
    inorderTraversal(node.left, arr);
    arr.add(node.val);
    inorderTraversal(node.right, arr);
}
```
