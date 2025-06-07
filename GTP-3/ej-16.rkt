;  Defina un procedimiento en Racket llamado attach-at-end que reciba como parámetro un valor y una
; lista y retorne la lista con los mismos valores excepto el que se pasó por parámetro que se agregará al final.

(define attach-at-end (lambda (elem ls)
                        (foldr cons (list elem) ls)
                        )
  )


(attach-at-end 'prueba '(esto es una)) ; → (esto es una prueba)