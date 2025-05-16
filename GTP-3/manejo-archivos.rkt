(define w (open-output-file "archivo-prueba.txt" #:exists 'append)) ; si existe el archivo agrega al final lo que se agregue nuevo
(display "prueba" w)
(write-char #\space w)
(display "archivos_racket" w)
(close-output-port w)

(define subst (lambda (reemp letra lista)
                (if (null? lista)
                    '()
                    (if (equal? (car lista) reemp)
                        (cons letra (subst reemp letra (cdr lista))) ; si el elemento es igual agrega al principio de una lista la letra que reemplaza y el resto de la lista que se esta tratando
                        (cons (car lista) (subst reemp letra (cdr lista))))))) ; si no es la letra a reemplazar, agrega a una lista esa letra y la lista que resulte de llamar subst con la cola de la lista


(subst 'c 'k '( c o c o n u t))

(define w (open-output-file "archivo-prueba.txt" #:exists 'append))
(newline w)
(display (subst 'c 'k '(c o c o n u t)) w)
(close-output-port w)