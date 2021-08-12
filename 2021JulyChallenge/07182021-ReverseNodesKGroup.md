# Reverse Nodes in k-Group

## Description

* Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
* k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
* You may not alter the values in the list's nodes, only nodes themselves may be changed.

## [Solution](https://labuladong.gitbook.io/algo-en/iv.-high-frequency-interview-problem/reverse-nodes-in-k-group)

* reverse link list

  ```Java
  ListNode reverse(ListNode head){
      ListNode dummy, curr, next;
      prev = null, curr = head, next = head;
      while(curr != null){
          next = curr.next;
          curr.next = prev;
          // update pointer
          prev = curr;
          curr = next;
      }
      return prev;
  }
  ```

* reverse the nodes in the interval [a,b)
  
  ```Java
  ListNode reverse(ListNode a, ListNode b){
      ListNode dummy, curr, next;
      prev = null;
      curr = next = a;
      while(curr != b){
          next = curr.next;
          curr.next = prev;
          // update pointer
          prev = curr;
          curr = next;
      }
      return prev;
  }
  ```

* reverse k nodes at a time
  * locate the starting and ending pointers
  * recursively reverse each group of nodes
