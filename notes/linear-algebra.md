# Linear Algebra for Machine Learning

## Matrices

A matrix is simply a rectangular array of numbers and the *dimension* of a matrix is written as *rows x columns*. For the example below, the dimension of the matrix would be *2x3*. Often times you will see the matrix dimensionality depicted as $\R^{2x3}$ where $\R$ simply denotes a *real number*.

> $\begin{bmatrix}1,2,3\\4,5,6 \end{bmatrix}$

To reference a specific element in a matrix we would specify the row and column. For the example below, matrix $A$, $A_{1,2}$ would give us the number in the $1^{st}$ row and $2^{nd}$ column which would be the number $2$.

> $A = \begin{bmatrix}10,24,35\\34,15,76 \end{bmatrix}$   *where* $A_{1,2} = 24$

## Vectors

A *vector* is simply a matrix with a single column. We would express the dimensionality of the below as simply a three dimensional vector, or $\R^3$ where $y_2 = 21$.

> $y =\begin{bmatrix}18\\21\\33\end{bmatrix}$

The indexes of matrices can be *1-indexed* or *0-indexed*, meaning, the first element (row or column) starts at either *1* or *0*. Matrices are also, by convention, referenced with *uppercase* letters and numbers and vectors with *lowercase* letters.

## Matrix Addition & Subtraction

When adding or subtracting one matrix from another we simply add or substract each number in each column with it's corresponding number in the other matrix. Also, both matrices must be of the same dimension. For example:

> $\begin{bmatrix}1,3,5\\7,9,2\\3,4,1\end{bmatrix} + \begin{bmatrix}3,2,0\\3,1,4\\6,9,8\end{bmatrix} = \begin{bmatrix}4,5,5\\10,10,6\\9,13,9\end{bmatrix}$

## Scalar Multiplication and Division

> $2$ x$\begin{bmatrix}2,3,5\\7,9,2\\3,4,1\end{bmatrix}=\begin{bmatrix}4,6,10\\14,18,4\\6,4,2\end{bmatrix}$

## Identity Matrix

Just as the number 1 in multiplication is the identity property:

> $3\cdot1=1\cdot3=3$

Matrices also have an identity which has all zeros and number 1 in the diagonal. These matrices are denoted by the capital letter I. For example, the below is an identity matrix for a 2x2 matrix:

> $I_{2x2} = \begin{bmatrix}1&0\\0&1\end{bmatrix}$

When we apply this to another 2x2 matrix the result is the same as the original matrix:

> If $A=\begin{bmatrix}3&4\\2&16\end{bmatrix}$
>
> And $I=\begin{bmatrix}1&0\\0&1\end{bmatrix}$
>
> Then $A(I) = A$
>
> $\begin{bmatrix}3&4\\2&16\end{bmatrix}\cdot\begin{bmatrix}1&0\\0&1\end{bmatrix}=\begin{bmatrix}3&4\\2&16\end{bmatrix}$

## Special Matrix Operations

### Matrix Inverse

Just as many numbers have an inverse such as:

> $3(3^{-1}) = 1$ or $34(34^{-1}) = 1$

Matrices can also have an inverse:

> $A(A^{-1}) = A^{-1}(A) = I$

For example:

> $\begin{bmatrix}3&4\\2&16\end{bmatrix}\cdot\begin{bmatrix}0.4&-0.1\\-0.05&0.075\end{bmatrix}=\begin{bmatrix}1&0\\0&1\end{bmatrix}$

However, some numbers, such as 0 do not have an inverse:

> $0(0^{-1}) = undefined$

In the same way the inverse of a matrix with all zeros is undefined. Such matrices are called *singular* or *degenerate*.

> $\begin{bmatrix}0&0\\0&0\end{bmatrix}$

### Matrix Transposition

This is simply converting matrix rows to columns, for example:

> $A=\begin{bmatrix}3&4\\2&16\end{bmatrix}$

Transposed, it would be:

> $A^T=\begin{bmatrix}3&2\\4&16\end{bmatrix}$

Therefore:

> $A_{mxn} = A^T_{nxm}$

For example:

> $A_{2,1} = A^T_{1,2} = 4$