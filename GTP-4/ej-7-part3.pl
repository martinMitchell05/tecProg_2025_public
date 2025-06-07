/* Escriba un programa en Prolog que, dada una lista, elimine todos los elementos duplicados de la misma. */

contar(_,[],0).
contar(L,[E|R],C) :- E == L,contar(L,R,T),C is T+1,!.
contar(L,[E|R],C) :- E \== L,contar(L,R,T),C is T.

buscar_dup(_,[],[]).
buscar_dup(Dup,[E|L],subLis):-
    Dup == E,
    buscar_dup(Dup,L,subAux),
    subLis = [Dup|subAux].

buscar_dup(Dup,[E|L],subLis):-
    buscar_dup(Dup,L,subAux),
    subLis = [E|subAux].

eliminar_dup([],[]):-!.
eliminar_dup([E|L],sinDup) :-
    contar(E,[E|L],C),
    C > 1,
    buscar_dup(E,[E|L],subL),
    eliminar_dup(subL,dupsAux).

eliminar_dup([E|L],sinDup) :-
    eliminar_dup(L,dupsAux),
    sinDup = [E|dupsAux].

/* FINALIZAR */