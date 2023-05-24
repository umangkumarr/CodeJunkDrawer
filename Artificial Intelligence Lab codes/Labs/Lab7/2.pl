parent(t,m).
parent(k,e).
parent(1,f).
parent(m, f).
parent(n,h).
parent(o,i).
parent(p,i).
parent(g,j).
parent(r,j).
parent(s,j).
parent(e,b).
parent(f,b).
parent(g,c).
parent(h,c).
parent(i,c).
parent(j,d).
parent(b,a).
parent(c,a).
parent(d,a).
ancestor(X,Y):-parent(X,Y).
ancestor(X,Y):- X == Y.
ancestor(X,Y):-parent(X,Z), ancestor Z,Y).