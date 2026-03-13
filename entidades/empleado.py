from entidades.enums import Bono, Area   

class Empleado:
    def __init__(self, nombre, area, dias, racha_asistencia):
        self.nombre = nombre
        self.area = area
        self.dias = dias
        self.racha_asistencia = racha_asistencia
        self.salario_base = 0

    def calcular_bono(self):
        if self.racha_asistencia > 6: #si la racha es mayor a 6 DIAS DE JALE SE DA EL BONO
            # Comparamos con los nombres en mayúsculas del Enum
            if self.area == Area.PRODUCCION:
                return self.salario_base * Bono.PRODUCTOR.value
            elif self.area == Area.INGENIERIA:
                return self.salario_base * Bono.INGENIERO.value
            elif self.area == Area.SUPERVISION:
                return self.salario_base * Bono.SUPERVISOR.value
        return 0

    def calcular_salario(self):
        salario_diario = self.salario_base / 30
        salario_total = (salario_diario * self.dias) + self.calcular_bono()
        return salario_total

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Area: {self.area.value}")
        print(f"Dias trabajados: {self.dias}")
        print(f"Racha de asistencia: {self.racha_asistencia}")
        print(f"Salario base: ${self.salario_base}")
        print(f"Salario total: ${self.calcular_salario()}")