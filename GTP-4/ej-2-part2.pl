/* Arbol Genealogico */

hombre(x).
mujer(y).
progenitor(z,w).

padre(P,H) :- hombre(P),progenitor(P,H),P\=H.
madre(M,H) :- mujer(M),progenitor(M,H),M\=H.

hermano(P,H) :- padre(M,P),padre(M,H),madre(F,P),madre(F,H),P\=H.
hermano_varon(P,H) :- hombre(P),hermano(P,H),P\=H.
hermana_mujer(M,H) :- mujer(M),hermano(M,H),M\=H.

abuelo(A,P) :- padre(A,X),padre(X,P);padre(A,Y),madre(Y,P).
abuela(A,P) :- madre(A,X),padre(X,P);madre(A,Y),madre(Y,P).

sucesor(X,P) :- abuelo(P,X);abuela(P,X);padre(P,X);madre(P,X).

es_madre(Y) :- madre(Y,_).
es_padre(X) :- padre(X,_).

tia(T,P) :- padre(H,P),hermana_mujer(T,H);madre(F,P),hermana_mujer(T,F).

yerno(Y,S) :- \+ padre(S,Y),\+ madre(S,Y), padre(Y,P),abuelo(S,P);\+ padre(S,Y),\+ madre(S,Y), padre(Y,P),abuela(S,P).

/* TERMINAR */