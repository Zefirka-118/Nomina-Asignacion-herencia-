from entidades.empleado import Empleado
from entidades.enums import Area

class Productor(Empleado):
    def __init__(self, nombre, dias, racha_asistencia, salario_p):
        self.nombre = nombre
        self.area = Area.PRODUCCION      
        self.dias = dias
        self.racha_asistencia = racha_asistencia
        self.salario_base = salario_p
        self.unidades = 0

    def registrar_unidades(self, cantidad):
        self.unidades = cantidad

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Area: {self.area.value}")
        print(f"Dias trabajados: {self.dias}")
        print(f"Racha de asistencia: {self.racha_asistencia}")
        print(f"Salario base: ${self.salario_base}")
        print(f"Unidades producidas: {self.unidades}")
        print(f"Salario total: ${self.calcular_salario()}")
        print("-" * 30)