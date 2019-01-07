
### Summary： Predictive Movie Ratings
- Content based recommendations
  1. A set of movies {1, ..., i, ...}, a set of users {1, ..., j, ...}.
  2. Movies are rated by the users. Some movie may not receive ratings from users.
  3. Given feature vectors for each movie. (This feature vector is the same for each user.)
  4. Each user has a preference governed by the vector Theta, which is unknown to the modeler and is to be estimated.
  5. Linear regression to find estimate the Theta vector.

### Summary: Collaborative Filtering (what if content is not available?)
- Collaborative Filtering (feature learning)
  1. A set of movies {1, ..., i, ...}, a set of users {1, ..., j, ...}.
  2. Movies are rated by the users. Some movie may not receive ratings from users.
  3. Now, we are given each user's preference -- the vector Theta, e.g. {"action": "5 stars", "romance": "3 stars", ...}.
  4. We learn from users' preference the content features of each movie.
  5. So we are able to do Theta -> X -> Theta -> X ... *This is possible because user-movie is a many-to-many relationship!*
