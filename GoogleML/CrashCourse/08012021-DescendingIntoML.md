# Descending into ML

* Linear regression is a method for finding the straight line or hyperplane that best fits a set of points

## Learning Objectives

* Refresh your memory on line fitting.
* Relate weights and biases in machine learning to **slope** and **offset** in line fitting.
* Understand "loss" in general and **squared loss** in particular.

## Learning from data

* y = wx + b
  * w: slope
  * b: bias (offset/y-intercept)
* loss (plot)
* how do we define loss?
  * L<sub>2</sub> Loss
    * squared error: (observation - prediction)<sup>2</sup>
  * minimizing loss across our entire dataset

## Key terms

* [bias (the bias term)](https://developers.google.com/machine-learning/glossary#bias)
  * an intercept or offset from an origin
  * b or w<sub>0</sub>
  * [bias (ethics/fairness)](https://developers.google.com/machine-learning/glossary#bias_ethics)
  * [prediction bias](https://developers.google.com/machine-learning/glossary#prediction_bias)
    * A value indicating how far apart the average of predictions is from the average of labels in the dataset.
* inference
  * to infer means to predict
  * applying the trained model to unlabeled examples
* linear regression
  * linear vs. logistic (sigmoid function)
  * regression vs. classification
* weight
  * a coefficient for a feature
  * an edge in a deep network
* empirical risk minimization (ERM)
* loss
* mean squared error (MSE)
  * squared loss / number of examples
* squared loss
* training
