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

def dar_baja_estudiante_asignatura(datos, dni, cod_asig):
    estudiantes, asignaturas, examenes = datos
    
    if dni not in estudiantes or cod_asig not in asignaturas:
        return "Datos incorrectos"
        
    # 1. Eliminar de la lista de estudiantes de la asignatura
    asignaturas[cod_asig]['estudiantes'].discard(dni)
    
    # 2. Eliminar de la lista de asignaturas del estudiante
    estudiantes[dni]['asignaturas'].discard(cod_asig)
    
    # 3. Eliminar notas de exámenes de ESA asignatura
    # Identificamos los exámenes de esa asignatura
    examenes_asig = asignaturas[cod_asig]['examenes']
    
    for cod_ex in examenes_asig:
        # Borrar del diccionario de exámenes
        if dni in examenes[cod_ex]['notas']:
            del examenes[cod_ex]['notas'][dni]
            
        # Borrar del historial del estudiante
        if cod_ex in estudiantes[dni]['examenes_realizados']:
            del estudiantes[dni]['examenes_realizados'][cod_ex]
            
    return "Baja tramitada y notas eliminadas"

def eliminar_examen_completo(datos, cod_examen):
    estudiantes, asignaturas, examenes = datos
    
    if cod_examen not in examenes: return "No existe"
    
    info_examen = examenes[cod_examen]
    cod_asig = info_examen['asignatura']
    
    # 1. Eliminar referencia en Asignaturas
    if cod_asig in asignaturas:
        asignaturas[cod_asig]['examenes'].discard(cod_examen)
        
    # 2. Eliminar referencias en Estudiantes (historial de notas)
    dnis_presentados = info_examen['notas'].keys()
    for dni in dnis_presentados:
        if dni in estudiantes:
            del estudiantes[dni]['examenes_realizados'][cod_examen]
            
    # 3. Eliminar el examen en sí
    del examenes[cod_examen]
    return "Examen eliminado"

def eliminar_estudiante_completo(datos, dni):
    estudiantes, asignaturas, examenes = datos
    
    if dni not in estudiantes: return "No existe"
    
    # 1. Borrarlo de las listas de las asignaturas donde estaba matriculado
    for cod_asig in estudiantes[dni]['asignaturas']:
        if cod_asig in asignaturas:
            asignaturas[cod_asig]['estudiantes'].discard(dni)
            
    # 2. Borrar sus notas de los exámenes
    for cod_ex in estudiantes[dni]['examenes_realizados']:
        if cod_ex in examenes:
             if dni in examenes[cod_ex]['notas']:
                del examenes[cod_ex]['notas'][dni]
                
    # 3. Borrar estudiante
    del estudiantes[dni]
    return "Estudiante eliminado"

def eliminar_asignatura_completa(datos, cod_asig):
    estudiantes, asignaturas, examenes = datos
    
    if cod_asig not in asignaturas: return "No existe"
    
    # 1. Eliminar todos los exámenes asociados a esta asignatura
    # Hacemos una copia de la lista porque vamos a modificar el diccionario mientras iteramos
    lista_examenes = list(asignaturas[cod_asig]['examenes'])
    for cod_ex in lista_examenes:
        eliminar_examen_completo(datos, cod_ex) # Reutilizamos función
        
    # 2. Desmatricular a los estudiantes
    lista_estudiantes = list(asignaturas[cod_asig]['estudiantes'])
    for dni in lista_estudiantes:
        if dni in estudiantes:
            estudiantes[dni]['asignaturas'].discard(cod_asig)
            
    # 3. Borrar asignatura
    del asignaturas[cod_asig]
    return "Asignatura eliminada"