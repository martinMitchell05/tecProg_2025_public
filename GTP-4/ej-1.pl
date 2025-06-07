# A continuación, se presenta un cuerpo de conocimiento en Prolog. Responda qué retornarán las
# consultas dadas este cuerpo de conocimiento.

# cuerpo de conocimiento

f(a,2).
f(a,3).
f(b,2).
f(b,4).
f(c,1). 
f(c,2).
 
# Consultas:
# a- f(X,1). --> X = c
# b- f(X). --> error, false --> incompleta
# c- f(a,X). --> X = 2; X = 3
# d- f(c,1). --> true 
# e- f(X,Y). --> X = a, Y = 2;
# X = a, Y = 3; X = b, Y = 2; X = b, Y = 4; X = c, Y = 1; X = c, Y = 2;
# todos los pares que cumplen con la consulta

# f- f(2,a). --> false
# g- f(X,Y),f(X,4). --> X = b, Y = 2; X = b, Y = 4; false. --> busca todos los que cumplan f(X,Y) ^ f(X,4)

# En los casos que exista unificación, para que muestre
#todas las soluciones posibles quedara esperando por cada una,
# para pasarlas se debe apretar tab 