/* Facts */ 

/* It is hot today */
hot(today).

/* It was hot yesterday */
hot(yesterday).

/* Rule */

/* If it is hot, it will rain */
rainy(X) :- hot(X).

