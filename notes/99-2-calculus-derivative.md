# Derivatives

A *derivative* (slope of a line) is measuring the sensitivity of a function's output with respect to a very small change in  input. In other words, it measures the *steepness* of the graph of a function.

If we want to find the derivative of the a linear function like below:

> $f(x)=3x^2$

Then, given the definition of slope is the change in $y$ divided by the change in $x$, we have the below where $h$ represents an extremely small number like $.00001$:

> $\large d=\frac{\Delta y}{\Delta x}=\frac{f(x+h)-f(x)}{h}=\frac{3(x+h)^2-3x^2}{h}$

Apply the slope formula:

> $\large d=\frac{(3x+2xh+3h^2)-3x^2}{h}$

Simplify:

> $\large d=\frac{2xh+3h}{h}=\small 2x+3$

Next, set $h$ to $0$ (the limit of $h$ approaches $0$):

> $d=

If we have a point where $x=2$ then $y=6$

> $f(2)=3\cdot2=6$ 

Therefore, our first point is at:

> $(2,6)$

If we say $x=6.001$, then:

> $f(6.001)=3\cdot6.001=18.003$

Therefore, our second point is at:

> $(6.001,18.003)$

If we want to know what the derivative is we take the change in $y$ and divide by the change in $x$:

> $\large\frac{\Delta y}{\Delta x}=\large\frac{6.001-2}{18.003-6}=\frac{4.001}{12.003}=\small.\overline{33}$

Therefore, we say the *derivative of our function $f(x)$ with respect to* $x$ is $.\overline{33}$.

> $\large\frac{df(x)}{dx}=\small.\overline{33}$

Or, more precisely, we would use the delta $\delta$ term which says: The delta (or rate of change), which is the derivative for the function $f(x)$ with respect to $x$ is $.\overline{33}$.

> $\delta=\large\frac{df(x)}{dx}=\small.\overline{33}$

# Derivatives and Quadratics

For getting the derivative of a quadratic function we will need to calculate it with respect to the tangent line as shown below. Also, since quadratics are complex function and don't yield a simple straight line we only know the partial derivative $\partial$ at any given point since it is constantly changing.

> $\large\frac{\partial f(x)}{\partial x}$ or $\large\frac{\partial}{\partial x}f(x)$

![Derivative of a Quadratic](../images/calculus/derivative_quadratic.png)