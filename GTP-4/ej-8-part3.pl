/* Escriba un programa en Prolog que recorra un árbol binario y determine la profundidad del mismo. 
La representación del árbol será una lista con el siguiente formato: [I, N, D]. */

profundidad([], 0).
/* si el subarbol o arbol es vacio, su profundidad sera 0 */

profundidad([_], 1).
/* si el subarbol contiene algo es porque es hijo-padre dentro del arbol, entonces suma 1 a la profundidad */

profundidad([Izq, _, Der], P) :-
    profundidad(Izq, PI),
    profundidad(Der, PD),
    Max is max(PI, PD),
    /* max(PI,PD) calcula la profundidad maxima entre el subarbol izquierdo y el derecho */
    P is Max+1, !.
    /* se suma 1 contando al nodo padre */
