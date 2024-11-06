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