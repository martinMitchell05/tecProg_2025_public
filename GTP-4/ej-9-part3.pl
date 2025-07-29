/* Escriba un programa en Prolog que, dada una lista numérica ordenada,
inserte un elemento en el lugar correspondiente según el orden. */

/* si llego al final de la lista y todavía no inserté el elemento, se inserta al final de una lista. */
insertar(N,[],[N]):- !.
insertar(_,[],[]).
/* cuando el numero sea menor o igual al que esta en la lista se inserta delante del de la lista y la cola queda igual. */
insertar(N,[E|C],[N,E|C]):-
    N =< E, !.

insertar(N,[E|C],[E|R]):-
    N > E,
    insertar(N,C,R).
