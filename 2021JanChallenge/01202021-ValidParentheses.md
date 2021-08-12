# Valid Parentheses

## Description

* Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
* An input string is valid if:
  * Open brackets must be closed by the same type of brackets.
  * Open brackets must be closed in the correct order.

## Solution

### Hint

* An interesting property about a valid parenthesis expression is that a sub-expression of a valid expression should also be a valid expression.
* What if whenever we encounter a matching pair of parenthesis in the expression, we simply remove it from the expression? This would keep on shortening the expression. e.g.
* The **stack data** structure can come in handy here in representing this recursive structure of the problem. We can't really process this from the inside out because we don't have an idea about the overall structure. But, the stack can help us process this recursively i.e. **from outside to inwards**.

### Stack

* Declare an empty stack.
* Push an opening parenthesis on top of the stack.
* In case of a closing bracket, check if the stack is empty.
* If not, pop in a closing parenthesis if the top of the stack contains the corresponding opening parenthesis.
* If the parentheses are valid,​ then the stack will be empty once the input string finishes.

### Python

* list isEmpty
  * if not LIST:
* list remove and return the removed value
  * .pop(index)
