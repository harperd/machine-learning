# Neural Networks

*Neural Networks* (NNs) are much better for a complex non-linear hypothesis even when feature space is huge. They were originally motivated by looking at machines which replicate the brain's functionality. Neural networks were used a lot in the 80s and 90s with their popularity diminished in the late 90s. However, there has been a resurgence in neural networks because large scale NNs have became computationally feasible.

In neural networks, *layer 1* is the input layer followed by a number of *hidden layers* (layer 2 in the example below) and an *output layer* which produces the hypothesis result. Each layer is comprised of *activation functions* also called *neurons*. 

![Neural Network](../images/neural-network.png)

## Activation Functions

In artificial neural networks, the *activation* function (also referred to as a unit or neuron) of a node defines the output of that node given an input or set of inputs. A standard computer chip circuit can be seen as a digital network of activation functions that can be "ON" or "OFF", depending on input. The *Sigmoid* function is one of several popular activation functions.

![Activation Functions](../images/activation-functions.png)

Activation functions are typically denoted by $a$ where:

> $a^{(j)}_i$ is an activation function of the $i$th activation function (neuron) in the $j$th hidden layer.
>
> $a^{(2)}_1$ is an activation function of the $1^{st}$ activation function (neuron) in the $2^{nd}$ hidden layer.

## NN Matrix

The values passed between layers in a nerual network a represented as a matrix of values (or weights) as denoted by $\theta$ where:

> $\theta^{(j)}$ is a matrix of values controlling function mapping from layer $j$ to the next layer, $j+1$.
>
> $\theta^{(2)}$ is a matrix of values controlling function mapping from layer $2$ to layer $3$.

Input thetas to an activation function are superscripted with the index of the calling layer where:

> $\theta^{(2)}$ matrix would be input to $a^{(3)}_i$ and output a $\theta^{(3)}$ matrix.

### Matrix Dimensions

If a neural network has $s_j$ activation functions in layer $j$ and $s_{j+1}$ in layer $j+1$, then $\theta^{(j)}$ will be of dimension $s_{j+1}$ x $(s_j+1)$. In other words, the number of columns ($m$) is the number of activation functions in the next layer and the number of rows ($n$) is the number of activation functions plus 1 from the current layer.

![Neural Network](../images/neural-network-matrix-size.png)

