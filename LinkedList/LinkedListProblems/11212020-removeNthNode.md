# Remove Nth Node
* Given the head of a linked list
  * remove the nth node *from the end*
* one pass?
# Two Pass
* the key is to find the **list length L**
* add an auxiliary "dummy" node
  * points to the list head
  * corner cases (edge cases)
    * list with only one node
    * removing the head of the list
* Algorithm
  * find the list length L
  * set a pointer to the dummy node
  * traverse the list to the (L-n)th node
    * ```let traverse: ListNode = head;```
  * point the next pointer of the (L-n)th node to the (L-n+2)th node
  * **linked list**
    * dummy.next = head
    * traverse = dummy
      * traverse.next also points to the same *head*, which means modification will apply to *dummy*
* Time complexity: O(L)
  * 2L - n
* Space complexity: O(1)
# One Pass
* instead of only using a single pointer, we could use **two pointers**
* separate the two pointers by n nodes apart: 
  * The first pointer advances the list by **n+1** steps from the beginning
  * while the second pointer starts from the beginning of the list
* Time complexity: O(L)
  * makes only one traversal of the list of L nodes
* Space complexity: O(1)
