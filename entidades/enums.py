from enum import Enum

class Bono(Enum):
    PRODUCTOR = 0.5
    INGENIERO = 1.5
    SUPERVISOR = 2.0

class Area(Enum):
    PRODUCCION = "Producción"
    INGENIERIA = "Ingeniería"
    SUPERVISION = "Supervisión"