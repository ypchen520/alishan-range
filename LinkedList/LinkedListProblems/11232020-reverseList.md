# Reverse Linked List
* iteratively
  * While you are traversing the list, change the current node's next pointer to point to its previous element
    * Since a node does not have reference to its previous node, you must **store its previous element beforehand**
    * You also need **another pointer to store the next node** before changing the reference
  * prev
  * curr
  * while(curr != null)
  *   nextTemp = curr.next
  *   curr.next = prev
  *   prev = curr
  *   curr = nextTemp
  * return prev
* recursively
  * the key is to work backwards
  * Assume that the rest of the list had already been reversed, now how do I reverse the front part
  * We want nk+1’s next node to point to nk. So, nk.next.next = nk;
  * Be very careful that n1's next must point to Ø. If you forget about this, your linked list has a cycle in it 
  * Space complexity: O(n)
    * The extra space comes from **implicit stack space due to recursion**. The recursion could go up to n levels deep.
