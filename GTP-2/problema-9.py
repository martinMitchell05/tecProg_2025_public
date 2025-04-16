from typing import List
from datetime import datetime as dt

class Carrera:
    def __init__(self):
        self.c_alumnos: List[Alumno] = []

    # Este método cuenta la cantidad de egresados de la carrera
    # y muestra el promedio de cada uno de ellos (Sin desaprobados)
    def listar_egresados(self) -> int:
        cant_egresados = 0
        # Recorro todos los alumnos de la CARRERA
        iter_alumnos = iter(self.c_alumnos)
        alumno = next(iter_alumnos, None)
        while alumno is not None:
            f_egreso = alumno.fecha_egreso #tiene que llamar a un metodo
            if f_egreso is not None:
                cant_egresados += 1
                ###llamada a metodo de Alumno
                print(alumno.getPromedio())

            alumno = next(iter_alumnos, None)
        return cant_egresados
        

class Examen:
    def __init__(self, nota: float):
        self.nota = nota

class Alumno:
    def __init__(self, nombre: str, fecha_egreso: dt, examenes: List['Examen']):
        self.nombre = nombre
        self.fecha_egreso = fecha_egreso
        self.examenes = examenes
        self.promedio = 0.0

    def getPromedio(self):

        self.promedio_final()

        return f"Alumno: {self.nombre} - Promedio: {self.promedio:.2f}"

    def promedio_final(self):
        # Recorro todas las NOTAS de los ALUMNOS
        acumula_notas = 0
        cant_examenes_aprobados = 0
        for examen in self.examenes:
            if examen.nota >= 6: #tiene que llamar a un metodo
                acumula_notas += examen.nota
                cant_examenes_aprobados += 1
        
        self.promedio = acumula_notas / cant_examenes_aprobados

    
           


# Ejemplo de uso
if __name__ == "__main__":
    alumno1 = Alumno("Juan", dt.now(), [Examen(7), Examen(8), Examen(5)])
    alumno2 = Alumno("María", dt.now(), [Examen(6), Examen(7), Examen(6)])
    carrera = Carrera()
    carrera.c_alumnos = [alumno1, alumno2]
    egresados_final = carrera.listar_egresados()
    print(f"Cantidad total de egresados: {egresados_final}\n")
