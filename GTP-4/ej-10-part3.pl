/* Escriba un programa en Prolog que recursivamente ordene una lista de números enteros. */

/* Realiza un ordenamiento de bubble sort siempre que la lista resultante sea distinta a la entrante, si no cambia quiere decir que ya está ordenada. */
ordenar(L, R) :- 
    ordenamiento(L, L1),
    ( L = L1 -> R = L ; ordenar(L1, R) ).

/* Implementa un ordenamiento de bubble sort. */
ordenamiento([N],[N]).
ordenamiento([P,Q|C],[P|R]):-
    P =< Q,
    ordenamiento([Q|C],R), !.

ordenamiento([P,Q|C],[Q|R]):-
    P > Q,
    ordenamiento([P|C],R).
