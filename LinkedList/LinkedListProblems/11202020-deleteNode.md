# Singly-linked list (typescript)
* ```typescript
 class ListNode {
     val: number
     next: ListNode | null
     constructor(val?: number, next?: ListNode | null) {
         this.val = (val===undefined ? 0 : val)
         this.next = (next===undefined ? null : next)
     }
 }```
* typescript
  * ?: (optional)(specific type)
    * **?** marks the member as being **optional** in the interface.
    * *the Elvis operator*
  * this.val = (val===undefined ? 0 : val)
  * null: Something is currently unavailable
  * undefined: Something hasn't been initialized
* ```Python3
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
```
# singly-linked list
* will not be given access to the **head** of the list
* will be given access to **the node to be deleted** directly
* the node to be deleted is **not a tail node** in the list
* The value of each node in the list is **unique**
# swap with next node
* The usual way of deleting a node node from a linked list is to *modify the next pointer of the node before it*, to point to the node after it
  * Since we do not have access to the node before the one we want to delete, we cannot modify the next pointer of that node in any way
* **Instead, we have to replace the value of the node we want to delete with the value in the node after it, and then delete the node after it**
  * Because we know that the node we want to delete is not the tail of the list, we can guarantee that this approach is possible
