# Modifica los siguientes fragmentos de código de manera de que cumplir con los principios SOLID. 
# Explicitar qué principio se viola en cada caso (salvo en el de Correo Electrónico)

class Empleado:
    def __init__(self, nombre, horas_trabajadas, tarifa_por_hora):
        self.nombre = nombre
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora

    def calcular_salario(self):
        return self.horas_trabajadas * self.tarifa_por_hora

    def generar_reporte_desempenio(self):
        self.reporte = Reporte(self)

    def getReporteDesempenio(self):
        return self.reporte

class Reporte: #--> should be an interface??
    def __init__(self, emp: Empleado):
        # Código para generar el reporte de desempeño
        pass

# Principle that was vulnerated 1. SRP - 2. OCP


from abc import ABC, abstractmethod

class Notificador(ABC): #--> this should be an interface, so
    @abstractmethod
    def enviar_notificacion(self, destinatario: str, mensaje: str):
        pass

class CorreoElectronico(Notificador):
    def enviar_notificacion(self, destinatario: str, mensaje: str):
        # Lógica para enviar notificación por correo electrónico
        print(f"Correo electrónico enviado a {destinatario}: {mensaje}")

# Uso del código actual
correo_electronico = CorreoElectronico()
notificador = Notificador(correo_electronico)
notificador.enviar_notificacion("usuario@example.com", "¡Tu tarea está lista!")

# Usage after changes
correo_electronico = CorreoElectronico()
correo_electronico.enviar_notificacion("user@example.com","Your homework is ready!")

# Principle that was vulnerated: 1. Demeter - 2. OCP - 3. SRP

### FINISH ###
class Producto:
    def __init__(self, nombre: str, categoria: str):
        self.nombre = nombre
        self.categoria = categoria

class Carrito:
    def __init__(self, productos: list):
        self.productos = productos

def calcular_descuento(productos: list):
    for producto in productos:
        if producto.categoria == 'alimentos':
            print(f"Descuento del 10% en {producto.nombre}")
        elif producto.categoria == 'limpieza':
            print(f"Descuento del 5% en {producto.nombre}")
        # Añadir más condiciones para nuevos tipos de productos y descuentos

productos = [
    Producto('manzanas', 'alimentos'),
    Producto('jabón', 'limpieza')
]

carrito = Carrito(productos)
calcular_descuento(carrito.productos)

# Principle that was vulnerated: 