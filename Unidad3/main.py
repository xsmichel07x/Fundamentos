from reportes import *
from computadoras import *

# MENÚ PRINCIPAL
opcion = 0
while opcion <= 10:
    print("\n   ୨୧ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ୨୧")
    print("        ♡ SISTEMA DE PRÉSTAMOS ♡")
    print("   ୨୧ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ୨୧")
    print(" 1. Consultar computadoras")
    print(" 2. Buscar por software")
    print(" 3. Solicitar préstamo")
    print(" 4. Devolver computadora")
    print(" 5. Crear reservación")
    print(" 6. Agregar computadora")
    print(" 7. Historial de prestamos")
    print(" 8. Historial de necesidades")
    print(" 9. Estadisticas")
    print(" 10. Salir")
    print("   ୨୧ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ୨୧")
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
      consultar_computadoras()

    elif opcion == 2:
      buscar_sw()

    elif opcion == 3:
      solicitar_prestamo()

    elif opcion == 4:
      devolver_computadora()

    elif opcion == 5:
      print("\n   .｡.:*･°  CREAR RESERVACIÓN  °･*:.｡.   ")

    elif opcion == 6:
      agregar_computadora()

    elif opcion == 7:
      mostrar_prestamos()

    elif opcion == 8:
      mostrar_necesidades()

    elif opcion == 9:
      mostrar_estadisticas()

    elif opcion == 10:
        print("\nGracias por utilizar el sistema ♡")
        break
    else:
        print("\nOpción no válida.")