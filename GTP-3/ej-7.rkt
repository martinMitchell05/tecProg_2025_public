
; Usando length, defina el procedimiento mascorta, que retorna la lista
; más corta de los dos argumentos pasados o la primera lista si tienen el mismo largo.

(define mascorta
         (lambda (l1 l2) ; necesario para poder trabajar las listas que se le pasen despues
           (if (<= (length l1) (length l2)) ;length es una funcion entonces l1 y l2 son los argumentos que se le pasan
               l1
               l2)))

(mascorta '(a b) '(c d e))
(mascorta '(a) '(b c d))
(mascorta '(a b) '(c))