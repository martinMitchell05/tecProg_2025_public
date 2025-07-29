/* Se define la base de conocimientos del problema:
Se define cada tramo con su ciudad de partida, llegada y su precio. */
tramo('Cordoba Capital','Carlos Paz',1500).
tramo('Carlos Paz','Bialet Masse',1500).
tramo('Bialet Masse','Valle Hermoso',1000).
tramo('Valle Hermoso','La Falda',1200).
tramo('La Falda','Huerta Grande',1000).
tramo('Huerta Grande','La Cumbre',1200).
tramo('La Cumbre','Capilla Del Monte',1600).
tramo('Capilla Del Monte',_,0).

/* Se define el recorrido que hará cada persona con la ciudad de partida y llegada. */
recorrido('Jorge','Cordoba Capital','La Falda').
recorrido('Adriana','Valle Hermoso','La Cumbre').
recorrido('Gabriela','Carlos Paz','Capilla Del Monte').
recorrido('Roberto','Bialet Masse','Huerta Grande').
recorrido('Jose','Cordoba Capital','Capilla Del Monte').

/* Regla que busca si existe un camino desde la ciudad X hacia Y, retornando una lista con el recorrido completo. */
camino(X,Y,[X]):-
                X==Y.
camino(X,Y,[X|Lista]):-
                tramo(X,Z,_),
                camino(Z,Y,Lista),!.

/* Regla que cuenta la cantidad de veces que aparece una ciudad "Y" en una lista de ciudades destino. */
contar(_,[],0).
contar(Y,[X|L],Cant):- X==Y,contar(Y,L,U),Cant is U+1. 
contar(Y,[X|L],Cant):- X\=Y,contar(Y,L,U),Cant is U.

/* Regla que para cada ciudad del recorrido, calcula el valor final que tendrá según la cantidad de personas que pasen por dicha ciudad.
Recibe : 
    Lista de ciudades de un recorrido;
    Lista con las ciudades que recorre una persona; */
contar_apareciones([],_,[]).
contar_apareciones([X|Lista], LisConcPers, [[X,Valor]|ListaPesos]):-
                                                        contar_apareciones(Lista,LisConcPers,ListaPesos),
                                                        contar(X,LisConcPers,Cantidad),
                                                        tramo(X,_,Precio),
                                                        (Cantidad\=0 -> Valor is Precio/Cantidad;Valor is 0).

/* Regla para concatenar los elementos de dos listas en una tercera. */
concatenar([_|[]],L2,L2).
concatenar([X|L1],L2,[X|L3]):-
                            concatenar(L1,L2,L3).

/* Regla para concatenar sublistas en una sola lista. */
concatenarListas([],[]).
concatenarListas([X|L1],Lista):-
                            concatenarListas(L1,ListaAux),
                            concatenar(X,ListaAux,Lista).

/* Regla que para cada persona que realice un recorrido le calcula su subtotal a pagar.
Recibe : 
    Lista con las ciudades por donde pasa la persona;
    Lista de todas las ciudades con su valor calculado según la cantidad de personas que pasen por ella. */
calcularSubtotal([_|[]],[],0).
calcularSubtotal([_|[]],_,0).
calcularSubtotal(_,[],0).
calcularSubtotal([X|ListaParPer],[[Y,Z]|ListaTotalPar],SubtotalPers):-
                                                                X == Y,
                                                                calcularSubtotal(ListaParPer,ListaTotalPar,MediaSuma),                                                           
                                                                SubtotalPers is MediaSuma+Z.

calcularSubtotal([X|ListaParPer],[Y|ListaTotalPar],SubtotalPers):-
                                                                X\=Y,
                                                                calcularSubtotal([X|ListaParPer],ListaTotalPar,MediaSuma),
                                                                SubtotalPers is MediaSuma.

/* Regla que recibe una lista de nombres de personas y para cada una arma su recorrido correspondiente. */
armarTramos([],[]).
armarTramos([X|Nombres],[Aux|Lista]):-
                                armarTramos(Nombres,Lista),
                                recorrido(X,P,LL),
                                camino(P,LL,Aux),
                                !.

/* Regla que calcula el total a pagar para cada persona.
Recibe :
    Lista de personas;
    Lista de recorrido de las personas;
    Lista de las ciudades con su valor correspondiente; */
calculoFinal([],[],_,[]).
calculoFinal([X|Nombres],[Y|ListasPorPersona],ListaTodasLasCiudadesPeso,[[X,Y,Subtotal]|AuxListaFinal]):-
                                                                                calculoFinal(Nombres,ListasPorPersona,ListaTodasLasCiudadesPeso,AuxListaFinal),
                                                                                calcularSubtotal(Y,ListaTodasLasCiudadesPeso,Subtotal).
                                                                                
                                                                                
                                                                            


/* Regla principal, la cual va llamando a reglas secundarias para poder hacer una repartición de costos del viaje para las personas que se ingresan. */
repartir_costos(Nombres,Resultado):-
                        armarTramos(Nombres,ListaTramosPers),
                        concatenarListas(ListaTramosPers,ListaConcPers),
                        camino('Cordoba Capital','Capilla Del Monte',ListaTotalCiudad),
                        contar_apareciones(ListaTotalCiudad,ListaConcPers,ListaPesos),
                        calculoFinal(Nombres,ListaTramosPers,ListaPesos,Resultado),!.
