from datos import *

def consultar_computadoras():
    print("\n   .｡.:*･°  COMPUTADORAS  °･*:.｡.   ")
    for i in range(len(computadoras)):
        print("Aula:", computadoras[i]["aula"],"| ID:", computadoras[i]["id"] ,
              "| Software:", computadoras[i]["programas"]," |Estado:", computadoras[i]["estado"] )

def buscar_sw():
  programa = input( "\nIngrese el software que desea buscar: ")
  print("\n   .｡.:*･°  RESULTADOS  °･*:.｡.   ")
  encontrado = False
  for i in range(len(computadoras)):
      if programa.lower() in computadoras[i]["programas"].lower():
          print("ID:", computadoras[i]["id"], "| Aula:", computadoras[i]["aula"], "| Software:", computadoras[i]["programas"], "| Estado:", computadoras[i]["estado"])
          encontrado = True
  if encontrado == False:
      print("No se encontraron computadoras con ese software.")

from datetime import datetime
def solicitar_prestamo():
    print("\n   ꒰  SOLICITAR PRESTAMO  ꒱   ")
    num_control = input("Numero de control del alumno: ")
    # Verificar si el alumno existe buscando en toda la lista de alumnos
    alumno_existe = False
    for al in alumnos:
        if al["num_control"] == num_control:
            alumno_existe = True
            break
    if alumno_existe:
        programa = input("Que programa necesita: ")
        encontrado = False
        for i in range(len(computadoras)):
            if programa.lower() in computadoras[i]["programas"].lower():
                if computadoras[i]["estado"] == "Disponible":
                    computadoras[i]["estado"] = "Prestada"
                    print("Se asignó la computadora", computadoras[i]["id"], "que esta en el aula", computadoras[i]["aula"])
                    prestamo = {"num_control": num_control, "programa": programa, "aula": computadoras[i]["aula"], "id": computadoras[i]["id"]}
                    prestamos.append(prestamo)
                    encontrado = True
                    break
                else:
                    print("Si se encontro el sofware pero esta", computadoras[i]["estado"])
        if not encontrado:
            print("\nEl programa no está disponible.")
            respuesta = input("¿Desea agregar este programa a la lista de necesidades? (si/no): ")
            if respuesta.lower() in ["si", "sí", "s"]:
                fecha_hora_actual = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                necesidades.append({"programa": programa, "fecha": fecha_hora_actual})
                print(f"El programa '{programa}' ha sido agregado a la lista de necesidades ({fecha_hora_actual}).")
    else:
        print("EL alumno no existe en la lista")

def devolver_computadora():
  print("\n   ꒰  DEVOLVER COMPUTADORA  ꒱   ")
  id_pc = input("Dame el ID de la computadora: ")
  existe = False
  for i in range( len(computadoras) ):
    if computadoras[i]["id"] == id_pc:
      existe = True
      if computadoras[i]["estado"]== "Prestada" or computadoras[i]["estado"]=="Reservada":
        computadoras[i]["estado"] = "Disponible"
        print("La computadora", id_pc, "ya esta disponible")
        break
      else:
        print("La computadora", id_pc, "no esta prestada/reservada")
  if existe == False:
    print("No existe la computadora", id_pc)

def agregar_computadora():
  print("\n   .｡.:*･°  AGREGAR COMPUTADORA  °･*:.｡.   ")
  id_computadora = input("ID de la computadora: ")
  aula = input("Aula: ")
  programas = input("Software instalado: ")
  # Se agrega como diccionario para mantener la consistencia con el resto del código
  nueva_computadora = {"id": id_computadora, "aula": aula, "programas": programas, "estado": "Disponible"}
  computadoras.append(nueva_computadora)
  print("\nComputadora agregada correctamente.")