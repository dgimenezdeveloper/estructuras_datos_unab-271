# src/menu.py
import os
from sistema_gestion_pacientes import SistemaGestionPacientes
from paciente import Paciente
from arbol_general import ArbolGeneral
from cola_prioridades import ColaPrioridades
from grafo import Grafo
from datos_diagnosticos import obtener_datos_diagnosticos
from datos_hospitales import cargar_datos_hospitales
from entradas import solicitar_dni, solicitar_nombre, solicitar_fecha_nacimiento, solicitar_lista

def menu_principal():
    sistema_gestion = SistemaGestionPacientes()
    arbol_general = ArbolGeneral("Evento Raíz")
    cola_prioridades = ColaPrioridades()
    grafo = Grafo()
    grafo_diagnostico = Grafo()
    
    vertices, aristas = obtener_datos_diagnosticos()
    grafo_diagnostico.cargar_datos(vertices, aristas)
    
    cargar_datos_hospitales(grafo)

    opcion = None
    while opcion != "5":
        print("\nMenú Principal")
        print("1. Gestión de Pacientes")
        print("2. Operaciones con Pacientes")
        print("3. Gestión de Hospitales")
        print("4. Gestión de Diagnósticos")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            os.system('clear')
            menu_gestion_pacientes(sistema_gestion)
        elif opcion == "2":
            os.system('clear')
            menu_operaciones_pacientes(sistema_gestion)
        elif opcion == "3":
            os.system('clear')
            menu_gestion_hospitales(grafo)
        elif opcion == "4":
            os.system('clear')
            menu_gestion_diagnosticos(grafo_diagnostico)
        elif opcion == "5":
            os.system('clear')
            print("Saliendo del programa...")
        else:
            os.system('clear')
            print("Opción no válida. Intente de nuevo.")

def menu_gestion_pacientes(sistema_gestion):
    opcion = None
    while opcion != "5":
        os.system('clear')
        print("\nGestión de Pacientes")
        print("1. Agregar un nuevo paciente")
        print("2. Eliminar un paciente existente")
        print("3. Obtener información de un paciente")
        print("4. Actualizar información de un paciente")
        print("5. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            os.system('clear')
            id = solicitar_dni()
            nombre = solicitar_nombre()
            fecha_nac = solicitar_fecha_nacimiento()
            historial_enfermedades = solicitar_lista("Historial de Enfermedades (separadas por coma): ")
            medicamentos = solicitar_lista("Medicamentos (separados por coma): ")
            paciente = Paciente(id, nombre, fecha_nac, historial_enfermedades, medicamentos)
            if sistema_gestion.agregar_paciente(paciente):
                print("Paciente agregado exitosamente.")
            else:
                print("Error: El paciente con ese ID ya existe.")
        elif opcion == "2":
            os.system('clear')
            id = solicitar_dni()
            if sistema_gestion.eliminar_paciente(id):
                print("Paciente eliminado exitosamente.")
            else:
                print("Paciente no encontrado.")
        elif opcion == "3":
            os.system('clear')
            id = solicitar_dni()
            paciente = sistema_gestion.obtener_paciente(id)
            if paciente:
                print(paciente)
            else:
                print("Paciente no encontrado.")
        elif opcion == "4":
            os.system('clear')
            id = solicitar_dni()
            nombre = input("Nuevo Nombre (dejar en blanco para no cambiar): ")
            fecha_nac = input("Nueva Fecha de Nacimiento (YYYY-MM-DD) (dejar en blanco para no cambiar): ")
            if fecha_nac:
                fecha_nac = solicitar_fecha_nacimiento()
            historial_enfermedades = solicitar_lista("Nuevo Historial de Enfermedades (separadas por coma) (dejar en blanco para no cambiar): ")
            medicamentos = solicitar_lista("Nuevos Medicamentos (separados por coma) (dejar en blanco para no cambiar): ")
            if sistema_gestion.actualizar_paciente(id, nombre or None, fecha_nac or None, historial_enfermedades or None, medicamentos or None):
                print("Paciente actualizado exitosamente.")
            else:
                print("Paciente no encontrado.")
        elif opcion == "5":
            os.system('clear')
            print("Volviendo al Menú Principal...")
        else:
            os.system('clear')
            print("Opción no válida. Intente de nuevo.")

def menu_operaciones_pacientes(sistema_gestion):
    opcion = None
    while opcion != "4":
        print("\nOperaciones con Pacientes")
        print("1. Registrar un nuevo paciente")
        print("2. Buscar un paciente por DNI")
        print("3. Eliminar un paciente por DNI")
        print("4. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            os.system('clear')
            id = solicitar_dni()
            nombre = solicitar_nombre()
            fecha_nac = solicitar_fecha_nacimiento()
            historial_enfermedades = solicitar_lista("Historial de Enfermedades (separadas por coma): ")
            medicamentos = solicitar_lista("Medicamentos (separados por coma): ")
            paciente = Paciente(id, nombre, fecha_nac, historial_enfermedades, medicamentos)
            if sistema_gestion.agregar_paciente(paciente):
                print("Paciente registrado exitosamente.")
            else:
                print("Error: El paciente con ese ID ya existe.")
        elif opcion == "2":
            os.system('clear')
            id = solicitar_dni()
            paciente = sistema_gestion.obtener_paciente(id)
            if paciente:
                print(paciente)
            else:
                print("Paciente no encontrado.")
        elif opcion == "3":
            os.system('clear')
            id = solicitar_dni()
            if sistema_gestion.eliminar_paciente(id):
                print("Paciente eliminado exitosamente.")
            else:
                print("Paciente no encontrado.")
        elif opcion == "4":
            os.system('clear')
            print("Volviendo al Menú Principal...")
        else:
            os.system('clear')
            print("Opción no válida. Intente de nuevo.")

def menu_gestion_hospitales(grafo):
    opcion = None
    while opcion != "6":
        print("\nGestión de Hospitales")
        print("1. Agregar un nuevo hospital")
        print("2. Agregar una conexión entre hospitales")
        print("3. Buscar una ruta entre hospitales")
        print("4. Buscar una ruta más corta entre hospitales")
        print("5. Calcular distancias desde un hospital")
        print("6. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            os.system('clear')
            hospital = input("Nombre del hospital: ").lower()
            grafo.agregar_vertice(hospital)
            print(f"Hospital '{hospital}' agregado exitosamente.")
        elif opcion == "2":
            os.system('clear')
            hospital1 = input("Nombre del primer hospital: ").lower()
            hospital2 = input("Nombre del segundo hospital: ").lower()
            peso = int(input("Distancia de la conexión: "))
            grafo.agregar_arista(hospital1, hospital2, peso)
            print(f"Conexión entre '{hospital1}' y '{hospital2}' con distancia {peso} agregada exitosamente.")
        elif opcion == "3":
            os.system('clear')
            inicio = input("Hospital de inicio: ").lower()
            objetivo = input("Hospital objetivo: ").lower()
            ruta = grafo.dfs(inicio, objetivo)
            print(f"Ruta encontrada: {ruta}")
        elif opcion == "4":
            os.system('clear')
            inicio = input("Hospital de inicio: ").lower()
            objetivo = input("Hospital objetivo: ").lower()
            ruta = grafo.bfs(inicio, objetivo)
            print(f"Ruta más corta encontrada: {ruta}")
        elif opcion == "5":
            os.system('clear')
            inicio = input("Hospital de inicio: ").lower()
            grafo.imprimir_dijkstra(inicio)
        elif opcion == "6":
            os.system('clear')
            print("Volviendo al Menú Principal...")
        else:
            os.system('clear')
            print("Opción no válida. Intente de nuevo.")

def menu_gestion_diagnosticos(grafo_diagnostico):
    continuar = True
    while continuar:
        os.system('clear')
        print("\nGestión de Diagnósticos")
        print("1. Buscar pasos para diagnóstico")
        print("2. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            os.system('clear')
            sintoma = input("Ingrese el síntoma inicial: ").lower()
            diagnostico = input("Ingrese el diagnóstico: ").lower()
            camino = grafo_diagnostico.dfs(sintoma, diagnostico)
            if camino:
                print(f"Pasos necesarios para {diagnostico}: {' -> '.join(camino)}")
            else:
                print("No se encontraron pasos para este diagnóstico.")
            input("\nPresione Enter para continuar...")
        elif opcion == "2":
            continuar = False
        else:
            print("Opción no válida. Intente de nuevo.")
            input("\nPresione Enter para continuar...")