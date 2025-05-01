import hashlib as hs
from datetime import datetime as dt

class Persona:
    def __init__(self, nombre, fechaNac: dt.date, passw : str): #init es el constructor y self hace referencia a la propia clase, para poder usar un atr se necesita pasarle el self
        self.nombre = nombre
        self.fechaN = fechaNac
        self.edad = self._calcula_edad()
        self._password = hs.sha256(passw.encode()).hexdigest() #encoda el string en bytes, le hace el hash sha256 y lo retorna en un str con el hexdigest

    def validarPass(self, password):
        ps = hs.sha256(password.encode())
        return self._password == ps.hexdigest()
    
    def _calcula_edad(self): #el guion bajo indica que es privado
        return dt.now().year - self.fechaN.year

    def mostrar(self):
        print(self.nombre,":", self.edad,"Años\n" "Cumpleaños: ", self.fechaN.year,"-",self.fechaN.month,"-",self.fechaN.day) 

juan = Persona("juan",dt(2000,12,12),"passw")
print(f"{juan.validarPass("pass")}\n")
print(f"{juan.validarPass("Passw")}\n")
print(f"{juan.validarPass("passw")}\n")