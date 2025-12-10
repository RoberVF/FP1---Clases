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

def actualizar_nota(datos, cod_examen, dni, nueva_nota):
    estudiantes, _, examenes = datos
    
    # Verificaciones basicas omitidas por brevedad, pero necesarias
    if dni in examenes.get(cod_examen, {}).get('notas', {}):
        examenes[cod_examen]['notas'][dni] = nueva_nota
        estudiantes[dni]['examenes_realizados'][cod_examen] = nueva_nota
        return "Nota actualizada"
    else:
        return "El estudiante no ha realizado este examen previamente"

def cambiar_semestre(datos, cod_asig, nuevo_semestre):
    _, asignaturas, _ = datos
    
    if cod_asig in asignaturas:
        if 1 <= nuevo_semestre <= 8:
            asignaturas[cod_asig]['semestre'] = nuevo_semestre
            return "Semestre actualizado"
    return "Error en datos"

def renombrar_asignatura(datos, cod_asig, nuevo_nombre):
    _, asignaturas, _ = datos
    if cod_asig in asignaturas:
        asignaturas[cod_asig]['nombre'] = nuevo_nombre

def cambiar_codigos_asignaturas(datos):
    estudiantes, asignaturas, examenes = datos

    # Paso 1: Crear mapeo de claves viejas a nuevas
    mapeo_cambios = {}
    claves_antiguas = list(asignaturas.keys())
    
    for cod in claves_antiguas:
        if cod.startswith("EX") and "-" not in cod:
            nuevo_cod = cod.replace("EX", "EX-")
            mapeo_cambios[cod] = nuevo_cod
            
            # Mover datos en diccionario asignaturas
            valor = asignaturas.pop(cod)
            asignaturas[nuevo_cod] = valor
    
    # Paso 2: Actualizar referencias en Examenes
    for info_examen in examenes.values():
        asig_examen = info_examen['asignatura']
        if asig_examen in mapeo_cambios:
            info_examen['asignatura'] = mapeo_cambios[asig_examen]
            
    # Paso 3: Actualizar referencias en Estudiantes
    for info_est in estudiantes.values():
        nuevas_asigs = set()
        cambio_necesario = False
        for asig in info_est['asignaturas']:
            if asig in mapeo_cambios:
                nuevas_asigs.add(mapeo_cambios[asig])
                cambio_necesario = True
            else:
                nuevas_asigs.add(asig)
        
        if cambio_necesario:
            info_est['asignaturas'] = nuevas_asigs
            
    return "Códigos actualizados masivamente"