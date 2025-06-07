/* Cree un programa en Prolog que permita calcular el factorial de un número con el predicado
factorial/2, validando que dicho número sea mayor o igual a cero. */

factorial(0,1).
factorial(1,1).

factorial(N,F) :- N > 1,A is N-1,factorial(A,R),F is N*R.

/* Va "acumulando" las llamadas hasta llegar a los hechos de 0 y 1, de ahi empieza a multiplicar en F y eso es lo que retorna.
! sirve para que una vez que llegue al caso base corte después de terminar. */
