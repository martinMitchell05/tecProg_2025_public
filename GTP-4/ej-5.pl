/* Rutas Existentes */

ruta(santafe, parana).
ruta(parana, corrientes).
ruta(santafe, cordoba).
ruta(santafe, coronda).
ruta(santafe, rosario).
ruta(rosario, capital).
ruta(rosario, mardelplata).
ruta(capital, cordoba).

combinacion(Desde,Hasta) :- ruta(Desde,Z),ruta(Z,Hasta).

/* ¿Desde que orígenes se llega a Córdoba? --> ruta(Origen,cordoba). */

/* ¿Que destinos son alcanzados desde Paraná? --> ruta(parana,Destino). */

/* ¿Hay alguna ruta entre Paraná y Córdoba? --> ruta(parana,cordoba); ruta(cordoba,parana) */

/* ¿Hay alguna combinación de dos rutas que permita ir desde Santa Fe a Corrientes?
    opcion.1. que retorna con que ciudad se hace la combinacion --> ruta(santafe,Y),ruta(Y,corrientes).
    opcion.2. retorna si existe o no alguna combinacion para llegar --> combinacion(Desde,Hasta) :- ruta(Desde,Z),ruta(Z,Hasta). */