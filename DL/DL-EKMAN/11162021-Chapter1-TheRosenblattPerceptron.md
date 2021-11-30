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

## Limitations of the Perceptron

* what happens if a straight line cannot separate the data points
  * exclusive OR (XOR)
* one of the key limitations
  * it can solve classification problems only where the classes are linearly separable
    * two dimensions: separated by a straight line

## Combining Multiple Perceptrons

* add yet another perceptron that uses the outputs of the previous perceptrons as its inputs
  * two-level feedforward network implementing XOR function

### Fully Connected Feedforward Network

* Fully connected
  * the output of each neuron in one layer is connected to all neurons in the next layer
* Feedforward
  * there are no backward connections
  * directed acyclic graph (DAG)

### Multilevel Neural Network

* an input layer
* one or more hidden layers
* an output layer
* a feedforward network is also known as a multilevel perceptron

### Deep Learning (DL)

* DL is a class of machine learning algorithms that use multiple layers of computational units where each layer learns its own representation of the input data. These representation are combined by later layers in a hierarchical fashion

## Implementing Perceptrons with Linear Algebra

* input examples: vectors
* perceptron weights: matrices
* dot products, matrix-vector multiplications, matrix multiplications
  * efficient implementation
    * NumPy
      * Basic Linear Algebra Subprograms (BLAS)
* graphics processing unit (GPU)
  * CUDA
  * cuBLAS
  * offload computations to the GPU

### Vector Notation

* a vector is typically known as an array
* column vectors
  * transpose: row vector
* element-wise operation
  * some hardware implementations can do the operations efficiently in parallel

### Dot Product

* the two vectors are of equal length
  * weighted sum
  * y = sign(w dot x)
* enable us to call an efficient library: NumPy

### Extending the vector to a 2D matrix

* vector: a special case of the more general concept of
  * a multidimensional structure: matrix
  * vector: dimension is 1
* matrix
  * we state the row first and the column second
* represent the weights for n neurons with n vectors by arranging them in a matrix
* transpose a matrix: element ij becomes element ji

### Matrix-vector multiplication

* only for cases where the number of columns in the matrix matches the number of elements in the vector
* results in
  * a vector with the same number of elements as there are rows in the matrix
  * y_i = sigma(a_ij * x_j)
* dot product between two vectors
  * consider each of the m+1 rows of the matrix as row vectors
  * doing m+1 dot products of the matrix rows and the x-vector
* y = Ax = a^T dot x
* m+1 perceptrons
  * each having n inputs plus the bias input
  * single input example consisting of n+1 values
  * w_i ^ T: row vector corresponding to a single neuron
* z = Wx
  * z contains m+1 elements

### Matrix-matrix multiplication

* c_ij = sigma(a_ik * b_kj)
* compute all the dot products between all row-vectors in matrix A and all column-vectors in matrix B
* perceptron
  * (m+1) perceptrons, each having n inputs + bias input
  * (p+1) input examples, each consisting of (n+1) values
    * input examples: column vectors

### Dot product as a matrix multiplication

* transpose vector a (column vector): becomes a matrix with a single row
* do matrix multiplication between a^T and b
* omit the dot product operator
* a dot b = a^T * b

### Extending to multidimensional tensors

* the more generalized concept: a tensor
  * a multidimensional array
* the input data is multidimensional
  * a color image
    * a 2D array of pixel values
    * each pixel consists of three components (RGB)
  * a collection of images as input values
    * a 4D tensor
* all the computations are typically reduced to a large number of dot products

## Geometric Interpretation of the Perceptron

* two-input perceptron (x1, x2)
  * 3D chart: x1, x2, z
* weighted sum (z-value) forms a plane
  * the actual output (y) of the perceptron
    * -1 if z < 0
    * 1 if z >= 0
    * a line on the plane
      * becomes a 2D chart with a line if we look at the 3D chart from above

## Understanding the Bias Term
