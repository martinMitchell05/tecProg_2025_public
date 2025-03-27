from datetime import datetime as dt


class Inscripcion:
    def __init__(self, fecha: dt.date):
        self.fecha = fecha
    
    def getFecha(self):
        return self.fecha

class Alumno:
    def __init__(self, n: str, dni: int, fechaNac: dt.date):
        self.nombre = n
        self.dni = dni
        self.fechaN = fechaNac

    def mostrarse(self):
        return f"{self.nombre} / {self.dni} / {self.calcularEdad()} Años\n"

    def calcularEdad(self):
        return dt.now().year - self.fechaN.year        
    

class Carrera:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.alumnos = []

    def getNombre(self):
        return self.nombre

    def inscribirAlumno(self, alumno: Alumno, fecha: dt.date):
        self.alumnos.append((alumno, Inscripcion(fecha)))

    def mostrarAlumnos(self):
        for a in self.alumnos:
            print(f"{a[0].mostrarse()}Inscripcion: {a[1].getFecha()}\n")

class Facultad:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.carreras = []

    def crearCarrera(self, carrera: Carrera):
        self.carreras.append(carrera)

    def mostrarCarrerasyAlumnos(self):
        for c in self.carreras:
            print(self.nombre)
            print(f"{c.getNombre()}\n")
            c.mostrarAlumnos()
    



def main():
    fac = Facultad("FICH")
    c1 = Carrera("Ingeniería en Informática")
    fac.crearCarrera(c1)

    a1 = Alumno("martin",46371805,dt(2005,1,3))
    c1.inscribirAlumno(a1,dt.now())

    a2 = Alumno("emanuel", 45057139, dt(2003,8,21))
    c1.inscribirAlumno(a2,dt.now())

    fac.mostrarCarrerasyAlumnos()


if __name__ == "__main__":
    main()