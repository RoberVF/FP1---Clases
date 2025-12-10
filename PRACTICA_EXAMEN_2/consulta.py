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

def inicializar_datos():
    return ({}, {}, {}) # Retorna la tupla vacía inicial

def listar_estudiantes_asignatura(datos, cod_asig):
    estudiantes, asignaturas, _ = datos
    
    # Validacion de claves
    if cod_asig not in asignaturas:
        return "La clave no existe"
    
    lista_dnis = asignaturas[cod_asig]['estudiantes']
    
    # Validacion de vacio
    if not lista_dnis:
        return None
        
    nombres = []
    for dni in lista_dnis:
        # Asumimos consistencia: si está en la asignatura, existe en estudiantes
        nombres.append(estudiantes[dni]['nombre'])
        
    return sorted(nombres)

def calcular_media_estudiante(datos, dni):
    estudiantes, _, _ = datos
    
    if dni not in estudiantes:
        return "La clave no existe"
        
    notas_dict = estudiantes[dni]['examenes_realizados']
    
    if not notas_dict:
        return None
        
    lista_notas = list(notas_dict.values())
    return sum(lista_notas) / len(lista_notas)

def asignaturas_sin_examenes(datos):
    _, asignaturas, _ = datos
    resultado = {}
    
    for cod, info in asignaturas.items():
        if not info['examenes']: # Si el conjunto/lista está vacío
            resultado[cod] = info['nombre']
            
    if not resultado:
        return None
        
    return resultado

def ranking_estudiantes(datos):
    estudiantes, _, _ = datos
    ranking = []
    
    for dni, info in estudiantes.items():
        if info['examenes_realizados']: # Solo si ha hecho exámenes
            notas = info['examenes_realizados'].values()
            media = sum(notas) / len(notas)
            ranking.append((dni, info['nombre'], media))
            
    if not ranking:
        return None
        
    # Ordenar por nota media (índice 2) descendente
    # Truco docente: explicar la lambda o itemgetter aquí
    return sorted(ranking, key=lambda x: x[2], reverse=True)

def examen_mas_concurrido(datos, cod_asig):
    _, asignaturas, examenes = datos
    
    if cod_asig not in asignaturas:
        return "La clave no existe"
    
    codigos_examenes = asignaturas[cod_asig]['examenes']
    
    if not codigos_examenes:
        return None
        
    max_presentados = -1
    resultado = []
    
    for cod_ex in codigos_examenes:
        # Obtenemos cuantos tienen nota en ese examen
        num_presentados = len(examenes[cod_ex]['notas'])
        
        if num_presentados > max_presentados:
            max_presentados = num_presentados
            resultado = [(examenes[cod_ex]['descripcion'], num_presentados)]
        elif num_presentados == max_presentados:
            resultado.append((examenes[cod_ex]['descripcion'], num_presentados))
            
    if len(resultado) == 1:
        return resultado[0]
    return resultado

