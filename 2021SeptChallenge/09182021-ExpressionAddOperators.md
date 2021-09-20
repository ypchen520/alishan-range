# Expression Add Operators

## Description

* Given a string num that contains only digits and an integer target, return all possibilities to add the binary operators '+', '-', or '*' between the digits of num so that the resultant expression evaluates to the target value.

## Solution

### Hint

* Note that a number can contain multiple digits.
* Since the question asks us to find all of the valid expressions, we need a way to iterate over all of them. (Hint: Recursion!)
* We can keep track of the expression string and evaluate it at the very end. But that would take a lot of time. Can we keep track of the expression's value as well so as to avoid the evaluation at the very end of recursion?
* Think carefully about the multiply operator. It has a higher precedence than the addition and subtraction operators.
* We simply need to keep track of the last operand in our expression and reverse it's effect on the expression's value while considering the multiply operator.

### Backtracking
