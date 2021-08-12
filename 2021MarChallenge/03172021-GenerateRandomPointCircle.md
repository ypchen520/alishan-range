# Generate Random Point in a Circle

## Description

* Given the radius and x-y positions of the center of a circle, write a function randPoint which generates a uniform random point in the circle.
* Note
  * input and output values are in floating-point.
  * radius and x-y position of the center of the circle is passed into the class constructor.
  * a point on the circumference of the circle is considered to be in the circle.
  * randPoint returns a size 2 array containing x-position and y-position of the random point, in that order.

## Solution

* [Why sqrt(random())?](https://programming.guide/random-point-within-circle.html)
  * [another explanation](https://dev.to/seanpgallivan/solution-generate-random-point-in-a-circle-ldh)
* Java
  * Give a uniformly random number between 0 and 1: Math.random()
