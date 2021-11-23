# Flatten a Multilevel Doubly Linked List

## Description

* You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example [below](https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/).
* Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.

## Solution

* Start form the head, move one step each time to the next node
* When meet with a node with child, say node p, follow its child chain to the end and connect the tail node with p.next
* Return to p and proceed until find next node with child
* Repeat until reach null
