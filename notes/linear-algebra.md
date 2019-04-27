# Linear Algebra for Machine Learning

## Matrices

A matrix is simply a rectangular array of numbers and the *dimension* of a matrix is written as *rows x columns*. For the example below, the dimension of the matrix would be *2x3*. Often times you will see the matrix dimensionality depicted as $\R^{2x3}$ where $\R$ simply denotes a *real number*.

> $\begin{bmatrix}1,2,3\\4,5,6 \end{bmatrix}$

To reference a specific element in a matrix we would specify the row and column. For the example below, matrix *Y*, $Y_{1,2}$ would give us the number in the $1^{st}$ row and $2^{nd}$ column which would be the number $2$.

> $Y = \begin{bmatrix}10,24,35\\34,15,76 \end{bmatrix}$   *where* $Y_{1,2} = 24$

## Vectors

A *vector* is simply a matrix with a single column. We would express the dimensionality of the below as simply a three dimensional vector, or $\R^3$ where $y_2 = 21$.

> $y =\begin{bmatrix}18\\21\\33\end{bmatrix}$

The indexes of matrices can be *1-indexed* or *0-indexed*, meaning, the first element (row or column) starts at either *1* or *0*. Matrices are also, by convention, referenced with *uppercase* letters and numbers and vectors with *lowercase* letters.

## Matrix Addition & Subtraction

When adding or subtracting one matrix from another we simply add or substract each number in each column with it's corresponding number in the other matrix. Also, both matrices must be of the same dimension. For example:

> $\begin{bmatrix}1,3,5\\7,9,2\\3,4,1\end{bmatrix} + \begin{bmatrix}3,2,0\\3,1,4\\6,9,8\end{bmatrix} = \begin{bmatrix}4,5,5\\10,10,6\\9,13,9\end{bmatrix}$

## Scalar Multiplication and Division

> $2$ x$\begin{bmatrix}2,3,5\\7,9,2\\3,4,1\end{bmatrix}=\begin{bmatrix}4,6,10\\14,18,4\\6,4,2\end{bmatrix}$