# Basic Calculator

## Description

* Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.
* Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

## Solution

### Stack

* Simple iterative solution by identifying characters one by one. One important thing is that the input is valid, which means the parentheses are always paired and in order.
Only 5 possible input we need to pay attention:
  * digit: it should be one digit from the current number
  * '+': number is over, we can add the previous number and start a new number
  * '-': same as above
  * '(': push the previous result and the sign into the stack, set result to 0, just calculate the new result within the parenthesis.
  * ')': pop out the top two numbers from stack, first one is the sign before this pair of parenthesis, second is the temporary result before this pair of parenthesis. We add them together.
  * Finally if there is only one number, from the above solution, we haven't add the number to the result, so we do a check see if the number is zero.
