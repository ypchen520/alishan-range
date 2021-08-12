# Two-Pointer in Linked List

## A classic problem: Given a linked list, determine if it has a cycle in it

* Use two pointers with different speed in a linked list:
  * If there is no cycle, the fast pointer will stop at the end of the linked list.
  * If there is a cycle, the fast pointer will eventually meet with the slow pointer.
* The remaining problem:
  * What should be the proper speed for the two pointers?
    * It is a safe choice to move the slow pointer one step at a time while moving the fast pointer two steps at a time.
    * For each iteration, the fast pointer will move one extra step.
    * If the length of the cycle is M, after M iterations, the fast pointer will definitely move one more cycle and catch up with the slow pointer
