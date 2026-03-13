from entidades.productor import Productor
from entidades.ingeniero import Ingeniero
from entidades.supervisor import Supervisor

try:
    # Productor
    print("--- Datos del Productor ---")
    nombre_p: str = input("Nombre: ")
    dias_p: int = int(input("Dias trabajados: "))
    racha_p: int = int(input("Racha de asistencia: "))
    salario_p: float = float(input("Salario base: "))
    unidades_p: int = int(input("Unidades producidas: "))

    productor = Productor(nombre_p, dias_p, racha_p, salario_p)
    productor.registrar_unidades(unidades_p)

    # Ingeniero
    print("\n--- Datos del Ingeniero ---")
    nombre_i: str = input("Nombre: ")
    dias_i: int = int(input("Dias trabajados: "))
    racha_i: int = int(input("Racha de asistencia: "))
    salario_i: float = float(input("Salario base: "))
    documentacion_i: str = input("Documentacion a cargo: ")
    proyectos_i: int = int(input("Cuantos proyectos ha completado?: "))

    ingeniero = Ingeniero(nombre_i, dias_i, racha_i, salario_i, documentacion_i)
    contador = 0
    while contador < proyectos_i:
        ingeniero.agregar_proyecto()
        contador = contador + 1

    # Supervisor
    print("\n--- Datos del Supervisor ---")
    nombre_s: str = input("Nombre: ")
    dias_s: int = int(input("Dias trabajados: "))
    racha_s: int = int(input("Racha de asistencia: "))
    salario_s: float = float(input("Salario base: "))
    reporte_s: str = input("Reporte a cargo: ")
    empleados_cargo_s: int = int(input("Cuantos empleados tiene a cargo?: "))

    supervisor = Supervisor(nombre_s, dias_s, racha_s, salario_s, reporte_s)
    contador2 = 0
    while contador2 < empleados_cargo_s:
        supervisor.agregar_empleado()
        contador2 = contador2 + 1

    # Mostrar
    print("\n______________________")
    print("Nominas de empleadores")
    print("______________________")

    print("\n--- Productor ---")
    productor.mostrar_info()
    print("--- Ingeniero ---")
    ingeniero.mostrar_info()
    print("--- Supervisor ---")
    supervisor.mostrar_info()

except ValueError:
    print("Error: Ingresaste un valor no valido (se esperaba un numero).")