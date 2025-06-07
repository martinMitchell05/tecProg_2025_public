; Defina en Racket un procedimiento recursivo que encuentre el primer elemento de una lista que es
; un número. Debe retornar el número si lo encuentra, sino retornar null.

(define primer-num (lambda (ls)
                     (if (null? ls)
                         null
                         (if (number? (car ls))
                             (car ls)
                             (primer-num (cdr ls))
                             )
                         )
                     )
  )
                     
(primer-num '((1 . 2) 'a (b) (5) (6 8) '(a 9))) ; --> null