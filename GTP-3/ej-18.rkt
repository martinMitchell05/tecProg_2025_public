; Definir una estructura que represente un punto en el plano. Crear una función que calcule la distancia
; entre dos puntos dados recibiendo como parámetros la estructura de cada uno.

; definir una funcion que arme una lista impropia con los valores x e y del punto

(define punto (lambda (x y)
                (cons x y)
                )
  )

(define difx
  (lambda (p1 p2)
    (- (car p2) (car p1))))

(define dify
  (lambda (p1 p2)
    (- (cdr p2) (cdr p1))))


(define distance2d
  (lambda (p1 p2)
    (let ((dif1 (* (difx p1 p2) (difx p1 p2))) (dif2 (* (dify p1 p2) (dify p1 p2))))
      (sqrt (+ dif1 dif2))
      )
    )
  )

(define p1 (punto 1 1))
(define p2 (punto 2 2))

(distance2d p1 p2)