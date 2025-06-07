
entrada("empanadas").
entrada("papas").
entrada("picada").

principal("asado").
principal("locro").
principal("pizza").

postre("flan").
postre("queso y dulce").
postre("tiramisu").

carta(X,Y,Z) :- entrada(X),principal(Y),postre(Z).

