# Lista de alumnos activos en el sistema
alumnos = [ { "num_control" : "26040200", "nombre" : "Superman"       , "carrera" : "Ingenieria en Inteligencia Artificial"  } ,
            { "num_control" : "26040201", "nombre" : "Batman"         , "carrera" : "Ingenieria en Sistemas Computacionales" } ,
            { "num_control" : "26040202", "nombre" : "Spiderman"      , "carrera" : "Ingenieria en Sistemas Computacionales" } ,
            { "num_control" : "26040203", "nombre" : "Thor"           , "carrera" : "Ingenieria en Inteligencia Artificial"  } ,
            { "num_control" : "26040203", "nombre" : "Ironman"        , "carrera" : "Ingenieria en Sistemas Computacionales" } ,
            { "num_control" : "26040204", "nombre" : "Capitan America", "carrera" : "Ingenieria en Inteligencia Artificial"  } , ]

# Cada valor en la lista de computadoras tiene su lista correspondiente con el
# aula donde esta ubicada, el software instalado y el estado de esa computadora
computadoras = [ { "id" : "PC-LC1-01", "aula" : "LC1", "programas" : "Python, VS Code"      , "estado" : "Disponible"    } ,
                 { "id" : "PC-LC1-02", "aula" : "LC1", "programas" : "Python, Java, VS Code", "estado" : "Prestada"      } ,
                 { "id" : "PC-LC1-03", "aula" : "LC1", "programas" : "AutoCAD, MATLAB"      , "estado" : "Reservada"     } ,
                 { "id" : "PC-LC2-01", "aula" : "LC2", "programas" : "Python, VS Code"      , "estado" : "Disponible"    } ,
                 { "id" : "PC-LC2-02", "aula" : "LC2", "programas" : "Python, Java, VS Code", "estado" : "Prestada"      } ,
                 { "id" : "PC-LC2-03", "aula" : "LC2", "programas" : "AutoCAD, MATLAB"      , "estado" : "Disponible"    } ,
                 { "id" : "PC-LC3-01", "aula" : "LC3", "programas" : "Python, VS Code"      , "estado" : "Disponible"    } ,
                 { "id" : "PC-LC3-02", "aula" : "LC3", "programas" : "Python, Java, VS Code", "estado" : "Prestada"      } ,
                 { "id" : "PC-LC3-03", "aula" : "LC3", "programas" : "AutoCAD, MATLAB"      , "estado" : "Reservada"     } ,
                 { "id" : "PC-LC3-04", "aula" : "LC3", "programas" : "Python, VS Code"      , "estado" : "Mantenimiento" } , ]

prestamos = [ { "num_control" : "26040201", "programa" : "python", "aula" : "LC1", "id" : "PC-LC1-01" } ,
              { "num_control" : "26040202", "programa" : "java"  , "aula" : "LC1", "id" : "PC-LC1-02" } ,
              { "num_control" : "26040201", "programa" : "matlab", "aula" : "LC2", "id" : "PC-LC2-01" } ,
              { "num_control" : "26040203", "programa" : "python", "aula" : "LC3", "id" : "PC-LC3-01" } ,
              { "num_control" : "26040204", "programa" : "python", "aula" : "LC3", "id" : "PC-LC3-02" } , ]

necesidades = [ { "programa" : "Photoshop", "fecha" : "12-102026 07:30:00" }, ]
