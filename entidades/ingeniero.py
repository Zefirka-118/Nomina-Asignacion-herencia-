from entidades.empleado import Empleado
from entidades.enums import Area

class Ingeniero(Empleado):
    def __init__(self, nombre, dias, racha_asistencia, salario_i, documentacion):
        self.nombre = nombre
        self.area = Area.INGENIERIA      
        self.dias = dias
        self.racha_asistencia = racha_asistencia
        self.salario_base = salario_i
        self.documentacion = documentacion
        self.proyectos = 0

    def agregar_proyecto(self):
        self.proyectos = self.proyectos + 1

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Area: {self.area.value}")
        print(f"Dias trabajados: {self.dias}")
        print(f"Racha de asistencia: {self.racha_asistencia}")
        print(f"Salario base: ${self.salario_base}")
        print(f"Documentacion: {self.documentacion}")
        print(f"Proyectos: {self.proyectos}")
        print(f"Salario total: ${self.calcular_salario()}")
        print("-" * 30)