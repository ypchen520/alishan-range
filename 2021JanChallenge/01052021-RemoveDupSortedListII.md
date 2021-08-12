# Remove Duplicates from Sorted List II 

## Description

* Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. 
* Return the linked list sorted as well.

## Solution

* declare a dummy node and assign the head to its **next** node
  * dummy = ListNode(0)
  * dummy.next = head
* maintain a **previous** node to keep the information of the previous block of nodes that have been checked for duplicates
  * previous = dummy
* and a **current** node for traversing the linked list
  * while curr:
    * // DO SOMETHING
    * curr = curr.next
* check for duplicates
  * while cur.next and cur.val == cur.next.val: 
    * cur = cur.next
* if previous == current
  * current is not updated, which means current.val != current.next.val
  * move both pointers (previous and current) forward by one node
* else
  * previous node is not moved
  * make the previous node point to current.next
    * skipping the entire sequence of nodes with the same value
