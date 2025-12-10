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
        "EXP01": { 
            "nombre": "Expresión Gráfica",
            "semestre": 1,
            "estudiantes": set(),
            "examenes": set()
        }
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
    
    # # CONSULTA
    # print(consulta.listar_estudiantes_asignatura(datos, "PROG1"))
    
    # print(consulta.calcular_media_estudiante(datos, "1111A")) 
    # print(consulta.asignaturas_sin_examenes(datos)) 

    # print(consulta.ranking_estudiantes(datos))

    # # ADICCION    
    # print(adiccion.matricular_estudiante(datos, "3333C", "PROG1"))

    # nuevo_examen = ("E-PROG-REC", "Recuperacion Python", "PROG1", "2024-06-20")
    # print(adiccion.crear_examen(datos, nuevo_examen))

    # print(adiccion.registrar_nota(datos, "E-PROG-REC", "2222B", 6.0))

    # # MODIFICACION
    # print(modificacion.actualizar_nota(datos, "E-MAT-1", "1111A", 10.0))
    # _, asignaturas, examenes = datos
    # print("   Nueva nota en examen:", examenes["E-MAT-1"]["notas"]["1111A"])

    # print(modificacion.cambiar_codigos_asignaturas(datos))
    # print("   Claves de asignaturas actuales:", list(asignaturas.keys()))

    # #BORRADO
    # print(borrado.eliminar_estudiante_completo(datos, "2222B"))