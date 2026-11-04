from datos import *

def mostrar_prestamos():
  print("\n   .｡.:*･°  HISTORIAL DE PRESTAMOS  °･*:.｡.   ")
  if len(prestamos) == 0:
    print("No hay prestamos registrados.")
  for i in range(len(prestamos)):
    print("Alumno:", prestamos[i]["num_control"], "| Software:", prestamos[i]["programa"],
          "| Aula:", prestamos[i]["aula"], "| ID:", prestamos[i]["id"])

def mostrar_necesidades():
  print("\n   .｡.:*･°  HISTORIAL DE NECESIDADES  °･*:.｡.   ")
  if len(necesidades) == 0:
    print("No hay necesidades registradas.")
  else:
    for i in range(len(necesidades)):
      print("Programa:", necesidades[i]["programa"], "| Fecha y hora:", necesidades[i]["fecha"])

def mostrar_estadisticas():
  print("\n   .｡.:*･°  ESTADISTICAS DE PRESTAMOS  °･*:.｡.   ")
  if len(prestamos) == 0:
    print("No hay préstamos registrados para generar estadísticas todavía.")
    return
  conteo_programas = {}
  for p in prestamos:
      prog = p["programa"] # Corregido acceso a diccionario
      conteo_programas[prog] = conteo_programas.get(prog, 0) + 1
  print("\n   ✿ Préstamos por Programa ✿   ")
  for prog, cant in conteo_programas.items():
      print(f"- {prog}: {cant} vez/veces")
  conteo_carreras = {}
  for p in prestamos:
      n_control = p["num_control"] # Corregido acceso a diccionario
      carrera_alumno = "Carrera No Registrada"
      # Buscar la carrera del alumno en la lista de alumnos activos
      for al in alumnos:
          if al["num_control"] == n_control:
              carrera_alumno = al["carrera"]
              break
      conteo_carreras[carrera_alumno] = conteo_carreras.get(carrera_alumno, 0) + 1
  print("\n   ✿ Préstamos por Carrera ✿   ")
  for carrera, cant in conteo_carreras.items():
      print(f"- {carrera}: {cant} vez/veces")