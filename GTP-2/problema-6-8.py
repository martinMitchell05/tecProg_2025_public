
class Categoria:
    def __init__(self, nombre, salario):
        self.cat = nombre
        self.remu = salario

class Trabajador:
    def __init__(self, nombre: str, direccion: str, dni: int):
        self.nom_ape = nombre
        self.dir = direccion
        self.dni = dni
        self.salario = 0.0
    
    def es_tipo(self):
        return "Trabajador"
    
    def getSalario(self) -> float:
        return self.salario
    
    def categoria(self):
        return "No posee"
    
    def mostrarse(self):
        print(f"Empleado: {self.nom_ape}, Tipo: {self.es_tipo()}, Categoria: {self.categoria()}\n")
        print(f"DNI: {self.dni}, Direccion: {self.dir}\n")
        print(f"Salario: ${self.getSalario()}\n")


class Jefe(Trabajador):
    def __init__(self, nombre, direccion, dni, salario):
        super().__init__(nombre, direccion, dni)
        self.salario = salario
        self.empleados = []
    
    def agregarEmpleado(self, empleado):
        self.empleados.append(empleado)

    def listar_empleados(self):
        i = 1
        for e in self.empleados:
            print(f"{i})_") 
            e.mostrarse()
            i += 1

class Mensualizados(Trabajador):
    def __init__(self, nombre, direccion, dni, categoria: Categoria):
        super().__init__(nombre, direccion, dni)
        self.salario = categoria.remu
        self.cate = categoria.cat
        self.jefe = None
    
    def es_tipo(self):
        return "Mensualizado"
    
    def categoria(self):
        return self.cate

    def asignarJefe(self, jefe: Jefe):
        self.jefe = jefe
        jefe.agregarEmpleado(self)
    

class Jornalizados(Trabajador):
    def __init__(self, nombre, direccion, dni, precioHora, precioAdicional):
        super().__init__(nombre, direccion, dni)
        self.horas = 0.0
        self.precio_hs = precioHora
        self.adicional = precioAdicional
        self.jefe = None
    
    def sumarHoras(self, hs: float):
        self.horas += hs
    
    def es_tipo(self):
        return "Jornalizado"
    
    def getSalario(self):
        if self.horas <= 40:
            return self.horas*self.precio_hs
        else:
            return 40*self.precio_hs + self.horas%40*self.adicional
        
    def asignarJefe(self, jefe: Jefe):
        self.jefe = jefe
        jefe.agregarEmpleado(self)
    
    
class Empresa:
    def __init__(self):
        self.jefes = []
    
    def agregarJefe(self, jefe: Jefe):
        self.jefes.append(jefe)
    
    def listar_empleados_x_jefe(self, jefe: Jefe):
        if jefe in self.jefes: #busca al elemento 'jefe' dentro de la lista de jefes, si está, se ejecuta
            print(f"Jefe: {jefe.nom_ape}\n")
            jefe.listar_empleados()

categoria1 = Categoria("primera categoria",1200000)
empresa = Empresa()

jefe1 = Jefe("martin mitchell","boulevard galvez 2302",46371805,2000000)
print(f"Salario de jefe {jefe1.dni}: ${jefe1.getSalario()}\n")
empresa.agregarJefe(jefe1)

men1 = Mensualizados("marina perez","san jeronimo 1700",42222343,categoria1)
men1.asignarJefe(jefe1)

jor1 = Jornalizados("juan perez","boulevard galvez 2100",12345678,7000,8500)
jor1.asignarJefe(jefe1)
#jor1.sumarHoras(2.5)
jor1.sumarHoras(4)
jor1.sumarHoras(37)

jefe2 = Jefe("linus torvalds", "linux 123", 12312312, 15000000)
empresa.agregarJefe(jefe2)
print(f"Salario de jefe {jefe2.dni}: ${jefe2.getSalario()}\n")

men2 = Mensualizados("guadalupe mai","san jeronimo 1600",42322343,categoria1)
men2.asignarJefe(jefe2)

jor2 = Jornalizados("manuela piedrabuena","Catamarca 1980",12345679,9000,10500)
jor2.asignarJefe(jefe2)
jor2.sumarHoras(2.5)
jor2.sumarHoras(4)
jor2.sumarHoras(37)

empresa.listar_empleados_x_jefe(jefe1)
empresa.listar_empleados_x_jefe(jefe2)
