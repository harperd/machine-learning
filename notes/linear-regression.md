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

In machine learning, this is called our *hypothesis* function as shown below where theta $\theta$ can represent any two numbers. We just have to figure out what those two numbers are that allow the function to best intersect our data or features.

> $\large h_{\theta }( x) =\theta _{0} \ +\ \theta _{1} x$

If we only have a single feature $x$ then we call the algorithm *Univariate*, meaning, one variable and *Multivariate* refers to an algorithm that accepts multiple $x$ values or features.

### Univariate Linear Regression

This is the simplest form of supervised machine learning. When we have a single *feature* which basically just chooses the best line that divides our data.

![Linear Regression](https://github.com/harperd/machine-learning/raw/master/images/linear-regression.png)

#### Cost Function: Choosing Theta

In supervised learning we have a *training set* of data that is used to train our model $h_{\theta }( x) =\theta _{0} \ +\ \theta _{1} x$ where $x$ is a feature value from our training set and our predicted $y$ value is the result of our function $h_{\theta }( x)$. Our predicted $y$ value is then compared against the $y$ values from our training set (the correct predictions) to measure how accurate, or *fit*, our model is. Again, we need to find the best values for $\theta _{0}$ and $\theta _{1}$ to optimize our model. We want a good *fit* of the model where the difference between *$h_{\theta }( x)$* and our training set, $y$ values, are minimized. 

In the illustration below, our hypothesis function $h_{\theta }( x)$ is plotted along the blue line. The distance, or model *fitness*, is measured between our training data points and the result of our linear function, *$h_{\theta }( x)$*.

![Measuring Fit of a Model](https://github.com/harperd/machine-learning/raw/master/images/model-fit.jpg)

We can choose good theta values by using the *Cost Function* denoted as $J(\theta_{0}, \theta_{1})$ where  $\theta_{0}$, and $\theta_{1}$ points on the $x$,$y$ axis and $J(\theta_{0}, \theta_{1})$ is *z*. This is also called the *Squared Error Function* which is the most commonly used for linear regression problems. Here, we want to get the results of our cost function as close to zero as possible by trying different values for $\theta _{0}$ and $\theta _{1}$.

> $\large J( \theta _{0} ,\ \theta _{1}) =\frac{1}{2m}\sum\limits ^{m}_{i=1}\left( h_{\theta }\left( x^{( i)}\right) -y^{( i)}\right)^{2}$

> **Note:** Multiplying the result by $\frac{1}{2m}$ is purely for aesthetics. See: https://datascience.stackexchange.com/questions/10188/why-do-cost-functions-use-the-square-error

> **Note:** You will notice the *Sum of Squared Errors* used in many other equations used to measure cost or optimization. This is the part of the equation that measures the difference between your predicted $y$ and the $y$ of your training set as denoted by $(y_{1} - y_{2})^2$ Squaring the value just makes it easier to work with.

In the _Cost Function_ above you will notice the result of our *hypothesis* function, $h_{\theta }\left( x^{( i)}\right)$, subtracted by our training set $y^{( i)}$. This is the heart of the cost function where want to minimize the distance between our hypothesis and training values. We do this for the entire set of data, $\sum\limits ^{m}_{i=1}$.

When you plot the values for $\theta_{0}$, $\theta_{1}$ and $J(\theta_{0}, \theta_{1})$ ($x$, $y$ and *z* respectively) you will get a 3-D plot similar to the below where the optimal values for $\theta_{0}$ and $\theta_{1}$ are at the lowest point on the graph.

![Cost Function 3D Plot](https://github.com/harperd/machine-learning/raw/master/images/cost-function-plot1.jpg)

![Cost Function 3D Plot](https://github.com/harperd/machine-learning/raw/master/images/cost-function-plot2.jpg)

> **See Also:** [mplot3d Toolkit](https://matplotlib.org/tutorials/toolkits/mplot3d.html)

The cost function can be more easily understood by using a 2-D *Contour Plot* where the minimal theta values would lie somewhere near the center circle.

![Cost Function Contour Plot](https://github.com/harperd/machine-learning/raw/master/images/cost-function-contour-plot.jpg)

> **See Also:** [Contour Plot with Matplotlib](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.contour.html)

> **See Also:** [Contour Plot demo with Matplotlib](https://matplotlib.org/gallery/images_contours_and_fields/contour_demo.html)

#### Gradient Descent: Automate Finding Theta Values

*Gradient Descent* is an algorithm used to find the optimal or minimized $J(\theta_{0}, \theta_{1})$.

> $\large\theta_{j}\ := \theta_{j}-\alpha\frac{\partial}{\partial\theta_{j}}j(\theta_{0},\theta_{1})$

> **Note:** The function uses an *assignment* operator $:=$ instead of an *equality* operator $=$ which means that $\theta_{j}$ is not *equal* to the right hand side of the equation but *set* to the result of the equation.

Here, $\alpha$ (alpha) is the learning rate or step. The smaller the step the slower the algorithm will run. The larger, the faster. However, if alpha is too large you may not get to the lowest theta values. $\frac{\partial}{\partial\theta_{j}}j(\theta_{0},\theta_{1})$ is a derivative or rate of change (division). A *derivative* just measures the *slope* of a line (rise over run or x over y) that is *tangent* to or next to a point within of a graphed function. Here, $\partial$ (partial derivative) is a just a mathematical term which means that it the function works with multiple variables contrasted to $d$ (derivative) which is used with single variable functions. The derivative can be sloped in a positive direction on the $x,y$ axis (going from lower left to upper right) which denotes a *positive derivative* as shown in the illustration below. This derivative (positive, negative, or zero) tells the Gradient Descent algorithm which way to move (step next) with respect to the graphed function (shown as the green line in the graph below) in order to seek the minimum of $J(\theta_{0},\theta_{1})$.

![](https://github.com/harperd/machine-learning/raw/master/images/derivative.png)

If the result of the derivative, $\frac{\partial}{\partial\theta_{j}}j(\theta_{0},\theta_{1})$, is a *positive number* then the equation looks like the below which moves the Gradient Decent algorithm to the *left* on the graph moving it closer to the minimum. Here $\theta_{1}$ is on the $x$ axis and the result would yield an $x$ value to the left of the starting $x$ value which moves closer to the minimum of our function $h_{\theta}(x)$.

> $\theta_{1} := \theta_{1} - \alpha(+\partial)$

What *Gradient Descent* algorithm does is *simultaneously* compute values for $\theta_{0}$ and $\theta_{1}$. What is meant by *simultaneously* is represented in the pseudo code below where $\theta_{0}$ and $\theta_{1}$ are assigned new values at the same time. In other words, if $\theta_{0}$ was set ($\theta_{0} :=$ *temp0*) *before* temp1 was set (*temp1* $:= \theta_{1}-\alpha\frac{\partial}{\partial\theta_{1}}j(\theta_{0},\theta_{1})$) then it would affect the results of temp1 and yield incorrect results.

>  *repeat until convergence {*
>
> ​	*temp0* $:= \theta_{0}-\alpha\frac{\partial}{\partial\theta_{0}}j(\theta_{0},\theta_{1})$
>
> ​	*temp1* $:= \theta_{1}-\alpha\frac{\partial}{\partial\theta_{1}}j(\theta_{0},\theta_{1})$
>
> ​	$\theta_{0} :=$ *temp0*
>
> ​	$\theta_{1} :=$ *temp1*
>
> *}*

We want to repeat this series of steps until we reach *convergence* or $\theta_{0}$ and $\theta_{1}$ are at their minimum.