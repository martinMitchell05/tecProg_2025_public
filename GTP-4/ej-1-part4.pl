/* Utilice un operador de corte donde corresponda para que el programa finalice una vez terminada la
recursión y no retorne el false final. */

factorial(0, 1).
factorial(Numero, Factorial) :-
    Numero > 0,
    NumeroAnt is Numero - 1,
    factorial(NumeroAnt, FactorialAnt),
    Factorial is Numero * FactorialAnt, !.