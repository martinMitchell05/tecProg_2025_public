(define tabla '(("Córdoba Capital" 1500 ((07 00) (10 00) (12 00)))
                ("Carlos Paz" 1500 ((07 00) (10 30) (12 30)) )
                ("Bialet Massé" 1000 ((07 45) (10 45) (12 45)))
                ("Valle Hermoso" 1200 ((08 15) (11 15) (13 15)))
                ("La Falda" 1000 ((08 30) (11 30) (13 30)))
                ("Huerta Grande" 1200 ((08 45) (11 45) (13 45)))
                ("La Cumbre" 1600 ((09 30) (12 30) (14 30)))
                ("Capilla Del Monte" 0 ((10 00) (13 00) (15 00)))
))

(define hay_llegada (lambda (cL tbl)
                      (if (null? tbl)
                          #f
                          (if (equal? (caar tbl) cL)
                              #t
                              (hay_llegada cL (cdr tbl))
                              )
                          )
                      )
  )

(define esta_antes (lambda (cP cL tbl)
                     (if (null? tbl)
                     #f
                     (if (equal? cP (caar tbl))
                         (hay_llegada cL tbl)
                         (if (equal? cL (caar tbl))
                             #f
                             (esta_antes cP cL (cdr tbl))
                             )
                         )
                     )
                     )
  )


(define buscarDatosCiudad (lambda (cP tbl)
                          (if (null? tbl)
                              0
                              (if (equal? cP (caar tbl))
                                  (car tbl)
                                  (buscarDatosCiudad cP (cdr tbl))
                                  )
                              )
                            )
  )


(define horarios (lambda (hP lstH)
                   (if (null? lstH)
                      '()
                       (if (or (< (caar lstH) (car hP)) (and (= (caar lstH) (car hP)) (<= (cadar lstH) (cadr hP) )))
                           (horarios hP (cdr lstH))
                           (cons (car lstH) (horarios hP (cdr lstH)))
                           )
                   )
  )
  )


(define buscarSublista (lambda (cP tbl)
                        (if (null? tbl)
                            void
                            (if (equal? cP (caar tbl))
                                tbl
                                (buscarSublista cP (cdr tbl))
                                )
                            )
                        )
  )


(define calcularPrecio (lambda (cL tbl)
                         (if (equal? (caar tbl) cL)
                             0
                             (+ (cadar tbl) (calcularPrecio cL (cdr tbl)))
                             )
                         )
  )


(define ArgentinaTur (lambda (lst)
                       (if (and (= (length lst) 3) (esta_antes (car lst) (cadr lst) tabla) (= (length (caddr lst)) 2))
                           (if (null? (horarios (caddr lst) ( caddr (buscarDatosCiudad (car lst) tabla))))
                               (cons (cons (car lst) (cons (cadr lst) '())) (cons 0 (cons "NO HAY HORARIOS DE SALIDA DISPONIBLES" '()) ))
                               (cons (cons (car lst) (cons (cadr lst) '())) (cons (calcularPrecio (cadr lst) (buscarSublista (car lst) tabla)) (cons (horarios (caddr lst) ( caddr (buscarDatosCiudad (car lst) tabla)))  '()) ))

                           )
                           "Error"
                           )
                       )
  )

;Funciones validas:
;Factibles
(ArgentinaTur '("Córdoba Capital" "La Falda" (10 30)))
(ArgentinaTur '("Valle Hermoso" "La Cumbre" (09 00)))
(ArgentinaTur '("Córdoba Capital" "Capilla Del Monte" (09 00)))
;Sin horario
(ArgentinaTur '("Córdoba Capital" "La Falda" (16 00)))
;Secuencia destino-llegada no disponible
(ArgentinaTur '("La Falda" "Córdoba Capital" (10 00)))

;Funciones invalidas:
;Ciudad destino invalida
(ArgentinaTur '("Vle Hso" "La Cumbre" (09 00)))
;Ciudad llegada invalida
(ArgentinaTur '("Valle Hermoso" "La Ce" (09 00)))
;Horario invalido
(ArgentinaTur '("Valle Hermoso" "La Ce" (11)))
;Sin horarios
(ArgentinaTur '("Valle Hermoso" "La Cumbre" ()))
;Menos argumentos
(ArgentinaTur '("Valle Hermoso" (09 00)))
;Lista vacia
(ArgentinaTur '())