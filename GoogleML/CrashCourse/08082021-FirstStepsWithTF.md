# First Steps with TF

## Learning Objectives

* Learn enough about **NumPy** and **pandas** to understand ```tf.keras``` code.
* Learn how to use **Colabs**.
* Become familiar with linear regression code in tf.keras.
* Evaluate loss curves.
* Tune hyperparameters.

## [TensorFlow](https://www.tensorflow.org/)

* TensorFlow is an end-to-end open source platform for machine learning
* TensorFlow APIs are arranged hierarchically, with the high-level APIs built on the low-level APIs
  * Machine learning researchers use the low-level APIs to create and explore new machine learning algorithms
  * Hierarchy
    * High-level, object-oriented API: Estimators, tf.keras
    * reusable libraries for common model: tf.layers, tf.losses, tf.metrics
    * extensive control: low-level TF API
    * TF code can run on multiple platforms: CPU, GPU, TPU

### Colab

* Colab is Google's version of [Jupyter Notebook](https://jupyter.org/)
* two kinds of components
  * text cells
  * code cells
* must run code cells in order

### NumPy and pandas

* NumPy
  * simplifies representing arrays and performing linear algebra operations
  * np.array()
    * 2D array
  * np.zeros: populate a matrix with all ones
  * np.ones
  * np.arange(5,12)
    * includes the lower bound but not the upper bound
  * Populate arrays with random numbers
    * np.random.randint(low=50, high=101, size=(6))
      * includes the lower bound but not the upper bound
      * a 6-element vector
    * **To create random floating-point values between 0.0 and 1.0, call np.random.random**
      * np.random.random([6])
  * [**broadcasting**](https://developers.google.com/machine-learning/glossary/#broadcasting)
    * virtually expand the smaller operand to dimensions compatible for linear algebra
  * create a 15-element vector containing random floating-point value between -2 and +2
    * np.random.uniform(-2,2,size=15)
    * np.random.random([15]) * 4 - 2
* pandas
  * provides an easy way to represent datasets in memory

### Linear regression with tf.keras
