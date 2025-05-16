
; Defina un procedimiento subst que reciba tres parámetros (dos valores y una lista) y devuelva la
; lista con todos los componentes que son iguales al primer parámetro reemplazados por el valor del
; segundo parámetro.

(define subst (lambda (reemp letra lista)
                (if (null? lista)
                    '()
                    (if (equal? (car lista) reemp)
                        (cons letra (subst reemp letra (cdr lista))) ; si el elemento es igual agrega al principio de una lista la letra que reemplaza y el resto de la lista que se esta tratando
                        (cons (car lista) (subst reemp letra (cdr lista))))))) ; si no es la letra a reemplazar, agrega a una lista esa letra y la lista que resulte de llamar subst con la cola de la lista


(subst 'c 'k '( c o c o n u t))