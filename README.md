# linear-classification

Basic linear classification Algorithms
 
## Perceptron algorithms

### What they do?

Perceptron and average Perceptron find theta and theta_0 describing line dividing points into two positived labeled and negative labeled

### How they work


#### describing hyperplanes using vectors
we can describe the line as 

a*x+b*y+c = 0

we can see that ax+by is a [dot product](https://en.wikipedia.org/wiki/Dot_product) of vectors (x,y ) describing the point and (a,b) which is ussualy called theta (c in that description of line is ussualy called theta_0)

so we can describe line as

$$theta*point + theta_0 = 0$$

this will also work for higher dimension [hyperplanes](https://en.wikipedia.org/wiki/Hyperplane)

#### update step

every point in the training data set has also label value ($label = 1$ or $label = -1$)

when points is missclasified by current $ theta $ and $ theta_0 $
$$ label*(theta*point + theta_0) \leq 0$$

then we update percepton
$$ theta = theta+label*point $$
$$ theta_0 = theta_0 + label $$

NOTICE: this will not necessarily make theta and theta_0 correct but it will always improve it.

