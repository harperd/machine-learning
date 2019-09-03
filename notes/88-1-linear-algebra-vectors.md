# Vectors

A *vector* is defended as a line (or arrow) on the $xy$ coordinate plane hat has both direction and length. For the most part vectors, in mathematics, will almost always be rooted at the origin $(0,0)$. Vectors are written simply a matrix with a single column (an $n$ x $1$ matrix). We would express the dimensionality of the below as simply a three dimensional vector, or $\R^3$ where $y_2 = 21$.

> $\vec y =\begin{bmatrix}18\\21\\33\end{bmatrix}$

Below is a visual representation of a vector:

![https://www.youtube.com/watch?v=fNk_zzaMoSs&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab](C:/Users/Ryan/repos/machine-learning/images/linear-algebra/vector.png)

Most linear algebra topics tend to revolve around *adding* vectors and *scaling* vectors.

## Adding Vectors

When adding vectors you take the second vector and move the tail to the head of first vector. The distance between the origin and the head of the second vector is the sum. The illustration below shows visually how adding vectors works.  The distance of $\vec V$ and $\vec W$ is the same total distance as $\vec V + \vec W$.

![https://www.youtube.com/watch?v=fNk_zzaMoSs&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab](C:/Users/Ryan/repos/machine-learning/images/linear-algebra/vector-add.png)

## Scaling Vectors

*Scaling* a vector means changing it's size by multiplying by a *scalar*. For example take a vector and multiply it by a *scalar* of $2$ as shown below.

![https://www.youtube.com/watch?v=fNk_zzaMoSs&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab](C:/Users/Ryan/repos/machine-learning/images/linear-algebra/vector-scale.png)

> $\vec v=\begin{bmatrix}3\\1\end{bmatrix}$
>
> $2\vec v=2\cdot\begin{bmatrix}3\\1\end{bmatrix}=\begin{bmatrix}6\\2\end{bmatrix}$

## Basis Vectors

The *basis* of a vector space is a set of *linearly independent* vectors that *span* the full space. The following sections outline this concept in more detail.

There are different types of basis vectors. Basis vectors (unit vectors) can have a length of $1$ in a normed vector space as shown below. In this case, these two important vectors are $\hat{i}$ and $\hat{j}$, each with a length of $1$ (In a 3D space we would also use $\hat{z}$). These are call *basis vectors* because they are the *basis of a coordinate system*. By *basis* we mean, when describing vectors numerically, it directly depends on which type of basis vectors you are using. In this case, $\hat{i}$ and $\hat{j}$  which each have a length of $1$. From these basis vectors we can add and scale them.

![](C:/Users/Ryan/repos/machine-learning/images/linear-algebra/i_hat_j_hat.png)

> **NOTE:** The hat symbol $\hat{}$ is called a *circumflex* but pronounced "hat"
>
> **NOTE:**  It is also worth noting that $\hat{i}$, $\hat{j}$ and $\hat{z}$ represent vectors where $x$, $y$ and $z$ represents *points* and *axes*.

When we think of a vector like the below:

> $\vec v=\begin{bmatrix}3\\1\end{bmatrix}$

With basis vectors, we think of it as *scaling*  $\hat{i}$ and $\hat{j}$ by $3$ and $1$ respectively:

> $\vec v=\begin{bmatrix}3\hat{i}\\1\hat{j}\end{bmatrix}$

### Linear Combinations

Any time you add *and* scale two vectors, it is called a *linear combination*. The below shows a linear combination where $a$ and $b$ are <u>scalars</u> that scale the two vectors $\vec v$ and $\vec w$.

> $a\vec v + b\vec w$

For example:

> $0.88\vec v + 1.30\vec w$

![](C:/Users/Ryan/repos/machine-learning/images/linear-algebra/linear_combination.png)

For a linear combination with three vectors we simply add the third vectors and scalar:

> $a\vec v + b\vec w + c\vec u$

### Span

The *span* of any two vectors is the set of all of their linear combinations where scalars $a$ and $b$ can vary. If we were to stretch and pull the resulting vector (magenta in this case) to exactly every point possible for their linear combination in 2 dimensions the *span* would be every possible point on the 2D plane. In 3D space, if we were to stretch and pull the resulting vector to exactly every point possible for their linear combination the *span* would resemble a flat sheet.

![](C:/Users/Ryan/repos/machine-learning/images/linear-algebra/vector_span_3d.png)

For a linear combination with three vectors, we would have access to every 3 dimensional point just as with a linear combat ion of 2 vectors gives us access to every point on the 2D plane. Here, the tip of the third vector "moves the sheet" in 3 dimensions giving access to all possible points in the 3D space.

![](C:/Users/Ryan/repos/machine-learning/images/linear-algebra/vector_span_3d2.png)

### Linear Dependance and Independance

If the vectors are inline as below, their *span* would just be a straight line. In this case, we would say the two vectors are *linearly dependent* since second vector does not really change the span of the linear combination. The more official definition of linear dependence would be if one or more vectors can be definded as a linear combination of the other vectors.

![](C:/Users/Ryan/repos/machine-learning/images/linear-algebra/inline_vectors.png)

Therefore, we could say that one of the vectors can be expressed as a linear combination of the other two vectors since it lies in the same span as the other two vectors. Here, vector $\vec u$ is said to be *linearly dependent* on the linear combination of the other two vectors  $\vec v$ and $\vec w$:

> $\vec u=a\vec v + b\vec w$

If the second vector does add another dimension to the span they are said to be *linearly independent*:

> $\vec u\neq a\vec v + b\vec w$

In mathematics it is generally noted that vectors $\vec v$, $\vec w$ and $\vec u$ are said to be l*inearly independent* if the only solution to the linear combintation is a zero length vector $\vec 0$ such that:

> $a\vec v + b\vec w + c\vec u=\vec 0$