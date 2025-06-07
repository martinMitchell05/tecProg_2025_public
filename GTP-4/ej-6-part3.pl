/* Escriba un programa en Prolog que reciba dos listas de números, verifique que sean de la misma
longitud, y luego retorne una lista con la suma elemento a elemento de ambas listas. */

cantidad([],0).
cantidad([_|C],T) :- cantidad(C,S),T is S+1.

suma_lista([],[],[]).

suma_lista([E1|Cola1],[E2|Cola2],Suma):-
    cantidad(Cola1,T1),cantidad(Cola2,T2),
    T1 == T2,
    suma_lista(Cola1,Cola2,SAux),
    Acum is E1 + E2,
    Suma = [Acum|SAux].
