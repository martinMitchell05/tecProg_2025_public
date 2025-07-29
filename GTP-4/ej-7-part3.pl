/* Escriba un programa en Prolog que, dada una lista, elimine todos los elementos duplicados de la misma, excepto la primer ocurrencia. */

contar(_,[],0).
contar(L,[E|R],C) :- E = L,contar(L,R,T),C is T+1,!.
contar(L,[E|R],C) :- E \= L,contar(L,R,T),C is T,!.

buscar_dup(_,[],[]):- !.
buscar_dup(Dup,[E|L],subLis):-
    Dup = E,
    buscar_dup(Dup,L,subAux),
    subLis = [Dup|subAux].

buscar_dup(Dup,[E|L],subLis):-
    Dup \= E,
    buscar_dup(Dup,L,subAux),
    subLis = [E|subAux].

eliminar_dup([],[]).
eliminar_dup([E|L],sinDup) :-
    contar(E,L,C),
    C >= 1,
    buscar_dup(E,L,subL),
    eliminar_dup(L,subL),
    sinDup = subL.

eliminar_dup([E|L],sinDup) :-
    contar(E,L,C),
    C = 0,
    eliminar_dup(L,dupsAux),
    sinDup = [E|dupsAux].

/* FINALIZAR */