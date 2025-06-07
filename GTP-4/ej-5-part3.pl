/* Escriba un programa en Prolog que, dada una lista de números enteros, retorne otra lista solo con los
números positivos de la misma. */

positivos([],[]). 
/* Caso base --> si se termina una lista devuelve una lista vacia para empezar a armar */

positivos([E|Cola],LPositivos):- 
                                E > 0,
                                positivos(Cola,LAux),
                                LPositivos = [E|LAux],!.
/* Caso que el elemento de la lista es positivo, se lo agrega al retorno LPositivos y sigue con la cola LAux */

positivos([_|Cola],LPositivos):- 
                                positivos(Cola,LAux),
                                LPositivos = LAux.
/* Caso que el elemento sea negativo, no agrega nada y sigue con lo que venga de la recursión */