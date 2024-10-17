Salario_Base_Mensual1 = 3000000
Cargo_empleado1 = "directivo"
Nivel_desempeño1 = "alto"

Salario_Base_Mensual2 = 2500000
Cargo_empleado2 = "DIRECTIVO"
Nivel_desempeño2 = "Medio"

Salario_Base_Mensual3 = 1300000
Cargo_empleado3 = "Auxiliar"
Nivel_desempeño3 = "Bajo"

Salario_Base_Mensual4 = 1750000
Cargo_empleado4 = "Operativo"
Nivel_desempeño4 = "MEDIO"



def calcular_bonificacion(Salario_Base_Mensual, Cargo_empleado, Nivel_desempeño):
    # Definimos las tasas de bonificación de los empleados
    if Salario_Base_Mensual == 1:
        salario_base = Salario_Base_Mensual1
        Cargo_empleado1 = "directivo"
        Nivel_desempeño1 = "alto"
    elif Salario_Base_Mensual == 2:
        salario_base = Salario_Base_Mensual2
        Nivel_desempeño2 = "Medio"
    elif Salario_Base_Mensual == 3:
        salario_base = Salario_Base_Mensual3
        Nivel_desempeño3 = "Bajo"
    elif Salario_Base_Mensual == 4:
        salario_base = Salario_Base_Mensual4
        Nivel_desempeño4 = "MEDIO"
    else:
        return None #Tipo de salario invalido




Salario_Base_Mensual = [
    {'nombre': 'Empleado 1', 'salario_base': 3000000, 'cargo_empleado': 'directivo', 'desempeño': 'alto'},
    {'nombre': 'Empleado 2', 'salario_base': 2500000, 'cargo_empleaado': 'directivo', 'desempeño': 'medio'},
    {'nombre': 'Empleado 3', 'salario_base': 1300000, 'cargo_empleado': 'auxiliar', 'desempeño': 'bajo'},
    {'nombre': 'Empleado 4', 'salario_base': 1750000, 'cargo_empleado': 'operativo', 'desempeño': 'medio'}
]

# Proceso y salida
for Salario_Base_Mensual1 in Salario_Base_Mensual:
    salario_base = Salario_Base_Mensual['salario_base']
    cargo = Salario_Base_Mensual['cargo']
    desempeño = Salario_Base_Mensual['desempeño']

    # Verificar que el cargo esté en las tasas definidas
    if cargo in ['directivo', 'operativo']:
        bonificacion, total = calcular_bonificacion(salario_base, cargo, desempeño)
        print(f"-----Resumen del Pago-----")
        print(f"Cargo: {cargo.capitalize()}")
        print(f"Nivel de Desempeño: {desempeño.capitalize()}")
        print(f"Salario Base: ${salario_base}")
        print(f"Bonificación: ${bonificacion}")
        print(f"Total a Recibir: ${total}")
        print("-----------------------------------------")
    else:
        print(f"-----Resumen del Pago-----")
        print(f"Cargo: {cargo.capitalize()}")
        print(f"Nivel de Desempeño: {desempeño.capitalize()}")
        print(f"Salario Base: ${salario_base}")
        print(f"Bonificación: $0")
        print(f"Total a Recibir: ${salario_base}")
        print("-----------------------------------------")