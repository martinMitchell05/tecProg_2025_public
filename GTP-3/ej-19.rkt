; Se desea crear una función que reciba como parámetro una lista de strings y devuelva una lista con las cadenas ordenadas por su peso ASCII.

(define sumaLista (lambda (ls)
                    (if (null? ls)
                        0
                        (+ (car ls) (sumaLista (cdr ls)))
                        )
                    )
  )

; 2. calcular el peso de una palabra

(define pesoPalabra (lambda (palabra)
                      (sumaLista (map char->integer (string->list palabra))) ; convierte el caracter a un entero para cada caracter de la lista de caracteres y los suma
                      )
  )

; 3. concatenar cada palabra con su peso

(define listaPesos (lambda (ls)
                     (map cons ls (map pesoPalabra ls))
                     )
  )

; 4. insertar los elementos de forma ordenada

(define insertaOrdenado (lambda (elem ls)
                          (if (null? ls)
                              (list elem)
                              (if (< (cdr elem) (cdar ls))
                                  (cons e ls)
                                  (cons (car ls) (insertaOrdenado elem (cdr ls)))
                                  )
                              )
                          )
  )

; 5. Eliminar un elemento de la lista

(define eliminar (lambda (elem ls)
                   (if (null? ls)
                       '()
                       (if (equal? elem (car ls))
                           (cdr ls)
                           (cons (car ls) (eliminar elem (cdr ls)))
                           )
                       )
                   )
  )

; 6. Ordenar las palabras por su peso

(define ordenarAux (lambda (l1 l2)
                     (if (null? l1)
                         l2
                         (ordenarAux (cdr l1) (insertaOrdenado (car l1) l2))
                         )
                     )
  )

; 7. Wrapper
(define ordenar (lambda (ls)
                  (ordenarAux (listaPesos ls) '())
                  )
  )

(ordenar '("moto" "auto" "casa" "juego" "aire"))