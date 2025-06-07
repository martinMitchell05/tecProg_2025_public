/* Escriba un programa en Prolog que reciba como primer parámetro una lista de números y unifique el
segundo con la cantidad de elementos de dicha lista. */

cantidad([],0).
cantidad([_|C],T) :- cantidad(C,S),T is S+1.

/* Recursión hasta que la lista que se le pase esté vacía,
ahí empieza a sumar el largo de la lista. */