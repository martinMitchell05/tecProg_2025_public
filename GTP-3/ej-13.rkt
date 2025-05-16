; Se desea crear un función que reciba como parámetros una lista de átomos compuesto únicamente
; de letras y devuelva una lista agrupando los que son iguales en sublistas.


(define agrupar (lambda ls
                  (if (null? ls)
                      '()
                      (cons (agrupar_sublista (car ls) (cdr ls)) '())
                      )
                  )
  )


(agrupar '(A A B C A B A D C)) ;→ ((AAAA) (BB) (CC) (D)) 