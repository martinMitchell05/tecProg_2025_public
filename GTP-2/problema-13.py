# Modifica los siguientes fragmentos de código de manera de que cumplir con los principios SOLID. 
# Explicitar qué principio se viola en cada caso (salvo en el de Correo Electrónico)

class Empleado:
    def __init__(self, nombre, horas_trabajadas, tarifa_por_hora):
        self._nombre = nombre
        self._horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora
        self._reporte = None

    def getNom(self):
        return self._nombre
    
    def getReporte(self):
        return self._reporte

    def calcular_salario(self):
        return self._horas_trabajadas * self.tarifa_por_hora

# separates the responsibility of Empleado class
class Reporte:
    def __init__(self, emp: Empleado):
        # Código para generar el reporte de desempeño

        print(f"Reporte generado para empleado: {emp.getNom()}\n")

# Principle that was vulnerated 1. SRP - 2. OCP


from abc import ABC, abstractmethod

class Notificador(ABC): #--> this should be an interface, so
    @abstractmethod
    def enviar_notificacion(self, destinatario: str, mensaje: str):
        pass

class CorreoElectronico(Notificador):
    def enviar_notificacion(self, destinatario: str, mensaje: str):
        # Lógica para enviar notificación por correo electrónico
        print(f"Correo electrónico enviado a {destinatario}: {mensaje}\n")

# Uso del código actual
correo_electronico = CorreoElectronico()
correo_electronico.enviar_notificacion("usuario@example.com", "¡Tu tarea está lista!")

# Principle that was vulnerated: -

### FINISH ###
class DesctoCat(ABC): # apply the OCP splitting up the behaviour
    @abstractmethod
    def aplicar_descuento(self, nombre: str):
        pass

class DescuentoAlimentos(DesctoCat):
    def aplicar_descuento(self, nombre: str):
        print(f"Descuento del 10% en {nombre}\n")

class DescuentoLimpieza(DesctoCat):
    def aplicar_descuento(self, nombre: str):
        print(f"Descuento del 5% en {nombre}\n")


class Producto:
    def __init__(self, nombre: str, categoria: DesctoCat):
        self._nombre = nombre
        self._categoria = categoria

    def aplicar_descuento(self):
        self._categoria.aplicar_descuento(self._nombre)    

class Carrito:
    def __init__(self, productos: list):
        self._productos = productos

    def calcular_descuentos(self):
        for producto in self._productos:
            
            producto.aplicar_descuento()


productos = [
    Producto('manzanas', DescuentoAlimentos()),
    Producto('jabón', DescuentoLimpieza())
]

carrito = Carrito(productos)
carrito.calcular_descuentos()

# Principle that was vulnerated: 1. Demeter - 2. TDA - 3. SRP - 4. OCP