
; Defina una función distance2d que reciba como parámetros dos puntos en el plano y devuelva su
; distancia. Utilice una lista impropia para la declaración de x e y.

(define difx
  (lambda (p1 p2)
    (- (car p2) (car p1))))

(define dify
  (lambda (p1 p2)
    (- (cdr p2) (cdr p1))))


(define distance2d
  (lambda (p1 p2)
    (let ((dif1 (* (difx p1 p2) (difx p1 p2)))
          (dif2 (* (dify p1 p2) (dify p1 p2))))
      (sqrt (+ dif1 dif2)))))

(distance2d '(1 . 1) '(2 . 2))
