# Remove Nth Node From End of List

## Description

* Given the head of a linked list, remove the nth node from the end of the list and return its head.
* Follow up: Could you do this in one pass?

## Solution

### Hint

* Maintain two pointers and update one with a delay of n steps.

### Two pointers

* Maintain two pointers, the first will point to the head of the linked list and the second will point to the Nth node from the beginning.
* Now keep incrementing both the pointers by one at the same time until the second is pointing to the last node of the linked list
* After the operations from the previous step, first pointer should be pointing to the Nth node from the end by now. So, delete the node first pointer is pointing to
