/* Cree un programa en Prolog que cuente la cantidad de veces que aparece un elemento en una lista. */

contar(_,[],0).

contar(L,[E|R],C) :- E=L,contar(L,R,T),C is T+1.
contar(L,[E|R],C) :- E\=L,contar(L,R,T),C is T.

/* Primero evalua a la letra L y E que es el primer miembro de una lista.
Si son iguales pasa por linea 5 hasta llegar al caso base y empieza a sumar,
si son distintos pasa con R (resto de la lista) tambien pero sin sumar nada al acumulador. */