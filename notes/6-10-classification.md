# Classification

In *binary classification* there is only one $K$ output unit where output $y\in\{0,1\}$. In *multi-class classification* there are two or more $K$ output units that are $K$ dimentional where $y\in\R^K$. For example if there are two classes $A$ and $B$ then the results of the output units would be:

> Two classes where $K=\begin{bmatrix}A\\B\end{bmatrix}$
>
> Is class $A$ where $K^1=\begin{bmatrix}1\\0\end{bmatrix}$
>
> Is class $B$ where $K^2=\begin{bmatrix}0\\1\end{bmatrix}$

Where there are three or more output units for classification then *one-vs-all* will be used.