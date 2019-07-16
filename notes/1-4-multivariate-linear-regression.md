# Multivariate Linear Regression

## Hypothesis

Below is our *hypothesis* for *univariate* linear regression with a single feature value denoted by the variable $x$.

> $h_{\theta }( x) =\theta _{0} \ +\ \theta _{1} x$

For multiple features we would represent them in our equation in the form of $x_1, x_2, x_3$ all the way to $x_n$. For example, the below would be three features of $x_1$ to $x_3$.

> Features: *stock price* = $x_1$, *date sold* = $x_2$, *sale price* = $x_3$

To denote a single value in example $i$, feature $j$ we would write:

> $\large x^{(i)}_j$

Therefore to get the 5th feature in the 3rd example we would write it as:

> $\large x^{(3)}_5$

To support $n$ features the hypothesis function has to change to the following.

> $h_{\theta }( x) =\theta _{0} \ +\ \theta _1x_1+ \theta _2x_2+ \theta _3x_3+\cdot\cdot\cdot+ \theta _nx_n$

This can be written using vectors. Note, however, that $x^{(i)}_0$ will be a constant of 1. This can be thought of as adding an additional $0$ feature and our vectors are now *0-indexed*. The below is an example with $3$ examples and $3$+ features in each example:

> $\vec X=\begin{bmatrix}1&x^{(1)}_1&x^{(1)}_2&x^{(1)}_3&x^{(1)}_n\\1&x^{(2)}_1&x^{(2)}_2&x^{(2)}_3&x^{(2)}_n\\1&x^{(3)}_1&x^{(3)}_2&x^{(3)}_3&x^{(3)}_n\end{bmatrix}, \vec\theta=\begin{bmatrix}\theta_0\\\theta_1\\\theta_2\\\theta_3\\\theta_n\end{bmatrix}$

So, our hypothesis function can be written as the below where $\theta _0x_0 = 1\cdot1=1$

> $h_{\theta }( x) =\theta _0x_0 +\theta _1x_1+ \theta _2x_2+ \theta _3x_3+\cdot\cdot\cdot+ \theta _nx_n$

In order to multiply the two vectors, $\theta$ and $X$, we need to *transpose* the theta vector which will then be labeled as $\theta^T$ which is now an $(n$ x $1)$ x $1$ matrix or *row vector*.

> $\theta^T=\begin{bmatrix}\theta_0&\theta_1&\theta_2&\theta_3&\theta_n\end{bmatrix}$

Now, the hypothesis function can be re-written as simply:

> $h_{\theta }( x) =\theta^TX$

The function below visually illustrates our new hypothesis function.

> $h_{\theta }( x) =\begin{bmatrix}\theta_0&\theta_1&\theta_2&\theta_3&\theta_n\end{bmatrix}\cdot\begin{bmatrix}1&x^{(1)}_1&x^{(1)}_2&x^{(1)}_3&x^{(1)}_n\\1&x^{(2)}_1&x^{(2)}_2&x^{(2)}_3&x^{(2)}_n\\1&x^{(3)}_1&x^{(3)}_2&x^{(3)}_3&x^{(3)}_n\end{bmatrix}$

## Gradient Descent

Our cost function for Gradient Descent is slightly different for multivariate linear regression. Here we are passing in not one, but multiple features, that range from $\theta_0$ to $\theta_n$.

> $J( \theta _{0} ,\ \theta _{1},\cdot\cdot\cdot,\theta_n) =\frac{1}{2m}\sum\limits ^{m}_{i=1}\left( h_{\theta }\left( x^{( i)}\right) -y^{( i)}\right)^{2}$

For simplicity we can just write the function as $J(\theta)$.

> $J(\theta) =\frac{1}{2m}\sum\limits ^{m}_{i=1}\left( h_{\theta }\left( x^{( i)}\right) -y^{( i)}\right)^{2}$

The Gradient Descent algorithm now looks like the following:

>*repeat until convergence {* 
>
>​    $\theta_j:=\theta_j-\alpha\frac{\partial}{\partial\theta_j}J(\theta)$
>
>*} (Simultaneously updated for every $j=0$, . . ., $n$)*

Finding the partial derivative of the expression $\alpha\frac{\partial}{\partial\theta_{1}}J(\theta)$ yields the below:

>*repeat until convergence {* 
>
>​    $\theta_j:=\theta_j-\alpha\frac{1}{m}\sum\limits ^{m}_{i=1}\left( h_{\theta }\left( x^{(i)}\right) -y^{( i)}\right)x^{(i)}_j$
>
>*} (Simultaneously updated for every $j=0$, . . ., $n$)*
