;  Escriba en Racket el procedimiento (concatenar l1 l2) que recibe dos listas l1 y l2 como argumento y
; retorna una única lista que contiene primero todos los elementos de l1 seguido de todos los
; elementos de l2 (no puede usar el procedimiento interno append que viene en algunas implementaciones de Racket).


(define agregar-lista (lambda (ls-in ls-out)
                        (if (null? ls-in)
                            ls-out
                            (agregar-lista (cdr ls-in) (cons (car ls-in) ls-out)))
                            )
                        )

(define invertir (lambda (ls-in ls-out)
                   (if (null? ls-in)
                       ls-out
                       (invertir (cdr ls-in) (cons (car ls-in) ls-out))
                   )
                   )
  )


(define concatenar (lambda (l1 l2)
                     (let* ((sub-ls1 '())
                       (sub-ls2 (agregar-lista l1 sub-ls1))) ; se agregan todos los elementos de la primer lista
                       (invertir (agregar-lista l2 sub-ls2) '()) ; se agregan a la lista anterior los elementos de la segunda lista y luego se invierte para mantener el orden original
                       )
                     )
  )

(concatenar '(1 2 3) '(4 5 6 7)) ; --> (1 2 3 4 5 6 7)