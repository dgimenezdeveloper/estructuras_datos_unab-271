# Clase Paciente:
## self.historial_enfermedades y self.medicamentos:
- Declarar self.historial_enfermedades y self.medicamentos como listas vacías si no se proporcionan tiene varias ventajas:

### Evita errores de tipo: 
- Asegura que self.historial_enfermedades y self.medicamentos siempre sean listas, evitando errores si se intenta usar métodos de lista en ellos.

### Código más limpio: 
- Simplifica el código al evitar la necesidad de verificar si las variables son None antes de usarlas.

### Consistencia: 
- Mantiene un comportamiento consistente del objeto Paciente, ya que siempre tendrá listas para historial_enfermedades y medicamentos.

### Facilidad de uso: 
- Facilita la adición de enfermedades y medicamentos sin necesidad de inicializar las listas manualmente.

## calcular_edad():
### ventajas 
Usar una cadena de texto en el formato "YYYY-MM-DD" para representar la fecha de nacimiento (fec_nac) en la clase Paciente es conveniente por varias razones:

### Compatibilidad y Estándar:
- El formato "YYYY-MM-DD" es un estándar internacional (ISO 8601) para representar fechas. Esto asegura que la fecha sea interpretada de manera consistente en diferentes sistemas y regiones.

### Facilidad de Conversión:
- Las cadenas en este formato pueden ser fácilmente convertidas a objetos datetime en Python usando datetime.strptime. Esto permite realizar operaciones de fecha y hora, como calcular la edad.

### Legibilidad:
- Las cadenas en el formato "YYYY-MM-DD" son fáciles de leer y entender tanto para los desarrolladores como para los usuarios.

### Validación Sencilla:
- Es más fácil validar una cadena en un formato específico que validar otros tipos de datos. Por ejemplo, se puede usar expresiones regulares para asegurarse de que la cadena cumple con el formato esperado.

### Interoperabilidad:
- Las cadenas en formato "YYYY-MM-DD" son fácilmente intercambiables entre diferentes sistemas y lenguajes de programación, lo que facilita la integración con APIs y bases de datos.

# Clase GestionPacientes:

Para la gestión de pacientes, donde las operaciones más habituales son buscar y actualizar pacientes, es preferible usar un diccionario. Los diccionarios en Python permiten acceder a los elementos en tiempo constante promedio (O(1)), lo que hace que las operaciones de búsqueda y actualización sean muy eficientes.


### Acceso rápido:
- Los diccionarios permiten acceder a los elementos rápidamente usando claves únicas (en este caso, id_paciente).

### Actualización eficiente:
- Actualizar un paciente en un diccionario es una operación rápida y directa.

### Evita duplicados:
- Los diccionarios no permiten claves duplicadas, lo que asegura que cada id_paciente sea único.

### Legibilidad:
- El código es más legible y fácil de entender cuando se usan diccionarios para asociar claves únicas con valores.

# UNIDAD 2 ESTRUCTURAS RECURSIVAS
### buscar_en_historial():
#### Análisis Algorítmico
- Complejidad Temporal: La complejidad temporal de la función recursiva es O(n), donde n es el número total de elementos en el historial de enfermedades y medicamentos. Esto se debe a que en el peor de los casos, la función debe recorrer todos los elementos para encontrar la clave o determinar que no está presente.

- Complejidad Espacial: La complejidad espacial también es O(n) debido a la pila de llamadas recursivas. Cada llamada recursiva agrega un nuevo marco a la pila, lo que puede ser un problema para listas muy largas debido a la limitación de profundidad de recursión en Python.

#### Consideraciones para Grandes Volúmenes de Datos
- Eficiencia: Aunque la recursión proporciona una solución clara y concisa, para grandes volúmenes de datos, una implementación iterativa podría ser más eficiente en términos de uso de memoria, ya que evita el crecimiento de la pila de llamadas.
- Legibilidad: La recursión es fácil de entender y seguir, lo que puede ser beneficioso para el mantenimiento del código.
- Optimización: Si se espera que el historial de tratamientos crezca significativamente, se podría considerar optimizar la búsqueda utilizando estructuras de datos más eficientes como conjuntos (sets) o diccionarios (hash maps) que ofrecen una búsqueda en tiempo constante O(1).
- Es una práctica común en programación separar la lógica recursiva en una función auxiliar privada para mantener la interfaz pública limpia y fácil de usar. 



# UNIDAD 3 ABB
Análisis Algorítmico
Complejidad Temporal:

Inserción: O(log n) en promedio, O(n) en el peor de los casos (árbol desbalanceado).
Búsqueda: O(log n) en promedio, O(n) en el peor de los casos.
Eliminación: O(log n) en promedio, O(n) en el peor de los casos.
Complejidad Espacial:

El espacio requerido es O(n), donde n es el número de nodos en el árbol.
Ventajas del Árbol Binario de Búsqueda
Eficiencia: Permite realizar operaciones de inserción, búsqueda y eliminación de manera eficiente, especialmente en árboles balanceados.
Organización: Mantiene los datos ordenados, lo que facilita la búsqueda de elementos específicos.
Escalabilidad: Es adecuado para manejar grandes volúmenes de datos debido a su complejidad logarítmica en operaciones comunes.
Comparación con la Clase GestionPacientes
La clase GestionPacientes utiliza un diccionario para almacenar los pacientes, lo cual ofrece una búsqueda en tiempo constante O(1). Sin embargo, un árbol binario de búsqueda es útil en situaciones donde se requiere mantener los datos ordenados y realizar operaciones de rango (por ejemplo, encontrar todos los pacientes con IDs en un cierto rango).



# (HECHO): Revisar Operaciones con pacientes -> Buscar por DNI retorna 'None'

# (HECHO): Revisar Gestion de Pacientes --> Elimar paciente no funciona correctamente

# !TODO: Reviar Arbol General y Cola de Prioridad en menu principal

# (HECHO): se guardan datos en estructuras distintas, no se tienen acceso a ellos. (Paciente <-> Arbol Binario)





1- Gestion de Pacientes
  - 1 Agregar Paciente (check)
    # (HECHO): Levantar errores de ingreso de fecha de nacimiento. 
  - 2 Eliminar Paciente (a revisar)
    # (HECHO): Agregar mensaje de eliminacion de paciente
  - 3 Obtener información de un paciente:
    - 3.1 Buscar por DNI (check)  
    # (HECHO): Verificar que los datos ingresados sean del tipo correcto.
    # (HECHO): Verificar porque retorna None cuando dni no existe.
    - 4 Actualizar información de un paciente
    # (HECHO): - Revisar y corregir la actualización de enfermedades y medicamentos en la clase Paciente, para añadir nuevos sin eliminar lo anterior. (metodo extend())

    # TODO: Cola de prioridades y manejo de arbol general en menu. (
        - Urgencias médicas (Cola de prioridad)
        - Pacientes en espera (Arbol General)
        - Pacientes atendidos (Arbol General)
        - Pacientes fallecidos (Arbol General) (SOLO SI LLEGAMOS A TIEMPO)
    )
    # (HECHO): Ordenamiento topologico (sintomas, diagnosticos) (
        - Sintomas
        - Diagnosticos
    )

# 2- Operaciones con Pacientes
  - 1 Registrar un nuevo paciente
  # (HECHO) : Imprimir mensaje de confirmacion de registro (no figura paciente en clase Paciente)
    2- Buscar paciente por DNI
    # (HECHO): NO se imprime el paciente registrado(__str__) y tampoco se imprime mensaje de no encontrado.
    3 - Eliminar paciente por DNI
    # (HECHO): NO se imprime mensaje de eliminacion de paciente

3- Gestion Hospitales
    1- Agregar Hospital
  # TODO: Mejorar con un ciclo while la carga de hospitales? (Para mi no (DSG))
  2- Agregar una conexion entre hospitales
  # TODO: cambiar peso por distancia.
     garrahan -> elizalde (10)
     garrahan -> durand (100) (RUTA NO ENCONTRADA)
     fernandez -> pirovano (50)
     garrahan ->fernandez (20)
     garrahan -> pirovano (30)
  3 - Buscar una ruta entre dos hospitales
  # TODO: Devuelve lo mismo que opcion 4
  # TODO: No debe imprimir distancia 0 (hospital inicio -> hospital inicio)
  # TODO: evitar impresión de infinito cuando no hay conexion entre hospitales.
  5 - Calcular la distancia entre dos hospitales