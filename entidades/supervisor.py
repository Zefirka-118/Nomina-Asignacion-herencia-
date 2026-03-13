from entidades.empleado import Empleado
from entidades.enums import Area

class Supervisor(Empleado):
    def __init__(self, nombre, dias, racha_asistencia, salario_su, reporte):
        self.nombre = nombre
        self.area = Area.SUPERVISION     
        self.dias = dias
        self.racha_asistencia = racha_asistencia
        self.salario_base = salario_su
        self.reporte = reporte
        self.empleados_cargo = 0

    def agregar_empleado(self):
        self.empleados_cargo = self.empleados_cargo + 1

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Area: {self.area.value}")
        print(f"Dias trabajados: {self.dias}")
        print(f"Racha de asistencia: {self.racha_asistencia}")
        print(f"Salario base: ${self.salario_base}")
        print(f"Reporte: {self.reporte}")
        print(f"Empleados a cargo: {self.empleados_cargo}")
        print(f"Salario total: ${self.calcular_salario()}")
        print("-" * 30)