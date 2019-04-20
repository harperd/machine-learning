# Types of Supervised Learning

## Classification

When given labeled data (target) we need identify the mathematical service that best separates the labeled examples.

## Regression

Unlike _classification_, we use *regression* when the target is a range of possible values. When representing these data sets, _x_ denotes the features of the data set and _y_ denotes the target, or predicted value. This is then represented as:

> $\huge y\ =\ f(\ x\ )$

Here, the function *f()* is a trained data set and machine learning algorithm that takes certain features *x* and predicts *y* values. However, in machine learning *f()* is known as the *hypothesis* or *h()* which has stuck from the earlier days of machine learning. The machine learning algorithm *h()* can be based on a *linear* or more complicated *non-linear* types of algorithms.

### Linear Regression

Linear regression is just finding *y* using slope-intercept form where *b* is the y-intercept and *m* is the slope of the line.

> $\huge y\ =\ mx\ +\ b$

In machine learning, this is called our *hypothesis* function as shown below where theta *θ* can represent any number.

> $\huge h_{\theta }( x) =\theta _{0} \ +\ \theta _{1} x$

If we only have a single feature *x* then we call the algorithm *Univariate*, meaning, one variable and *Multivariate* refers to an algorithm that accepts multiple *x* values or features.

### Univariate Linear Regression

This is the simplest form of supervised machine learning. When we have a single *feature* which basically just chooses the best line that divides our data.

![Linear Regression](https://github.com/harperd/machine-learning/raw/master/images/linear-regression.png)

#### Cost Function: Choosing a Theta

In supervised learning we have a *training set* of data that is used to train our model *h(x)*. Our goal is to train our model to predict values for our function *h(x)* that are close to *y* (targets) from our training examples. In other words, given the *y* values in your training set (our known good answers), what is the closest *y* values we can predict using our machine learning linear regression algorithm *h(x)*? We want a good *fit* of the model where the difference between *h(x)* and our training set, *y* values, are minimized. 

If the illustration below, the values of *x* and *y* or *h(x)*, are plotted along the blue line. The distance, or model *fitness*, is measured between our training data points and the result of our linear function, *h(x)*.

![Measuring Fit of a Model](https://github.com/harperd/machine-learning/raw/master/images/model-fit.jpg)

We measure this _fit_ by using the *Cost Function* denoted as *J(θ<sub>0</sub>, θ<sub>1</sub>)* where *θ<sub>0</sub>* is a point on the *x* axis, *θ<sub>1</sub>* is a point on the *y* axis and the result of *J(θ<sub>0</sub>, θ<sub>1</sub>)* is *z*. This is also called the *Squared Error Function* which is the most commonly used for linear regression problems. Here, we want to get the results of our cost function *J(θ<sub>0</sub>, θ<sub>1</sub>)*, how fit our model is, as close to zero as possible.

In the _Cost Function_ below you will notice the result of our *hypothesis* function, $h_{\theta }\left( x^{( i)}\right)$, subtracted by our training set $y^{( i)}$. This is the heart of the function where want to minimize the distance between our hypothesis and training values. We do this for the entire set of data, $\sum\limits ^{m}_{i=1}$.

> $\huge J( \theta _{0} ,\ \theta _{1}) =\frac{1}{2m}\sum\limits ^{m}_{i=1}\left( h_{\theta }\left( x^{( i)}\right) -y^{( i)}\right)^{2}$

> **NOTE:** Multiplying the result by $\frac{1}{2m}$ is purely for aesthetics. See: https://datascience.stackexchange.com/questions/10188/why-do-cost-functions-use-the-square-error

> **NOTE:** You will notice the *Sum of Squared Errors* used in many other equations used to measure cost or optimization. This is the part of the equation that measures the difference between your predicted *y* and the *y* of your training set as denoted by (y<sub>1</sub> - y<sub>2</sub>)$^2$ Squaring the value just makes it easier to work with.

When you plot the values for *θ<sub>0</sub>*, *θ<sub>1</sub>* and *J(θ<sub>0</sub>, θ<sub>1</sub>)* (*x*, *y* and *z* respectively) you will get a 3-D plot similar to the below where the optimal theta values (*θ<sub>0</sub>* and *θ<sub>1</sub>*) are at the bottom of the bow.

![](https://github.com/harperd/machine-learning/raw/master/images/cost-function-plot.jpg)

> **See Also:** [mplot3d Toolkit](https://matplotlib.org/tutorials/toolkits/mplot3d.html)

The cost function can be more easily understood by using a 2-D *Contour Plot* where the minimal theta values would lie somewhere near the center circle.

![](https://github.com/harperd/machine-learning/raw/master/images/cost-function-contour-plot.jpg)

> **See Also:** [Contour Plot with Matplotlib](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.contour.html)

> **See Also:** [Contour Plot demo with Matplotlib](https://matplotlib.org/gallery/images_contours_and_fields/contour_demo.html)