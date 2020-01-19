% X, Y are siblings if they share a parent
sibling(X, Y)      :- parent_child(Z, X), parent_child(Z, Y).

% Father, mother implies parent
parent_child(X, Y) :- father_child(X, Y).
parent_child(X, Y) :- mother_child(X, Y).

% Introduce some people
father_child(tom, sally).
father_child(tom, erica).

% Ask:
?- sibling(sally, erica).
Yes
