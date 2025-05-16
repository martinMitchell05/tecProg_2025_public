;((lambda (r) (* pi r r))3) ; calculo del area de una circunferencia mediante funcion anonima

;(define (area radio) (* pi radio radio)) ; calculo del area ahora definiendo una función con nombre y parametro

;(area 3)

(define area (lambda (r) (* pi r r))) ; combinacion de ambas maneras para definir a una funcion

(area 3)

;(cadr '('(1 2) '(3 4))) ; mezcla entre car y cdr

