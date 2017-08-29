node(a).
node(b).
node(c).
node(d).
node(e).
node(f).
edge(a, b).
edge(a, d).
edge(b, c).
edge(b, e).
edge(d, e).
edge(d, f).
edge(e, f).

cover(X) | ncover(X) :- node(X).

:- edge(X, Y), not cover(X), not cover(Y).

:~ cover(X).
