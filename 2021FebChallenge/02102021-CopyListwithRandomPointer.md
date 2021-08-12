# Copy List with Random Pointer

## Description

* A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.
* Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.
* Return the head of the copied linked list.
* The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
  * val: an integer representing Node.val
  * random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.

## Solution

### Hint

* Just iterate the linked list and create copies of the nodes on the go. Since a node can be referenced from multiple nodes due to the random pointers, make sure you are not making multiple copies of the same node.
* You may want to use extra space to keep **old node ---> new node mapping** to prevent creating multiples copies of same node.
* We can avoid using extra space for old node ---> new node mapping, by tweaking the original linked list. Simply interweave the nodes of the old and copied list. E.g.,
  * Old List: A --> B --> C --> D
  * InterWeaved List: A --> A' --> B --> B' --> C --> C' --> D --> D' 
* The interweaving is done using next pointers and we can make use of interweaved structure to get the correct reference nodes for random pointers.

### Interweaving

* Create the copy of node 1 and insert it between node 1 & node 2 in original Linked List, create a copy of 2 and insert it between 2 & 3. Continue in this fashion, add the copy of N after the Nth node
* Now copy the random link in this fashion
  * ```original->next->random= original->random->next;```
* Now restore the original and copy linked lists in this fashion in a single loop.
  * original->next = original->next->next;
  * copy->next = copy->next->next;

    ```python
    curr = head
        clone = head.next
        while curr.next:
           tmp = curr.next
           curr.next = curr.next.next
           curr = tmp
    ```
