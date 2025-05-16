
; Escriba una función que cuente la cantidad de apariciones de un elemento en una lista. El primer
; parámetro será el elemento a buscar y el segundo la lista en la que se debe buscar.

(define count-elem (lambda (n lista)
                      (if (null? lista)
                          0
                          (if (equal? n (car lista))
                              (+ (count-elem n (cdr lista)) 1)
                              (count-elem n (cdr lista))))))


(count-elem 3 '(1 2 3 4 5 4 3 2 1 ))