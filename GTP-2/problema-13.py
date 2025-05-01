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


class Contador_Piezas(ABC):
    @abstractmethod
    def contar_piezas(self):
        pass

class Contador_Piezas_Cel(Contador_Piezas):
    def contar_piezas(self):
        return "Piezas requeridas para reparar el celular\n"

class Contador_Piezas_Tab(Contador_Piezas):
    def contar_piezas(self):
        return "Piezas requeridas para reparar la tablet\n"
    
class Contador_Piezas_Watch(Contador_Piezas):
    def contar_piezas(self):
        return "Piezas requeridas para reparar el smartwatch\n"
    

class Dispositivo:
    def __init__(self, marca: str, modelo: str, pantalla: bool, cont_piezas: Contador_Piezas):
        self.marca = marca
        self.modelo = modelo
        self.pantalla = pantalla
        self.cont = cont_piezas

    def contar_piezas(self):
        return self.cont.contar_piezas()


class Celular(Dispositivo):
    def __init__(self, marca: str, modelo: str, pantalla: bool, contador):
        super().__init__(marca, modelo, pantalla, contador)
        

class Tablet(Dispositivo):
    def __init__(self, marca: str, modelo: str, pantalla: bool, lapiz: bool, contador):
        super().__init__(marca, modelo, pantalla, contador)
        self.lapiz = lapiz
        

class Smartwatch(Dispositivo):
    def __init__(self, marca: str, modelo: str, pantalla: bool, gps: bool, contador):
        super().__init__(marca, modelo, pantalla, contador)
        self.gps = gps
        


# Ejemplo de uso
dispositivos = [
    Celular("Samsung", "Galaxy S20", True, Contador_Piezas_Cel()),
    Tablet("Apple", "iPad Pro", True, True, Contador_Piezas_Tab()),
    Smartwatch("Apple", "Watch Series 6", True, True, Contador_Piezas_Watch())
]

for d in dispositivos:
    print(d.contar_piezas())

# Principle that was vulnerated: 1. LSP - 2. OCP 


### FINISH ###
class IUsuario(ABC):
    @abstractmethod
    def solicitar_prestamo_libro(self):
        pass

    @abstractmethod
    def devolver_libro(self):
        pass

    @abstractmethod
    def buscar_libro(self):
        pass

    @abstractmethod
    def solicitar_reserva_sala_estudio(self):
        pass

class Estudiante(IUsuario):
    def solicitar_prestamo_libro(self):
        print("Estudiante solicitando préstamo de libro.")

    def devolver_libro(self):
        print("Estudiante devolviendo libro.")

    def buscar_libro(self):
        print("Estudiante buscando libro en el catálogo.")

    def solicitar_reserva_sala_estudio(self):
        raise NotImplementedError("Los estudiantes no pueden reservar salas de estudio.")

class Profesor(IUsuario):
    def solicitar_prestamo_libro(self):
        print("Profesor solicitando préstamo de libro.")

    def devolver_libro(self):
        print("Profesor devolviendo libro.")

    def buscar_libro(self):
        print("Profesor buscando libro en el catálogo.")

    def solicitar_reserva_sala_estudio(self):
        print("Profesor solicitando reserva de sala de estudio.")

# Ejemplo de uso
estudiante = Estudiante()
profesor = Profesor()

estudiante.solicitar_prestamo_libro()
estudiante.devolver_libro()
estudiante.buscar_libro()

profesor.solicitar_prestamo_libro()
profesor.devolver_libro()
profesor.buscar_libro()
profesor.solicitar_reserva_sala_estudio()


# Principle that was vulnerated: 1. 