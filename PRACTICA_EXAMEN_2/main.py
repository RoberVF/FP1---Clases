import consulta
import adiccion
import modificacion
import borrado

# DATOS
def cargar_datos_prueba():
    # Diccionario de Estudiantes
    dicc_estudiantes = {
        "1111A": {
            "nombre": "Ana García", 
            "asignaturas": {"PROG1", "MAT1"}, 
            "examenes_realizados": {"E-PROG-1": 9.5, "E-MAT-1": 7.0}
        },
        "2222B": {
            "nombre": "Berto Romero", 
            "asignaturas": {"PROG1"}, 
            "examenes_realizados": {"E-PROG-1": 4.5}
        },
        "3333C": {
            "nombre": "Carla Simona", 
            "asignaturas": {"MAT1", "FIS1"}, 
            "examenes_realizados": {}
        }
    }

    # Diccionario de Asignaturas
    dicc_asignaturas = {
        "PROG1": {
            "nombre": "Programacion I", 
            "semestre": 1, 
            "estudiantes": {"1111A", "2222B"}, 
            "examenes": {"E-PROG-1"}
        },
        "MAT1": {
            "nombre": "Matematicas I", 
            "semestre": 1, 
            "estudiantes": {"1111A", "3333C"}, 
            "examenes": {"E-MAT-1"}
        },
        "FIS1": {
            "nombre": "Fisica I", 
            "semestre": 2, 
            "estudiantes": {"3333C"}, 
            "examenes": set()
        },
        # "EXP01": { 
        #     "nombre": "Expresión Gráfica",
        #     "semestre": 1,
        #     "estudiantes": set(),
        #     "examenes": set()
        # }
    }

    # Diccionario de Examenes
    dicc_examenes = {
        "E-PROG-1": {
            "descripcion": "Parcial Python", 
            "asignatura": "PROG1", 
            "fecha": "2023-11-15", 
            "notas": {"1111A": 9.5, "2222B": 4.5}
        },
        "E-MAT-1": {
            "descripcion": "Final Álgebra", 
            "asignatura": "MAT1", 
            "fecha": "2024-01-20", 
            "notas": {"1111A": 7.0}
        }
    }

    return (dicc_estudiantes, dicc_asignaturas, dicc_examenes)

if __name__ == "__main__":
    datos = cargar_datos_prueba()
    print(consulta.listar_estudiantes_asignatura(datos, "PROG1"))