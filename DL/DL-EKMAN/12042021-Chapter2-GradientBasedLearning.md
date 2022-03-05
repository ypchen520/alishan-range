# Chapter2: Gradient-Based Learning

* how the perceptron learning algorithm works

## Intuitive Explanation of the Perceptron Learning Algorithm

* the value of the learning rate parameter will only affect how quickly the algorithm converges

## Derivatives and Optimization Problems

* derivative of y w.r.t x
  * how much the value of y changes given a small change in x
* the tangent to a curve
  * a straight line with the same slope (derivative) as the curve at the location where the line touches the curve
* observations
  * the derivative at the point that minimizes the value of y is 0 (the tangent is horizontal)
* minimization problems
  * we can maximization problems into minimization problems by negating the function we want to maximize
* a function of two variables: y = f(x0, x1)
  * a landscape that can contain hills and valleys
    * discontinuities, asymptotes, and so on
  * **the gradient of the function (nabla ∇)**
    * a derivative but generalized to a function with muliple variables
    * ∇y = [∂y/∂x0, ∂y/∂x1]^T
* **The gradient has a geometric interpretation**
  * a direction and a magnitude
    * direction
      * defined in the same dimensional space as the inputs to the function
      * the direction of the steepest ascent
    * magnitude
      * the slope of the hill in that direction

## Solving a Learning Problem with Gradient Descent

* solving the equation: y - ŷ = 0 
* combine multiple training examples into a single error metric
  * mean squared error (MSE)
    * 1/m 𝚺 (yi - ŷi)^2
    * solve it for 0 is impossible
    * try to find weights that minimize the value of the error function
* a closed form solution
  * analytically solving an equation to find an exact solution
* a numerical method (gradient descent)
  * approximate solution

### Gradient descent

* iterative method
  * start with an initial guess
  * gradually refine it
* the sign of the derivative indicates whether we should increase or decrease x0 slightly
  * a positive slope: indicates that y will decrease if we decrease x
* the value of the derivative
  * whether the current value of x is close to or far away from the value that will minimize y
  * can be used to decide how much to adjust x: **xn+1 = xn - η f'(xn)**
    * η: learning rate
      * too large: fail to converge
      * too small: get stuck in a local minimum
* Newton's method

### Gradient descent for multidimensional functions

* a gradient: a vector consisting of partial derivatives
  * negative gradient: the direction of steepest descent
* at x = (x0, x1) and want to minimize y
  * next point: (x0, x1) - η∇y
  * generalizes to functions of any number of dimensions: x and ∇y are vectors consisting of n elements

## Constants and Variables in a Network

* consider input values (x) to be constants, with our goal being to adjust the weights (w)
* learnable parameters: the weights (w)

## Analytic Explanation of the Perceptron Learning Algorithm
  