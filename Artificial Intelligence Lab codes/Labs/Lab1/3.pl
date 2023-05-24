
/* Facts */

/* Dog is mammal */
isa(dog, mammal).

/* Sparrow is a bird */
isa(sparrow, bird).


/* Rule: Something is an animal, if it is a mammal or a bird */
animal(X) :- isa(X, mammal); isa(X, bird).




