from calzadoo import total

salario = int(3000000)
cargoemple = ("directivo")
cargoemple = cargoemple[0].upper() + cargoemple[1:]
nivel_desempeño = ("alto")
nivel_desempeño = (nivel_desempeño[0].upper() + nivel_desempeño[1:])


#2
salairio2 = int(2500000)
cargoemple2 = ("DIRECTIVO")
cargoemple2 = cargoemple2[0].upper() + cargoemple2[1:].lower()
nivel_desempeño2 =("Medio")
#3
salario3 = int(1300000)
cargoemple3 = ("Auxiliar")
nivel_desempeño3 = ("Bajo")
#4
salario4 = int(1750000)
cargoemple4 = ("Operativo")
nivel_desempeño4 = ("MEDIO")
nivel_desempeño4= nivel_desempeño4[0].upper() + nivel_desempeño4[1:].lower()




def calcular_bonificacion(salario,cargoemple,nivel_desempeño):
    bonificacion : int = 0
 if cargoemple.lower() == "Directivo":
  if nivel_desempeño.lower() == "Alto":
    bonificacion = salario * 0.2
  elif nivel_desempeño.lower() == "Medio":
    bonificacion = salario * 0.1

elif cargoemple.lower() == "Operativo":
  if nivel_desempeño.lower() == "Alto":
    bonificacion = salario * 0.15
elif nivel_desempeño.lower() == "Medio":
    bonificacion = salario * 0.05

 return bonificacion



def mostrar_resumen(salario,cargoemple,nivel_desempeño):
    bonificacion : int =calcular_bonificacion(salario,cargoemple,nivel_desempeño)
    total =salario+bonificacion
    print("-----Resumen del Pago-----")
    print("Cargo:",cargoemple)
    print("Nivel de Desempeño:",nivel_desempeño)
    print("Salario Base:",salario)
    print("Bonificacion:",bonificacion)
    print("Total a Recibir: ",salario+bonificacion)
    print("--------------------------")

def main():
    try:
        salario = int(input("salario base mensual $:"))
        cargoemple = input("Cargo empleado:")
        cargoemple = cargoemple[0].upper() + cargoemple[1:].lower()
        nivel_desempeño = input("Nivel de desempeño:")
        mostrar_resumen(salario,cargoemple,nivel_desempeño)
    except ValueError:
        print("Error")










