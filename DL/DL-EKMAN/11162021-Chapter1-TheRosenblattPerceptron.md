# Chapter 1: The Rosenblatt Perceptron

## Perceptron

* an artificial neuron
  * a computational unit
  * a number of inputs
    * with an associated input weight
    * special bias input
  * a single output
    * 1 or -1 (perceptron)
* activation function
  * y = f(z)
  * for perceptron: sign function: signum function (y = sign(z))

## Example of a Two-Input Perceptron

* a NAND gate (Nielsen, 2015)
* although perceptrons are limited to outputting only one of two values (-1, +1), other neuron models can output a range of real numbers
* a learning algorithm that can be used to automatically design neural networks by learning from examples

## The Perceptron Learning Algorithm

* how we came up with these weights in the first place
* whether there is a general approach for determining the weights

### Supervised Learning Algorithm

* presented with
  * the input data
  * the desired output data (ground truth)
* unsupervised learning
  * the learning algorithm is responsible for **finding patterns in the data by itself**
  * Text Autocompletion with LSTM and Beam Search
    * find structure in natural language text
* training a model (network)
  * coming up with weights for a network consisting of one or more neurons

### The algorithm

* randomly initialize the weights
* select one input/output pair at random
* present the values x1, ..., xn to the perceptron to compute the output y
* if the output y is different from the ground truth for this input/output pair, adjust the weights in the following way
  * if y < 0, add eta * xi to each wi
  * if y < 0, subtract eta * xi from each wi
* repeat steps 2, 3, and 4 until the perceptron predicts all examples correctly
* eta: the learning rate
  * hyperparameter
* *Geometrical interpretation of the perceptron*
* the boundary is exactly where the weighted sum of the inputs is zero
  * w0x0 + w1x1 + w2x2 = 0
  * x2 = -w1/w2 * x1 - w0/w2
    * a straight line