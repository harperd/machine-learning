# Architecting a Basic Neural Network

![](../images/nn-design.png)

When deciding how to design a basic neural network you will need to start by answering a few questions:

1. How many input units input layer?
2. How many hidden layers?
3. How many activation units in each hidden layer?
4. How many outputs units in the output layer?

## Input Units

The number of input units are decided by the dimentions of your features $x^{(i)}$. So, if you have $5$ features, you would have $5$ input units.

## Output Units

Output units are equal to the number of classes in your multi-class classification problem. So, if your network is deciding if a picture is a cat or a dog then you would have $2$ output units.

## Hidden Layers

When deciding on the number of layers, a basic $3$ layer network architecture with just a single hidden layer is very common. If you decide on more hidden layers, having the same number of activation units in each layer is quite common. Having more hidden layers is computationally more expensive but can improve neural network performance.

## Activation Units

The number of activation units should be somewhat greater than the number of input units. For example, for $3$ input units you may decide on using $5$ activation units within each hidden layer.