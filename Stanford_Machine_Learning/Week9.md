
### Summary： Predictive Movie Ratings

- Content based recommendations
  1. A set of movies {1, ..., i, ...}, a set of users {1, ..., j, ...}.
  2. Movies are rated by the users. Some movie may not receive ratings from users.
  3. Given feature vectors X for each movie. (This feature vector is the same for each user.)
  4. Each user has a preference governed by the vector Theta, which is unknown to the modeler and is to be estimated.
    - Rating of movie i from user j := X_{i} .* Theta_{j,i};
  5. Linear regression to find estimate the Theta vector.

### Summary: Collaborative Filtering (what if content is not available?)

- Collaborative Filtering (feature learning)
  1. A set of movies {1, ..., i, ...}, a set of users {1, ..., j, ...}.
  2. Movies are rated by the users. Some movie may not receive ratings from users.
  3. Now, we are given each user's preference -- the vector Theta, e.g. {"action": "5 stars", "romance": "3 stars", ...}.
  4. We learn from users' preference the content features of each movie.
    - Rating of movie i from user j := X_{i} .* Theta_{j,i}
  5. So we are able to do Theta -> X -> Theta -> X ... *This is possible because user-movie is a many-to-many relationship!*

- Collaborative Filtering Algorithm (solve X and Theta simultaneously)
  1. Hold X constant, solve Theta; Hold Theta constant, solve X.
  2. Algorithm
    1. Intialize X and Theta
    2. Minimize for the cost function using gradient descent for each i, j.
    3. For user with parameter Theta, and a movie with (learned) features X, predict their rating by the inner product of Theta and X.

### Summary: Low Rank Matrix Factorization.

- Vectorization: Low Rank Matrix Factorization
  1. Low rank matrix factorization
    - form the user-movie matrix.
    - form the predicted ratings matrix.
    - X: movie per row. Theta: user per row.
  2. find related movies: X difference is small.
  
- Implementational Detail: Mean normalization
  1. mean normalize the user-movie matrix by row

