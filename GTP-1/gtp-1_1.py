### ejercicio 1: Calculadora de Edad

#nacimiento = int(input("Introduce tu año de nacimiento: "))
#actual = int(input("Introduce el año actual: "))

#edad = actual - nacimiento

#print("Tu edad es: ", edad)

### ejercicio 2: Conversión de segundos

#segundos = int(input("Introduce el numero en segundos: "))

#hora = int(segundos/3600)
#minutos = int((segundos%3600)/60)
#segundos =  int(segundos%60)

#print("La hora es:", hora, "hs", minutos, "min", segundos, "seg")

### ejercicio 3: Calculadora de Raices Cuadradas

import math

#numero = float(input("Introduce un numero: "))

#while (numero > 0):

    #raiz = math.sqrt(numero)

    #print("Tu raiz es: ", raiz)

    #numero = float(input("Introduce un numero: "))

#print("La raiz no existe")


### ejercicio 4: Calculo del IMC

#peso = float(input("Introduce tu peso en kg: "))
#altura = float(input("Introduce tu altura en metros: "))

#imc = peso/(altura*altura)

#if imc>=40:
    #print("Obesidad tipo III")
#elif imc>=30:
    #print("Obesidad")
#elif imc>=25:
    #print("Sobrepeso")
#elif imc>=18.5:
    #print("Normal")
#else:
    #print("Insuficiente")

### ejercicio 5: Conversion de Unidades

#celsius = float(input("Introduce la temperatura en Celsius: "))

#farenheit = (celsius*9/5)+32

#print("La temperatura en Farenheit es: ", farenheit, "°F")


### ejercicio 6: Calculo de Distancia de Viaje

#velProm = float(input("Introduce la velocidad promedio en km/h: "))
#tiempoTot = float(input("Introduce el tiempo total del viaje en h: "))

#distancia = velProm*tiempoTot

#print("La distancia recorrida es: ", distancia, "km")


### ejercicio 7: Presupuesto de viaje

#costoDia = float(input("Introduce el costo de alquiler por dia: "))
#numDias = int(input("Introduce el total de dias: "))
#presupCombustible = float(input("Introduce el presupuesto en combustible: "))

#total = float((costoDia*numDias) + presupCombustible)

#print("El costo total es $", total)

### ejercicio 8: Volumen de cilindro

r = float(input("Introduce el radio en m: "))
h = float(input("Introduce altura en m: "))

vol = math.pi*math.pow(r,2)*h

print("El volumen del cilindro es: ", vol, "m^3")