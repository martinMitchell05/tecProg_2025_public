/* Escriba un programa en Prolog que, dada una lista de números enteros, calcule el resultado de
sumar dichos números. */

suma([],0).
suma([E|C],S) :- suma(C,A),S is A + E.