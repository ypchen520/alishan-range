# Is Graph Bipartite?

## Description

* There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:
  * There are no self-edges (graph[u] does not contain u).
  * There are no parallel edges (graph[u] does not contain duplicate values).
  * If v is in graph[u], then u is in graph[v] (the graph is undirected).
  * The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
* A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

## Solution

### BFS

* The easy solution here is just to run a breadth first search approach using a stack (or queue)
* We can pick a random starting node and assign it to a group
* We then need to check each next node connected to our current node (curr)
  * if it's been assigned to a group and that group is the same as curr, then this graph is not bipartite and we should return false
  * If it hasn't been assigned, we should assign it to the opposite group of curr and move it onto the stack to check.
* But what if the graph is made up of several disconnected sections? In that case, we need to perform the previous step several times, so we'll need to iterate through the entire graph and skip any nodes that have already been assigned in a previous segment.
  * If we reach the end without error, then we can return true.
* In order to keep track of assignments, we can use a "visited" array (vis). In this case, 0 means that this node hasn't been visited, and 1 or 2 are the assigned groups. To quickly assign next to the opposite of curr, we can use a **bitwise XOR with 3**
  * 1 ^ 3  =  2
  * 2 ^ 3  =  1
