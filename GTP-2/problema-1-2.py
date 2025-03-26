from datetime import datetime as dt

class Persona:
    def __init__(self, nombre, fechaNac: dt.date): #init es el constructor y self hace referencia a la propia clase, para poder usar un atr se necesita pasarle el self
        self.nombre = nombre
        self.fechaN = fechaNac
        self.edad = self._calcula_edad()
    
    def _calcula_edad(self): #el guion bajo indica que es privado
        return dt.now().year - self.fechaN.year

    def mostrar(self):
        print(self.nombre,":", self.edad,"Años\n" "Cumpleaños: ", self.fechaN.year,"-",self.fechaN.month,"-",self.fechaN.day) 

class Principal:
    def __init__(self):
        pass

    def ejecutar(self):
        p1 = Persona("Martin", dt(2005,1,3))
        #print("ID persona 1:", id(p1))
        p1.mostrar()

        #if p1 is p2: compara las referencias en memoria si son iguales
         #   print("los objetos son iguales")
        #else:
         #   print("no son iguales")

if __name__ == "__main__": #ejecuta automaticamente cuando incia el .py (la funcion main)
    principal = Principal()
    principal.ejecutar()