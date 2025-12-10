# Estructura de datos académicos
La estructura de datos que se describe al final de esta página es similar a la que se usará en el segundo examen de Fundamentos de Programación I. La estructura se usa para almacenar datos académicos y consiste en una tupla que contiene tres diccionarios. Con esta estructura se puede plantear una gran variedad de ejercicios.

## Ejercicios de consulta (obtención de información)
1. Listar estudiantes de una asignatura. Dada una estructura de datos y un código de asignatura, devolver una lista con los nombres completos de todos los estudiantes matriculados en esa asignatura, ordenados alfabéticamente.

2. Calcular la nota media de un estudiante. Dado un DNI de un estudiante, calcular y devolver la nota media de todos los exámenes que ha realizado. Si no ha realizado ningún examen, devolver None.

3. Encontrar asignaturas sin exámenes. Devolver un diccionario donde las claves sean los códigos de las asignaturas que no tienen ningún examen asociado, y los valores sean los nombres de esas asignaturas.

4. Obtener el ránking de estudiantes por nota media. Generar una lista de tuplas (DNI, nombre_completo, nota_media) con todos los estudiantes que hayan realizado al menos un examen, ordenada de mayor a menor por la nota media.

5. Obtener la lista de exámenes de una asignatura con más examinados. Dado un código de asignatura, obtener el examen con mayor número de presentados y devolver los dos datos (descripción del examen y número de presenados) en una tupla. Si hay más de un examen con el mayor número de presentados, devolverlos todos en una lista dentro de la tupla.

*NOTA: Todas los ejercicios de consulta deben verificar que las claves existen en los diccionarios y que lo que se busca no está vacío. En los dos casos, devolver un valor diferente para destacar tal incidencia. Por ejemplo, si una clave no se encuentra, devolver "La clave no existe" y si una lista o un diccionario está vació devolver None.*

## Ejercicios de adición (inserción de información)
5. Matricular un estudiante en una asignatura. Dado un DNI de un estudiante existente y un código de una asignatura existente, matricular al estudiante en esa asignatura. La función debe actualizar tanto el diccionario de estudiantes como el de asignaturas, y verificar que el estudiante no esté ya matriculado.

6. Crear un nuevo examen. Dados los datos de un nuevo examen (código, descripción, código de asignatura, fecha), añadirlo a la estructura. El examen debe crearse sin notas inicialmente. La función debe actualizar el diccionario de exámenes y el conjunto de exámenes de la asignatura correspondiente.

7. Registrar la nota de un estudiante en un examen Dado un código de un examen, un DNI de un estudiante y una nota, registrar esa calificación. La función debe verificar que el estudiante esté matriculado en la asignatura del examen y actualizar tanto el diccionario de exámenes como el conjunto de exámenes realizados por el estudiante.

8. Matricular un listado de estudiantes en una asignatura. Dada una lista de estudiantes, representados mediante tuplas (DNI, nombre y apellido), y el código de una asignatura, comprobar si el estudiante y el código de asignatura ya existen para actuar en consecuencia. Crear los nuevos estudiantes si no existen y matricular a todos los estudiante en esa asignatura sólo si existe.

## Ejercicios de modificación (actualización de información)
9. Actualizar la nota de un estudiante en un examen. Dado un código de examen, un DNI de un estudiante y una nueva nota, modificar la calificación existente. La función debe verificar que el estudiante haya realizado ese examen previamente.

10. Cambiar el semestre de una asignatura. Dado un código de una asignatura y un nuevo número de semestre (entre 1 y 8), actualizar el semestre de impartición de esa asignatura.

11. Renombrar una asignatura. Dado un código de una asignatura y un nuevo nombre, actualizar el nombre de la asignatura en el diccionario correspondiente.

12. Cambiar todos los códigos de asignaturas. Cambiar todos los códigos de las asignaturas añadiendo un guion después del prefijo "EX", dando como resultado nuevos códigos del tipo EX-P01. Modificar todos los códigos de asignaturas existentes en la estructura.

*NOTA: Todas los ejercicios de consulta deben verificar que las claves existen en los diccionarios y que lo que se busca no está vacío. En los dos casos, devolver un valor diferente para destacar tal incidencia. Por ejemplo, si una clave no se encuentra, devolver "La clave no existe" y si una lista o un diccionario está vació devolver None.*

## Ejercicios de borrado (eliminación de información)
13. Dar de baja a un estudiante de una asignatura. Dado un DNI de un estudiante y un código de una asignatura, eliminar la matrícula del estudiante en esa asignatura. La función debe actualizar tanto el diccionario de estudiantes como el de asignaturas, y además eliminar todas las notas del estudiante en los exámenes de esa asignatura.

14. Eliminar un examen completo. Dado un código de examen, eliminarlo completamente de la estructura de datos. La función debe actualizar el diccionario de exámenes, el conjunto de exámenes de la asignatura correspondiente, y los conjuntos de exámenes realizados por todos los estudiantes que lo hayan hecho.

15. Eliminar un estudiante por completo. Dado un DNI de un estudiante, eliminar de la estructura toda la información relacionada con ese estudiante.

16. Eliminar una asignatura por completo. Dado un código de una asignatura, eliminar de la estructura toda la información relacionada con esa asignatura.

*NOTA: Todas los ejercicios de consulta deben verificar que las claves existen en los diccionarios y que lo que se busca no está vacío. En los dos casos, devolver un valor diferente para destacar tal incidencia. Por ejemplo, si una clave no se encuentra, devolver "La clave no existe" y si una lista o un diccionario está vació devolver None.*