; Se desea crear un función que reciba como parámetros una lista de átomos compuesto únicamente
; de letras y devuelva una lista agrupando los que son iguales en sublistas.


(define buscar-iguales (lambda (elem ls)
                         (if (null? ls)
                             '()
                             (if (equal? elem (car ls))
                                 (cons elem (buscar-iguales elem (cdr ls))) ; se va creando la sublista con todos los elementos que son iguales
                                 (buscar-iguales elem (cdr ls)) ; si no es el elemento prosigue con el proximo en la lista
                                 )

                         )
  )
  )


(define eliminar-iguales (lambda (elem ls)
                           (if (null? ls)
                               '()
                               (if (equal? elem (car ls))
                                   (eliminar-iguales elem (cdr ls)) ; si es el elemento a eliminar entonces lo que se hace es "ignorarlo" y se sigue con la cola de la lista
                                   (cons (car ls) (eliminar-iguales elem (cdr ls))) ; si no es, se hace una lista nueva con el elemento que no es, y la lista de la busqueda resultante con la cola de la lista original
                           )
                               )
                           )
  )


(define agrupar (lambda (ls)
                  (if (null? ls)
                      '()
                      (let* ((elem (car ls)) ; elemento que sigue a tratar de la lista
                             (subgrupo (buscar-iguales elem ls)) ; extrae todos los elementos que son iguales al elemento en una sublista
                             (resto (eliminar-iguales elem ls))) ; elimina todos los elementos iguales a el elemento y retorna la nueva lista sin el elemento
                        (cons subgrupo (agrupar resto)) ; llama a la recursion para pasar al siguiente elemento en la lista
                        )
                      )
                  )
  )
                 

(agrupar '(A A B C A B A D C)) ;→ ((AAAA) (BB) (CC) (D)) 