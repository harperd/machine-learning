# Gradient Descent: Automating the Cost Function

*Gradient Descent* is an algorithm used to find the optimal or minimized $J(\theta_{0}, \theta_{1})$. Sometimes it is referred to as *Batch Gradient Descent* because it is iterating over all training examples.

> $\theta_{j}\ := \theta_{j}-\alpha\frac{\partial}{\partial\theta_{j}}J(\theta_{0},\theta_{1})$

> **Note:** The function uses an *assignment* operator $:=$ instead of an *equality* operator $=$ which means that $\theta_{j}$ is not *equal* to the right hand side of the equation but *set* to the result of the equation.

Here, $\alpha$ (alpha) is the learning rate or step. The smaller the step the slower the algorithm will run. The larger, the faster. However, if alpha is too large you may not get to the lowest theta values since the algorithm may overshoot the minimum. 

![Gradient Descent Learning Rate](C:/Users/Ryan/repos/machine-learning/images/gradient-descent-alpha.png)

The derivative expression, $\frac{\partial}{\partial\theta_{j}}J(\theta_{0},\theta_{1})$, measures the rate of change. The *derivative* just measures the *slope* of a line (rise over run or y over x) that is *tangent* to or next to a point within of a graphed function. Here, $\partial$ (partial derivative) is a just a mathematical term which means that it the function works with multiple variables contrasted to $d$ (derivative) which is used with single variable functions. 

## Moving Toward Minimum

The derivative can be sloped in a positive direction on the $x,y$ axis (going from lower left to upper right) which denotes a *positive derivative* as shown in the illustration below. This derivative (positive, negative, or zero) tells the Gradient Descent algorithm which way to move (step next) with respect to the graphed function (shown as the green line in the graph below) in order to seek the minimum of $J(\theta_{0},\theta_{1})$.

![Tagent](C:/Users/Ryan/repos/machine-learning/images/derivative.png)

If the result of the derivative, $\frac{\partial}{\partial\theta_{j}}J(\theta_{0},\theta_{1})$, is a *positive number* then the equation looks like the below which moves the Gradient Decent algorithm to the *left* on the graph moving it closer to the minimum. Here $\theta_{1}$ is on the $x$ axis and the result would yield an $x$ value to the left of the starting $x$ value which moves closer to the minimum of our function $h_{\theta}(x)$.

> $\theta_{1} := \theta_{1} - \alpha(+\partial)$

As Gradient Descent approaches the minimum, the rate of change will become increasingly smaller. Hence, the algorithm will slow as it approaches the local minimum and ultimately stop changing once it has reached the minimum so there is not need to decrease the value of alpha.

## Simultaneous Compute

What *Gradient Descent* algorithm does is *simultaneously* compute values for $\theta_{0}$ and $\theta_{1}$. What is meant by *simultaneously* is represented in the pseudo code below where $\theta_{0}$ and $\theta_{1}$ are assigned new values at the same time. In other words, if $\theta_{0}$ was set ($\theta_{0} :=$ *temp0*) *before* temp1 was set (*temp1* $:= \theta_{1}-\alpha\frac{\partial}{\partial\theta_{1}}J(\theta_{0},\theta_{1})$) then it would affect the results of temp1 and yield incorrect results. We want to repeat this series of steps until we reach *convergence* or $\theta_{0}$ and $\theta_{1}$ are at their minimum.

> *repeat until convergence {*
>
> ​    $temp0 := \theta_{0}-\alpha\frac{\partial}{\partial\theta_{0}}J(\theta_{0},\theta_{1})$
>
> ​	$temp1 := \theta_{1}-\alpha\frac{\partial}{\partial\theta_{1}}J(\theta_{0},\theta_{1})$
>
> ​	$\theta_{0} := temp0$
>
> ​	$\theta_{1} := temp1$
>
> *}* 

Finding the partial derivatives of the expression $\alpha\frac{\partial}{\partial\theta_{1}}J(\theta_{0},\theta_{1})$ with respect to $\theta_{0}$ and $\theta_{1}$ yields the below where $m$ is the number of examples in our training set:

> *repeat until convergence {* 
>
> ​	$temp 0:= \theta_{0}-\alpha\frac{1}{m}\sum\limits ^{m}_{i=1}\left( h_{\theta }\left( x^{(i)}\right) -y^{( i)}\right)\cdot x_0^{(i)}$
>
> ​	$temp1 := \theta_{1}-\alpha\frac{1}{m}\sum\limits ^{m}_{i=1}\left( h_{\theta }\left( x^{(i)}\right) -y^{( i)}\right)\cdot x_i^{(i)}$
>
> ​	$\theta_{0} := temp0$
>
> ​	$\theta_{1} := temp1$
>
> *}* 

## Hypothesis Calculation Using Matrices

When applying a large set of features to a hypothesis function it is more computationally efficient to use matrices instead of a looping construct to compute the predictions for each feature. For example, in *univariate* regression with 3 features, using matrices, a hypothesis can be computed as below.

If  our values for $\theta _{0}$ and $\theta _{1}$ are $-40$ and $0.25$ respectively then our hypothesis would look like:

> $h_{\theta }( x) =-40 + 0.25x$

Given a set of features (5, 2 and 4) we can construct a matrix with the first column only containing the value $1$, which is called *bias*, since it is not multiplied by a feature:

> $\begin{bmatrix}1&5\\1&2\\1&4\end{bmatrix}$

Using matrix multiplication we can then apply each feature in our matrix to our hypotheses function:

> $\begin{bmatrix}1&5\\1&2\\1&4\end{bmatrix}\cdot\begin{bmatrix}-40\\0.25\end{bmatrix}=\begin{bmatrix}(1\cdot-40)+(5\cdot0.25)\\(1\cdot-40)+(2\cdot0.25)\\(1\cdot-40)+(4\cdot0.25)\end{bmatrix}=\begin{bmatrix}-38.75\\-39.50\\-40\end{bmatrix}$

## Competing Hypothesis

Matrix multiplication can be use to execute multiple hypothesis functions at the same time with a set of features in an efficient manner.

> $h_{\theta }( x) =-40 + 0.25x$
>
> $h_{\theta }( x) =200 + 0.1x$
>
> $h_{\theta }( x) =-150 + 0.4x$

> $\begin{bmatrix}1&2104\\1&1416\\1&1534\\1&852\end{bmatrix}\cdot\begin{bmatrix}-40&200&-150\\0.25&0.1&0.4\end{bmatrix}=\begin{bmatrix}486&410&692\\314&342&416\\344&353&464\end{bmatrix}$