; Cree una función llamada fullreverse-list que permite revertir completamente el contenido de una lista.

(define invertir-list (lambda (ls-in ls-out)
                        (if (null? ls-in)
                            ls-out
                            (invertir-list (cdr ls-in) (cons (car ls-in) ls-out))
                            )
                        )
  )
  


(define fullreverse-list (lambda (ls-in ls-out)
                           (if (null? ls-in)
                               '()
                               (if (list? (car ls-in))
                                   (cons (invertir-list (car ls-in) (cdr ls-in)) ls-out)
                                   (fullreverse-list (cdr ls-in) (cons (car ls-in) ls-out))
                                   )
                               )
                           )
  )


(fullreverse-list '(1 (2 3 4 (4 5) (3 (5 6)) 4)) '()) ;→ ((4 ((6 5) 3) (5 4) 4 3 2) 1)


;(define (deep-reverse ls)
  ;(define (invertir-list ls-in ls-out)
    ;(if (null? ls-in)
   ;     ls-out
  ;      (invertir-list (cdr ls-in) (cons (car ls-in) ls-out))))
  
 ; (define (aux ls)
    ;(cond
      ;[(null? ls) '()]
     ; [(list? (car ls))
    ;   (cons (aux (car ls)) (aux (cdr ls)))]
   ;   [else (cons (car ls) (aux (cdr ls)))]))

  ;(invertir-list
   ;(map (lambda (x)
    ;      (if (list? x)
   ;           (deep-reverse x)
  ;            x))
 ;       ls)
;   '())