/*Construya el árbol de resolución para la consulta del punto “c” del ejercicio 3.
Consulta del Punto “c”: menu(M), member('Locro', M).*/

menu(['Bombones de jamon', 'Locro', 'Dulce de batata']).
menu(['Bombones de jamon', 'Locro', 'Alfajor norteño']).
menu(['Tarta de Atun', 'Atados de repollo', 'Dulce de batata']).
menu(['Tarta de Atun', 'Pollo romano con hierbas y vino', 'Flan']).
menu(['Volovanes de atun', 'Matambre con espinacas y parmesano', 'Torta moka']).
menu(['Buñuelos de bacalao', 'Pollo romano con hierbas y vino', 'Alfajor norteño']).

/* Va buscando en el menu "M" en cada miembro si contiene el plato 'Locro', lo retorna como opcion en cada ocurrencia. 
    Un posible problema seria que si 'Locro' esta como otro plato ademas de principal, y yo solo necesito los principales, tambien me retorna
    las otras posibilidades.
    
    Una solucion es consultar segun el tipo de lista que me interesa, Por ejemplo: menu(['Locro',X,Y]). --> false */