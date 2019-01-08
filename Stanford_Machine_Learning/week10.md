- Why large data? learning curve.
  - m is not helpful when high bias.
  - m is helpful when high variance.
  - so we shift the data from high bias to high variance by adding more features etc..
  
  
## stochastic gradient descent.

- Batch gradient descent: has to load data all at once.
- Stochastic gradient descent: 
  - focus one on one single traing example, at one iteration.
  - define single observation cost.
  - randomly shuffle dataset
  - try to improve with just with one observation at each time.
**The trade off is accuracy and efficiency. whether it takes a painful time of thinking before you move a step.**
  
## mini batch

Some where between Batch GD (with m examples) and stochastic GD (with 1 example).

*It reminds me of difference sampling methods. It looks like systematic sampling. Of course depending on the data, cluster sampling and stratified sampling can be better.*

## SGD convengence. How to tune the hyperparameters to make sure it converges?
The graph is: `x- nb. of iterations. y - cost`
1. smaller learning rate
2. features
3. increase the nb. of examples for checking for convergence.
In SGD, the path is less noisy with decreasing learning rate as iteration number increases.

This method is used both for tuning learning rate and checking that SGD is functioning correctly.

## online learning.

