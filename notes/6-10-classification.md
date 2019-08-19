# Classification

In *binary classification* there is only one $K$ output unit where output $y\in\{0,1\}$. In *multi-class classification* there are two or more $K$ output units that are $K$ dimentional where $y\in\R^K$. For example if there are two classes $A$ and $B$ then the results of the output units would be:

> Two classes where $K=\begin{bmatrix}A\\B\end{bmatrix}$
>
> Is class $A$ where $K^1=\begin{bmatrix}1\\0\end{bmatrix}$
>
> Is class $B$ where $K^2=\begin{bmatrix}0\\1\end{bmatrix}$

Where there are three or more output units for classification then *one-vs-all* will be used.

# Cost Function

The cost function for nuerual networks with regularization is shown below. Instead of having a single output unit we now have $K$ units where $h_\Theta(x)_i$ refers to the $i^{th}$ value in the output vector. $\sum\limits^{K}_{k=1}$ is summing the normal logistic cost function over each of the $K$ output units and $y_k$ is the $i^{th}$ output such as $\begin{bmatrix}1\\0\end{bmatrix}$ (see *Classifiation*). Including the bias units in the cost is not a big deal but you generally want to omit them hence below we are not regularizing the bias units so our limits will start at $1$.

> $J(\Theta)=-\frac{1}{m}[\sum\limits^{m}_{i=1}\sum\limits^{K}_{k=1}(-y^{(i)}_k\cdot log(h_\Theta(x^{(i)}))_k + (1-y^{(i)}_k)\cdot log(1-h_\Theta(x^{(i)}))_k)]+\frac{\lambda}{2m}\sum\limits^{L-1}_{l=1}\sum\limits^{s_i}_{i=1}\sum\limits^{s_l+1}_{j=1}(\Theta^{(l)}_{ji})^2$

For the regularization term (also called a *Weight Decay*) it is doing the following:

1. For each layer: $\sum\limits^{L-1}_{l=1}$
2. For each weight in that layer: $\sum\limits^{s_i}_{i=1}$ and $\sum\limits^{s_l+1}_{j=1}$ where $s_i$ and $s_i+1$ are the matrix dimentions at that layer
3. Square the weight at $ji$: $(\Theta^{(l)}_{ji})^2$