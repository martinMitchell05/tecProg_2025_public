;(+ (/ (* 7 a) b) (/ (* 3 a) b) (/ (* 7 a) b))

;[7*a/b + 3*a/b + 7*a/b]

(define a 1)
(define b 5)

(let ((t1 (/ (* 7 a) b))
  (t2 (/ (* 3 a) b))
  (t3 (/ (* 7 a) b)))
  (+ t1 t2 t3))

;(cons (car (list a b c)) (cdr (list a b c)))

(define c 10)

(let ((l1 (list a b c)))
  (cons (car l1) (cdr l1)))