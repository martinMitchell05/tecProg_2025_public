#Sistema gestión concesionaria
from datetime import datetime as dt

class Persona:
    def __init__(self, nombre, telefono, dni):
        self.nombre = nombre
        self.tel = telefono
        self.dni = dni

class Vehiculo:
    def __init__(self,marca,modelo,patente,precio,kilometros):
        self.marca = marca
        self.modelo = modelo
        self.patente = patente
        self.precioVenta = precio
        self.km = kilometros
        if self.km > 0:
            self.estado = True
        else:
            self.estado = False
        self.duenio = None
    
    def que_Es(self):
        return "Vehiculo"

    def es_Usado(self):
        return self.estado
    
    def tieneDuenioRegist(self):
        if self.duenio == None:
            return False
        else:
            return True

    def registrarDuenio(self, duenio: Persona):
        if self.es_Usado():
            self.duenio = duenio
        else:
            pass


class Auto(Vehiculo):
    def __init__(self, marca, modelo, patente, precio, kilometros, origen):
        super().__init__(marca, modelo, patente, precio, kilometros)
        self.origen = origen
    
    def es_Nacional(self):
        return self.origen == "Nacional"
    
    def que_Es(self):
        return "Auto"
    

class Venta:
    def __init__(self, monto, producto, fecha: dt.date, comprador: Persona):
        self.total = monto
        self.fecha = fecha
        self.detalle = producto
        self.comprador = comprador

class Concesionaria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ventas = []

    def getTotalA_U(self):
        sum = 0
        for venta in self.ventas:
            if venta.detalle.que_Es() == "Auto" and venta.detalle.es_Usado() and venta.detalle.es_Nacional() and venta.detalle.tieneDuenioRegist():
                sum += venta.total

        return sum
    
    def agregarVenta(self, venta: Venta):
        self.ventas.append(venta)


conce = Concesionaria("Autos muy Baratos")
auto1 = Auto("Mercedes",2024,"WXZ-000",65000000,100000,"Nacional")
duenio_mercedes = Persona("roberto buendia",540800,23233332)
auto1.registrarDuenio(duenio_mercedes)
comprador = Persona("cosme fulanito",540700,33333444)

venta1 = Venta(55000000,auto1,dt.now(),comprador)
conce.agregarVenta(venta1)

auto2 = Auto("BMW",2022,"AA-123",95000000,1000000,"Nacional")
duenio_2 = Persona("roberto maldia",540900,23333452)
#auto2.registrarDuenio(duenio_2)

venta2 = Venta(95000000,auto2,dt.now(),comprador)
conce.agregarVenta(venta2)

auto3 = Auto("Fiat",2005,"XXY-321",20000000,0,"Importado")
auto3.registrarDuenio(duenio_mercedes)

venta3 = Venta(1000000,auto3,dt.now(),comprador)
conce.agregarVenta(venta3)

print(f"Ventas en autos nacionales usados: ${conce.getTotalA_U()}\n")