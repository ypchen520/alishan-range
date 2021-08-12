# Reducing Loss

## Learning Objectives

* Discover how to train a model using an iterative approach
* Understand full gradient descent and some variants
  * mini-batch gradient descent
  * stochastic gradient descent
* Experiment with learning rate

## How do we reduce loss

* a direction to go in the parameter space
  * gradient: derivative
* how large of a step to take in the negative gradient direction
  * learning rate
    * **too large: diverge**
* gradient descent
  * where do we start?

## Weight Initialization

* For **convex** problems, weights can start anywhere
  * a bowl shape
* Neural nets
  * **non-convex**

## SGD & Mini-Batch Gradient Descent

* Could compute gradient over entire data set on each step (full-batch)
* Stochastic gradient descent
  * one example at a time
  * **a batch size of 1**
* Mini-Batch gradient descent
  * batch of 10-1000

## Key Terms

* convergence
* gradient descent
* step
  * a forward and backward evaluation of one **batch**
* batch
  * the set of examples used in one iteration (i.e., one gradient update) of model training
* batch size
* SGD
* hyperparameter
* learning rate
  * step size
