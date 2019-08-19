# Classification

In *binary classification* there is only one $K$ output unit where output $y\in\{0,1\}$. In *multi-class classification* there are two or more $K$ output units that are $K$ dimentional where $y\in\R^K$. For example if there are two classes $A$ and $B$ then the results of the output units would be:

> Two classes where $K=\begin{bmatrix}A\\B\end{bmatrix}$
>
> Is class $A$ where $K^1=\begin{bmatrix}1\\0\end{bmatrix}$
>
> Is class $B$ where $K^2=\begin{bmatrix}0\\1\end{bmatrix}$

Where there are three or more output units for classification then *one-vs-all* will be used.

# Cost Function

The cost function for nuerual networks with regularization is shown below. Instead of having a single output unit we now have $K$ units. Where $\sum\limits^{K}_{k=1}$ is summing the normal logistic cost function over each of the $K$ output units and $y_k$ is the $i^{th}$ output such as $\begin{bmatrix}1\\0\end{bmatrix}$ (see *Classifiation*).

> $J(\Theta)=-\frac{1}{m}[\sum\limits^{m}_{i=1}\sum\limits^{K}_{k=1}(-y^{(i)}_k\cdot log(h_\Theta(x^{(i)}))_k + (1-y^{(i)}_k)\cdot log(1-h_\Theta(x^{(i)}))_k)]+\frac{\lambda}{2m}\sum\limits^{L}_{l=1}\sum\limits^{s_i}_{i=1}\sum\limits^{s_l+1}_{j=1}(\Theta^{(l)}_{ji})^2$