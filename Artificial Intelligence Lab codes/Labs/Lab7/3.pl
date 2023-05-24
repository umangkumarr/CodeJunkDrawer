male(unang kumar).
male(dipender kumar).
male(rakesh).
male(inder_pal).
male(ankit).
female(neetu devi).
female(anchal).
parent(dipender_kumar, umang_kumar). 
parent(neetu_devi, umang_kumar). 
parent(dipender_kumar ,anchal). 
parent(inder_pal, dipender_kumar).
parent(inder pal, rakesh). 
parent(neetu_devi, anchal). 
parent(rakesh, ankit).

%Father and Mother
father (X, Y) :-parent (X, Y) , male (X). 
mother (X, Y) :-parent (X, Y) , female (X) .

%sibling
sibling (X, Y) :-mother (Z,Y) , mother (Z, X) . 
sibling (X, Y) :-father (2,Y) , father (Z, X).

%GrandParent
grandparent (X, Y)  :- father (Z,Y) , father (X, Z). 
grandparent (X, Y) :-mother (2, Y) , mother (X, Z).

%GrandFather
grandfather (X, Y) :-father (Z, Y) , father (X, Z).

%grandMother
grandmother (X, Y) :-mother (Z, Y) , mother (X, Z) .

%Cousin
cousin (X, Y) :-father (Z,X), father (A, Y) , sibling (Z,A).

%Uncle
uncle (X,Y) :-father (2,Y), sibling (Z,X), not (father (X, Y) ).

%Aunt
aunt (X, Y) :-father (Z, Y) , sibling (2,A), father (A, B) , mother (X, B) , not (mother)