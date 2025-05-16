(vector-ref #(a b c d e) 4) ; accede a la posicion 4 del vector

(let ((v (vector 'a 'b 'c 'd 'e)))
  (vector-set! v 0 'x)
  (vector-set! v 4 'x)v) ; cambia la posicion 4 de v por el simbolo x