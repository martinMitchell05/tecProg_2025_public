; Escriba una función largo que devuelva el largo de una lista sin utilizar la función definida en Racket.

(define (largo lista)
  (if (null? lista)
      0
      (+ (largo (cdr lista)) 1)))

(largo '(1 4 8 9))