; Utilizando la función MAP cree una función llamada fullreverse-list que permite revertir completamente el contenido de una lista.

(define (fullreverse-list lst)
  (cond
    [(null? lst) '()] ; caso base: lista vacía
    [(list? lst)
     (map fullreverse-list (reverse lst))] ; reversa la lista y recursivamente aplica la función a cada elemento
    [else lst])) ; si no es lista, simplemente lo retorna (caso atómico)


(fullreverse-list '(1 2 (4 3) (5 6 7 (9 8))))