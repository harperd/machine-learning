# Types of Supervised Learning

## Classification

When given labeled data (target) we need identify the mathematical service that best separates the labeled examples.

## Regression

Unlike _classification_, we use *regression* when the target is a range of possible values. When representing these data sets, _x_ denotes the features of the data set and _y_ denotes the target, or predicted value. This is then represented as:

> $\large y\ =\ f(\ x\ )$

Here, the function $f()$ is a trained data set and machine learning algorithm that takes certain features $x$ and predicts $y$ values. However, in machine learning $f()$ is known as the *hypothesis* or $h()$ which has stuck from the earlier days of machine learning. The machine learning algorithm $h()$ can be based on a *linear* or more complicated *non-linear* types of algorithms.

### Linear Regression

Linear regression is just finding $y$ using slope-intercept form where *b* is the y-intercept and *m* is the slope of the line.

> $\large y\ =\ mx\ +\ b$

In machine learning, this is called our *hypothesis* function as shown below where theta *θ* can represent any two numbers. We just have to figure out what those two numbers are.

> $\large h_{\theta }( x) =\theta _{0} \ +\ \theta _{1} x$

If we only have a single feature $x$ then we call the algorithm *Univariate*, meaning, one variable and *Multivariate* refers to an algorithm that accepts multiple $x$ values or features.

### Univariate Linear Regression

This is the simplest form of supervised machine learning. When we have a single *feature* which basically just chooses the best line that divides our data.

![Linear Regression](https://github.com/harperd/machine-learning/raw/master/images/linear-regression.png)

#### Cost Function: Choosing Theta

In supervised learning we have a *training set* of data that is used to train our model $h_{\theta }( x) =\theta _{0} \ +\ \theta _{1} x$ where $x$ is a feature value from our training set and our predicted $y$ value is the result of our function $h_{\theta }( x)$. Our predicted $y$ value is then compared against the $y$ values from our training set (the correct predictions) to measure how accurate, or *fit*, our model is. Again, we need to find the best values for $\theta _{0}$ and $\theta _{1}$ to optimize our model. We want a good *fit* of the model where the difference between *$h_{\theta }( x)$* and our training set, $y$ values, are minimized. 

In the illustration below, our hypothesis function $h_{\theta }( x)$ is plotted along the blue line. The distance, or model *fitness*, is measured between our training data points and the result of our linear function, *$h_{\theta }( x)$*.

![Measuring Fit of a Model](https://github.com/harperd/machine-learning/raw/master/images/model-fit.jpg)

We can choose good theta values by using the *Cost Function* denoted as $J(\theta_{0}, \theta_{1})$ where  $\theta_{0}$ is a point on the $x$ axis, $\theta_{1}$ is a point on the $y$ axis and the result of $J(\theta_{0}, \theta_{1})$ is *z*. This is also called the *Squared Error Function* which is the most commonly used for linear regression problems. Here, we want to get the results of our cost function , how $J(\theta_{0}, \theta_{1})$ fit our model is, as close to zero as possible by trying different values for $\theta _{0}$ and $\theta _{1}$.

> $\large J( \theta _{0} ,\ \theta _{1}) =\frac{1}{2m}\sum\limits ^{m}_{i=1}\left( h_{\theta }\left( x^{( i)}\right) -y^{( i)}\right)^{2}$

> **NOTE:** Multiplying the result by $\frac{1}{2m}$ is purely for aesthetics. See: https://datascience.stackexchange.com/questions/10188/why-do-cost-functions-use-the-square-error

> **NOTE:** You will notice the *Sum of Squared Errors* used in many other equations used to measure cost or optimization. This is the part of the equation that measures the difference between your predicted $y$ and the $y$ of your training set as denoted by $(y_{1} - y_{2})^2$ Squaring the value just makes it easier to work with.

In the _Cost Function_ above you will notice the result of our *hypothesis* function, $h_{\theta }\left( x^{( i)}\right)$, subtracted by our training set $y^{( i)}$. This is the heart of the cost function where want to minimize the distance between our hypothesis and training values. We do this for the entire set of data, $\sum\limits ^{m}_{i=1}$.

When you plot the values for $\theta_{0}$, $\theta_{1}$ and $J(\theta_{0}, \theta_{1})$ (*x*, $y$ and *z* respectively) you will get a 3-D plot similar to the below where the optimal values for $\theta_{0}$ and $\theta_{1}$ are at the bottom of the bow.

![](https://github.com/harperd/machine-learning/raw/master/images/cost-function-plot1.jpg)

![](https://github.com/harperd/machine-learning/raw/master/images/cost-function-plot2.jpg)

> **See Also:** [mplot3d Toolkit](https://matplotlib.org/tutorials/toolkits/mplot3d.html)

The cost function can be more easily understood by using a 2-D *Contour Plot* where the minimal theta values would lie somewhere near the center circle.

![](https://github.com/harperd/machine-learning/raw/master/images/cost-function-contour-plot.jpg)

> **See Also:** [Contour Plot with Matplotlib](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.contour.html)

> **See Also:** [Contour Plot demo with Matplotlib](https://matplotlib.org/gallery/images_contours_and_fields/contour_demo.html)