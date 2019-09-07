# Parameter Initialization

One of the first things that you will want do is to initialize the weight matrices and bias vectors. Their initial values for the weight matrices should not be zero since the cost reduction gradients would be the same value for each iteration (all weights associated with a particular parameters will be the same value) causing the learning algorithm to not learn. This basically makes you neural network no better than a linear model. This is also called the **problem of symmetric weights**. So, it's best to randomly choose the initial weight values that are between $-1$ and $1$ and multiply them by a small scalar such as $0.01$ to make the activation units active and be on the regions where activation functions' derivatives are not close to zero.

Mathematically, we want to initialize each $\Theta^{(l)}_{ij}$ weight to a random value in $\large[-\epsilon,\epsilon]$:

> $\large-\epsilon\le\Theta^{(l)}_{ij}\le\epsilon$

However, when initializing weights randomly, you can run into two main issues (with deep networks): The problem of *vanishing gradients* or *exploding gradients*. During back propagation the gradients get smaller and smaller it approaches the global minimum as it should. However, you can run into the *problem of vanishing gradients* especially with *sigmoid* or *tanh* activation functions. This will prevent weights from changing their value. **ReLU overcomes the problem of vanishing gradients since the gradient is $0$ for numbers $\le0$ and $1$ for positive numbers.**

When weights are large and $\gt0$ and small activation functions like *sigmoid* are used, the change in cost $J(\Theta)$ will be quite large and result in *exploding gradients* during back propagation. **Exploding gradients may result in oscillating around the minima or even overshooting the optimum again and again causing the model to not learn.** Exploding gradients can get so large they **can also cause overflows and result in NaN**.

## Best Practices to Avoid Vanishing and Exploding Gradients

Consider using *ReLU* or *Leaky ReLU* for activation functions where you have deep networks prone to vanishing gradients. Leaky ReLU overcomes vanishing gradients entirely by supplying a small, non-zero gradient, $\alpha$ value (usually 0.01) for $z$ values $\le0$.

For deep networks using heuristics (logic) to initialize wieghts can help mitigate gradient issues. We create out weight values based on the types of non-linear activation functions that are used.

For ReLU we multiply our randomly generated weights by:

> $\large\sqrt{\frac{2}{size^{[l-1]}}}$

Implementation in Python:

```python
W = np.random.randn(size_l, size_l - 1) * np.sqrt(2 / size_l - 1)
```



## Python Implementation

Below is a Python example that initializes the weight matrices $W$ for each node $W^i$ with a uniform distribution of random values. Bias vectors are initialized to zeros. It accepts an array or list which contains the dimensions for each layer and returns a matrix and bias vector for each layer.

```python
def initialize_parameters(layers_dims):
    np.random.seed(1)               
    parameters = {}
    
    # Get the number of layers
    L = len(layers_dims)            
    
    # For each layer initalize the weights and bias vector
    for l in range(1, L):
        parameters["W" + str(l)] = np.random.randn(
            layers_dims[l], layers_dims[l - 1]) * 0.01
        parameters["b" + str(l)] = np.zeros((layers_dims[l], 1))

        assert parameters["W" + str(l)].shape == (
            layers_dims[l], layers_dims[l - 1])
        assert parameters["b" + str(l)].shape == (layers_dims[l], 1)

    return parameters
```



##### Sources

https://medium.com/usf-msds/deep-learning-best-practices-1-weight-initialization-14e5c0295b94

https://www.youtube.com/watch?v=OF8ocg5mgx0&list=PLLssT5z_DsK-h9vYZkQkYNWcItqhlRJLN&index=55