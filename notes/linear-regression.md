# Types of Supervised Learning

## Classification

When given labeled data (target) we need identify the mathematical service that best separates the labeled examples.

## Regression

We use regression when the target is not labeled but a range of possible values. When representing these data sets, X often denotes the features of the data set and Y denotes the target. This is then represented as:

> y = f(x)

Here, *f()* is a trained data set and machine learning algorithm that takes certain features *x* and predicts *y* values. However, in machine learning *f()* is known as the *hypothesis* or *h()* which has stuck from the earlier days of machine learning.

The machine learning algorithm *h()* can be based on a *linear* or more complicated *non-linear* types of algorithms. If we only have a single feature *x* then we call the algorithm *Univariate*, meaning, one variable and *Multivariate* refers to an algorithm that accepts multiple *x* values or features.

### Univariate Linear Regression

This is the simplest form of Supervised machine learning when we have a single *feature* which basically just chooses the best *line* that divides our data.

![Linear Regression](https://github.com/harperd/machine-learning/raw/master/images/linear-regression.png)

Linear regression just finding *y* using slope-intercept form where *b* is the y-intercept and *m* is the slope of the line.

> $\huge y\ =\ mx\ +\ b$

In machine learning, this is called our *hypothesis* function where we represent the equation as shown below where theta (*θ*) is a weight associated with feature *x*.

> $\huge h_{\theta }( x) =\theta _{0} \ +\ \theta _{1} x$

#### Cost Function: Choosing a Theta

In supervised learning we have a *training set* of data that is used to train our model. Our goal is to train our model to predict values for our function *h(x)* that are close to *y* (targets) from our training examples. In other words, given the *y* values in your training set (our known good answers), what is the closest *y* values we can predict using our machine learning linear regression algorithm *h(x)*? We want a good *fit* of the model where the difference between *h(x)* and our training set, *y* values, are minimized. 

We measure this by using the *Cost function* *J(θ0, θ1)* where *θ0* is a point on the *x* axis and *θ1* is a point on the *y* axis and the result of *J(θ0, θ1)* is *z*. This is also called the *Squared Error Function* which is the most commonly used for linear regression problems. Here, we want to get the results of our cost function *J()* as close to zero as possible.

> $\huge J( \theta _{0} ,\ \theta _{1}) =\frac{1}{2m}\sum\limits ^{m}_{i=1}\left( h_{\theta }\left( x^{( i)}\right) -y^{( i)}\right)^{2}$

> **NOTE:** Multiplying the result by 1/2m is purely for aesthetics. See: https://datascience.stackexchange.com/questions/10188/why-do-cost-functions-use-the-square-error

> **NOTE:** You will notice the *Sum of Squared Errors* used in many other equations used to measure cost or optimization. This is the part of the equation that measures the difference between your predicted *y* and the *y* of your training set as denoted by (y<sub>1</sub> - y<sub>2</sub>)<index>2</index> Squaring the value just makes it easier to work with.

When trying a range of values for *θ0* and *θ1* you will get a 3-D plot similar to the below where the optimal theta values are at the bottom of the bow. Again, *θ0* is a point on the *x* axis and *θ1* is a point on the *y* axis and the result of *J(θ0, θ1)* is *z*.

![](https://github.com/harperd/machine-learning/raw/master/images/cost-function-plot.jpg)

> **See Also:** [mplot3d Toolkit](https://matplotlib.org/tutorials/toolkits/mplot3d.html)

The cost function can be more easily understood by using a 2-D *Contour Plot* where the minimal theta values would lie somewhere near the center circle.

![](https://github.com/harperd/machine-learning/raw/master/images/cost-function-contour-plot.jpg)

> **See Also:** [Contour Plot with Matplotlib](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.contour.html)

> **See Also:** [Contour Plot demo with Matplotlib](https://matplotlib.org/gallery/images_contours_and_fields/contour_demo.html)