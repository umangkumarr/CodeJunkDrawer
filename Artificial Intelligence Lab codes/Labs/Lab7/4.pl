american (west).
missile (missilel).
weapon (Y) :- missile (Y).
enemy (nono, america).
hostile (Z) :- enemy (Z, america).
owns (nono, missile1).
sells (west,X,nono) :- missile (X), owns (nono, X).
criminal (X) :- american (X) ,weapon (Y) , sells (X, Y, Z), hostile (Z).