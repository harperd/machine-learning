# Pseudo Inverse: Gradient Descent Alternative

If you are familiar with the concept of **Pseudo Inverse** in Linear Algebra, the parameters *θ* can be obtained by this formula:

> $\theta=(X^TX)^{-1}Xy$

In Multivariate Linear Regression, the formula is the same as above. But, what if the Normal Equation is non-invertible? Then consider deleting redundant features or using the regularization.