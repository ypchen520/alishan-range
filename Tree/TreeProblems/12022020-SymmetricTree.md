## Symmetric Tree
* Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center)
# recursion
* Two trees are a mirror reflection of each other if:
  * Their two roots have the same value.
  * The right subtree of each tree is a mirror reflection of the left subtree of the other tree.
* the helper function: **isMirror()**
# iteration
* with the aid of a queue
* Each two **consecutive nodes** in the queue should be 
  * equal, and
  * their subtrees a mirror of each other.
* similar to BFS
* Each time, two nodes are extracted and their values compared.
* Then, the right and left children of the two nodes are inserted in the queue in opposite order.
* The algorithm is done when either the queue is empty, or we detect that the tree is not symmetric
