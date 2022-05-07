# Decision Tree

## Family of Decision Tree Learning Algorithms

* ID3
* C4.5
* C5.0
* CART

### Classification and Regression Trees (CART)

* build a tree: which question to ask and when
* split/partition
* unmixed vs. mixed
* quantify the amount of uncertainty: Gini impurity
  * quantify how much a question reduces that uncertainty: information gain
* recursively build the tree

### What type of question we can ask

* a list of questions
* partition into two subsets: true or false

### Quantifying uncertainty

* The best question is the one that reduces the uncertainty the most
  * Gini impurity
    * **Impurity**
      * Chance of being incorrect if you randomly assign a label to an example in the same set
      * 0 ~ 1
      * low impurity
      * high impurity

### Find the best question to ask

* Information gain
  * partition the data and calculate the uncertainty of the child nodes that result

### Putting it all together

* recursion
