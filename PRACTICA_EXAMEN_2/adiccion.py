# Estructura inferida: Una tupla con 3 diccionarios
# datos_academicos = (dicc_estudiantes, dicc_asignaturas, dicc_examenes)

# dicc_estudiantes:
# Clave: DNI (string)
# Valor: {'nombre': str, 'asignaturas': set(), 'examenes_realizados': {cod_examen: nota}}

# dicc_asignaturas:
# Clave: CODIGO (string)
# Valor: {'nombre': str, 'semestre': int, 'estudiantes': set(), 'examenes': set()}

# dicc_examenes:
# Clave: CODIGO (string)
# Valor: {'descripcion': str, 'asignatura': cod_asig, 'fecha': str, 'notas': {dni: nota}}

def matricular_estudiante(datos, dni, cod_asig):
    estudiantes, asignaturas, _ = datos
    
    if dni not in estudiantes or cod_asig not in asignaturas:
        return "La clave no existe"
    
    # Actualizamos diccionario Estudiantes
    estudiantes[dni]['asignaturas'].add(cod_asig)
    
    # Actualizamos diccionario Asignaturas
    asignaturas[cod_asig]['estudiantes'].add(dni)
    
    return "Matrícula realizada"

def crear_examen(datos, nuevo_examen):
    # nuevo_examen es tupla/diccionario: (cod_exam, desc, cod_asig, fecha)
    _, asignaturas, examenes = datos
    cod_exam, desc, cod_asig, fecha = nuevo_examen
    
    if cod_asig not in asignaturas:
        return "La asignatura no existe"
        
    # Crear entrada en diccionario Examenes
    examenes[cod_exam] = {
        'descripcion': desc,
        'asignatura': cod_asig,
        'fecha': fecha,
        'notas': {} # Inicialmente vacio
    }
    
    # Vincular en diccionario Asignaturas
    asignaturas[cod_asig]['examenes'].add(cod_exam)
    
    return "Examen creado"

def registrar_nota(datos, cod_examen, dni, nota):
    estudiantes, _, examenes = datos
    
    if cod_examen not in examenes:
        return "El examen no existe"
    if dni not in estudiantes:
        return "El estudiante no existe"
        
    cod_asig = examenes[cod_examen]['asignatura']
    
    # Verificar matrícula
    if cod_asig not in estudiantes[dni]['asignaturas']:
        return "El estudiante no está matriculado en la asignatura"
        
    # Actualizar diccionario Examenes
    examenes[cod_examen]['notas'][dni] = nota
    
    # Actualizar diccionario Estudiantes
    estudiantes[dni]['examenes_realizados'][cod_examen] = nota
    
    return "Nota registrada"

def matricular_lista_estudiantes(datos, lista_estudiantes, cod_asig):
    estudiantes, asignaturas, _ = datos
    
    if cod_asig not in asignaturas:
        return "La asignatura no existe"
        
    for dni, nombre in lista_estudiantes:
        # Crear estudiante si no existe
        if dni not in estudiantes:
            estudiantes[dni] = {
                'nombre': nombre,
                'asignaturas': set(),
                'examenes_realizados': {}
            }
        
        # Reutilizamos la funcion anterior :)
        matricular_estudiante(datos, dni, cod_asig)
        
    return "Proceso masivo completado"