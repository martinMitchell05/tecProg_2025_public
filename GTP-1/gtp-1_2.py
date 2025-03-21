### ejercicio 1: Conteo hasta N

#n = int(input("Introduce un numero: "))

#for x in range(1,n+1):
#    print(x)


### ejercicio 2: Suma de Numeros

#n = int(input("Cuantos numeros a sumar? "))

#suma = 0

#for x in range(0,n):
  #  x = int(input("Introduce un numero: "))
 #   suma += x

#print("Suma total: ", suma)


### ejercicio 3: Media de Numeros

#n = int(input("Cuantos numeros para promediar? "))
#suma = 0

#for i in range(0,n):
 #   i = float(input("Numero: "))
  #  suma += i

#print("Promedio: ", float(suma/n))


### ejercicio 4: Encontrar el Maximo

#n = int(input("Cuantos numeros? "))
#max = 0

#for i in range(0,n):
 #   i = float(input("Numero: "))

  #  if max < i:
   #     max = i

#print("El numero maximo es: ", max)


### ejercicio 5: Tabla de Multiplicar

#n = int(input("Introduce un numero para generar su tabla: "))

#i = 0
#while i <= 10:
    #print(n,"x", i, "=", n*i)

    #i += 1


### ejercicio 6: Suma de numeros pares

#n = int(input("Introduce un numero: "))
#suma = 0

#i = 2
#while i <= n:
  #  suma += i
 #   i = i+2

#print("La suma de pares es: ", suma)


### ejercicio 7: Contador de Digitos

#n = int(input("Introduce un numero entero: "))

#digits = [int(d) for d in str(n)] #hace todo junto el proceso de convertir e insertar en una posicion de la lista cada digito del numero ingresado

#print("La cantidad de digitos es ", len(digits))


### ejercicio 8: Conversión Binaria

n = int(input("Introduce un numero decimal: "))

binario = []
resto = n%2
q = int(n/2)

binario.append(resto)

while q > 0:

    resto = q%2
    q = int(q/2)

    binario.append(resto)

binario.reverse()
representacion = int("".join(str(d) for d in binario)) #primero con el join concatena cada posicion de la lista y luego a esa concatenacion la convierte en un numero entero

print("El numero en binario es: ", representacion)

