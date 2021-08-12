## Populating Next Right Pointers in Each Node
* You are given a **perfect binary tree** where all leaves are on the same level, and every parent has two children
* Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
* Initially, all next pointers are set to NULL.
## Solution
* modify child's next label of each nodes level by level
* Start with the left most child
* Use the next pointer populated when traversing the previous level to traverse the current level
