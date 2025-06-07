; Se desea crear una función que reciba como parámetro una lista de strings y devuelva una lista con las cadenas ordenadas por su peso ASCII.

(define sumaLista
  (lambda (ls)
    (if (null? ls)
        0
        (+ (car ls) (sumaLista (cdr ls))))))

(define pesoPalabra
  (lambda (palabra)
    (sumaLista (map char->integer (string->list palabra)))))

(define listaPesos
  (lambda (ls)
    (map (lambda (x y) (cons x y)) ls (map pesoPalabra ls))))

(define insertaOrdenado
  (lambda (elem ls)
    (if (null? ls)
        (list elem)
        (if (< (cdr elem) (cdar ls))
            (cons elem ls)
            (cons (car ls) (insertaOrdenado elem (cdr ls)))))))

(define ordenarAux
  (lambda (l1 l2)
    (if (null? l1)
        l2
        (ordenarAux (cdr l1) (insertaOrdenado (car l1) l2)))))

(define ordenar
  (lambda (ls)
    (ordenarAux (listaPesos ls) '())))

; Ejemplo de uso:
(ordenar '("moto" "auto" "casa" "juego" "aire"))
