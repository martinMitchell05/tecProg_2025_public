; Se desea crear un programa que permita convertir un lote de datos de un formato a otro. Los datos
; llegan en formato de lista de listas, donde el primer elemento determina el contenido de la lista y el
; segundo tiene la lista de datos. Los datos pueden venir en formato texto, decimal o booleano y se
; desea obtener una lista igual pero con todos sus componentes en formato decimal y todos positivos.

(define convierte_str (lambda (ls) ; convierte cada elemento de una lista de strings a numero decimal
                         (if (null? ls)
                             '()
                             (cons (string->number (car ls)) (convierte_str (cdr ls)))
                             )
                         )
                       
  )

(define convierte_bool (lambda (ls)
                          (if (null? ls)
                              '()
                              (cond
                                [(string=? (car ls) "V") (cons 1 (convierte_bool (cdr ls)))]
                                [else (cons 0 (convierte_bool (cdr ls)))]
                                )
                              )
                          )

  )


(define convdatos (lambda (lsL)
                     (if (null? lsL)
                         '()
                         (cond
                           [(string=? (caar lsL) "D") (cons (map abs (cadar lsL)) (convdatos (cdr lsL)))] ; la funcion map abs, mapea cada elemento de la sublista resultante con valor absoluto
                           [(string=? (caar lsL) "T") (cons (map abs (convierte_str (cadar lsL))) (convdatos (cdr lsL)))]
                           [(string=? (caar lsL) "B") (cons (convierte_bool (cadar lsL)) (convdatos (cdr lsL)))]
                           [else '()]
                           )
                         )
                     )
                   
  )

(convdatos '(("D" (1 2 3 -4 5)) ("T" ("6" "-7" "8")) ("B" ("V" "F"))))