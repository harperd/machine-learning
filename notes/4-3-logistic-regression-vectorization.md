# Logistic Regression: Vectorizing Logistic Regression

The *Sigmoid Function* of $\frac{1}{1+e^{-z}}$ is used when computing the hypothesis for logistic regression which means that the normal vectorized compute of $\theta^TX$ is not going to work in this case since the *Sigmoid Function* would not be applied. Using victor math this can be achieved using the following:

> $\vec Z=w^TX+\vec b$

Where

> $X=\begin{bmatrix}x^{(1)}_1&x^{(1)}_2&x^{(1)}_3&x^{(1)}_n\\x^{(2)}_1&x^{(2)}_2&x^{(2)}_3&x^{(2)}_n\\x^{(3)}_1&x^{(3)}_2&x^{(3)}_3&x^{(3)}_n\end{bmatrix}$
>
> $w^T=\begin{bmatrix}\theta_1&\theta_2&\theta_3&\theta_n\end{bmatrix}$
>
> $\vec b=\begin{bmatrix}\theta_0&\theta_0&\theta_0&...\end{bmatrix}$

From there we can take $\vec Z$ and pass to our Sigmoid Function:

> $h_\theta(x) = S(\vec Z)$