;+ --> indica que es una primitiva, un procedimiento

;'+ --> imprime el SIMBOLO

;'(a b c d)

;(car '(a b c)) ; car := primer elemento de la lista

;(cdr '(a b c)) ; cdr := accedo a la cola de la lista

(+ 1 (/ 3 (+ 2 (/ 1 (+ 5 0.5)))))

(+ 7 (* 2 (/ -1 3)) (/ (* -10.7 (* (/ 7 3) (/ 5 9))) (- (/ 5 8) (/ 2 3))))

(* 1 -2 3 -4 5 -6 7)

;(define cuadrado
  ;(lambda (n)
 ;   (* n n))) ; convendria ir tabeando segun parentesis para no tener un choclo

(cons 'car '+) ; inserta el primer elemento, dentro del segundo (que será una lista)
; la anterior es una lista impropia, porque esta separada por .
; son utilizadas con dos elementos, pero pueden haber mas de dos

; ejemplo
;(cons 'x 'y) ; lista impropia

;(cons 'a '(b c)) ; esto devuelve una lista propia

; si yo lo primero que le paso es una lista y lo segundo un elemento, me devuelve una lista impropia
(cons '(a b) 'c)

(list 'esto '(es muy facil)) ; retorna una lista de listas de simbolos

(cons 'esto '(es muy facil)) ; retorna una lista de simbolos
