# Reverse Linked List II

## Description

* Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

## Solution

### Iterative link reversal

* we reverse **the next pointers** for all the nodes in between
* understand how the link reversal will work and **what set of pointers** will be required
  * We can simply use these two pointers to reverse the link between A and B

    ```Java
    cur.next = prev
    ```

    * The only problem with this is, we don't have a way of progressing further
  * we need a third pointer that will help us continue the link reversal process

    ```Java
    third = cur.next
    cur.next = prev
    prev = cur
    cur = third
    ```
  