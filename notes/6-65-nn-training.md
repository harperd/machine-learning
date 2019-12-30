# Neural Networks: Training

Below is the basic code that's needed for training a neural network:

1. Initialize random weights
2. Implement forward propagation to compute $\large h_\Theta(x^{(i)})$ for any $x^{(i)}$
3. Implement code to compute the cost function $J(\Theta)$
4. Implement back propagation to compute partial derivatives $\large\frac{\partial}{\partial\Theta^{(l)}_{jk}}J(\Theta)$
5. Implement toggleable code in back propagation to perform gradient checking 

Iterate over each training example $(x^{(i)},y^{(i)})$ performing forward propagation and back propagation until you get through all of the training examples. Then, take the deltas from back propagation and compute the partial derivatives for the cost function $J(\Theta)$.

##### Sources

https://www.youtube.com/watch?v=cObOAIImeVQ&list=PLLssT5z_DsK-h9vYZkQkYNWcItqhlRJLN&index=56

