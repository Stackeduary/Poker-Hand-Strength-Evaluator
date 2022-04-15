# Coding test for candidate William Sendewicz for the Scala Bootcamp 2022 - 1 test at Evolution

### Known Limitations and Defects:

#### 1. My Texas hold 'em solution does currently break ties among hands with the same hand value based on high card(s), however, I haven't figured out a clever way to return a string when two hands are equal, for example, Ac4d=Ad4s. So I have omitted this functionality from my solution presently.

- I was working on a solution to this problem but it was getting quite messy and the juice wasn't worth the squeeze in my opinion.


#### 2. There's a bug in my Texas hold 'em implementation that isn't recognizing the case of two pair. I need to investigate that.


#### 3. I've currently implemented solutions for Five-card Draw and Texas hold 'em only; Omaha hold 'em is currently under development.

- A decent skeleton is in place for Omaha hold 'em, which I copied from Texas hold 'em, but the combinations are more complex for Omaha hold 'em in my estimation, but I don't know for sure as I've never played Omaha hold 'em.


#### 4. While my solution uses elements of the functional programming paradigm, such as pure functions and lambda expressions, I don't use recursion, map/filter/reduce or immutable data structures exclusively.

  - My solution is a mixture of procedural programming and functional programming:
    - Functions that attempt to adhere to the single responsibility principle are used throughout
    - All my functions are pure functions
    - Tuples are used in some instances, but the use of lists and dictionaries predominates

  - On the other hand, if it were a purely functional approach, there would be no for-loops in my solution, so it breaks the functional paradigm in that regard.

### How to build and run:
- Simply run `pytest <test name>` to run tests on each of the individual solvers