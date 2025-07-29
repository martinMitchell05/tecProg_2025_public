/* Evaluar las siguientes consultas, dejando registrado para cada una el resultado obtenido y explicando
en lenguaje natural por qué se obtiene dicho resultado, detallando los puntos de elección que han
sido desechados y cuál es el operador de corte por el cual han sido quitados. */

p(1).
p(2):- !.
p(3).

/*
a) p(X). --> encuentra la primer ocurrencia que unifica a X -> 1, sigue buscando y unifica X -> 2 y corta por el predicado
b) p(X), p(Y). --> va unificando para cada X los valores de Y, comenzando desde X=1 -> Y=1 e Y=2, luego aumenta X=2, Y=1 e Y=2, corta por el predicado
c) p(X), !, p(Y). --> solamente unifica para X=1, todos los valores de Y, luego corta, es decir hace X=1, Y=1, Y=2, corta.
*/