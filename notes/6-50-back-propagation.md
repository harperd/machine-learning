# Back Propagation

Back propagation is how neural networks *learn*. They take the final output at the output layer and work it's way back to layer 2.

In back propagation we want to capture the error, for each unit, of how far off it was when computing the hypotheis during forward propagation. To find the error of each node in each layer we start at the last layer and progress to the the second layer (non-input layer) and capture the error for each unit in each layer. The error term is represented as $\delta^{(l)}_j$ (delta) and computed by simply subtracting the hypotheses at each unit $a^{(l)}_j$ by the correct value $y_j$ from our labeled training data.

For and example with a 4 layer network ($L=4$), back propagation would start at layer 4 with the below where $j$ is the index of each output unit:

> $\delta^{(4)}_j=a^{(4)}_j-y_j$

Which can also be written as:

> $\delta^{(4)}_j=h_\Theta(x)_j-y_j$

This can easily be vectorized as the following where $a$ and $y$ are vectors with dimensions equal to the number of output units in the network (in this instance $4$):

> $\delta^{(4)}=a^{(4)}_j-y$

For the remainder of the layers, the computation is a little different. In using vectors for each layer, we take the error from the previous layer and multiply that by the $\Theta$ values for that current layer. Then, perform element wise multiplication by the prime of the activation units for that layer:

> **Layer 3**
>
> $\delta^{(3)}=(\Theta^{(3)})^T\delta^{(4)}\cdot g\prime(z^{(3)})$
>
> **Layer 2**
>
> $\delta^{(2)}=(\Theta^{(2)})^T\delta^{(3)}\cdot g\prime(z^{(2)})$

Here $g\prime$ ($g$ prime) is the *derivative* of the specific activation function which can be derived by using Calculus. For example, if we were using *Sigmoid* functions for each unit in a particular layer:

> $g(z)=\frac{1}{1+e^{-z}}$

 The derivative of *Sigmoid* would be:

> $g\prime(z)=g(z)\cdot(1-g(z))$

What the derivative is actually giving us is the gradients for that layer with our objective being finding the global minimum.

If there is no regularization involved (ignoring $\lambda$ or $\lambda=0$) in back propagation then the partial derivative terms you want are exactly given by activations and delta terms:

> $\frac{\partial}{\partial\Theta^{(l)}_{ij}}J(\Theta)=a^{(l)}_j\delta^{(l+1)}_1$

# Back Propagation With a Large Training Set

If we have a large training set such as:

> $\{(x^{(1)},y^{(1)}),...,(x^{(m)},y^{(m)})\}$

We will initialize all values to zero:

> $\Delta^{(l)}_{ij}=0$ (for all $l, i, j$)

The $\Delta$ term will be used to compute the partial derivative with respect to:

> $\frac{\partial}{\partial\Theta^{(l)}_{ij}}J(\Theta)$

