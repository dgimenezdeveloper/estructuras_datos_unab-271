# src/menus.py

from paciente import Paciente, GestionPacientes
from arbol_binario import ArbolBinarioBusqueda
from arbol_general import ArbolGeneral
from cola_prioridades import ColaPrioridades
from grafo import Grafo

def menu_principal():
    gestion_pacientes = GestionPacientes()
    arbol = ArbolBinarioBusqueda()
    arbol_general = ArbolGeneral("Evento Raíz")
    cola_prioridades = ColaPrioridades()
    grafo = Grafo()

    opcion = None
    while opcion != "4":
        print("\nMenú Principal")
        print("1. Gestión de Pacientes")
        print("2. Operaciones con Pacientes")
        print("3. Gestión de Hospitales")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_gestion_pacientes(gestion_pacientes)
        elif opcion == "2":
            menu_operaciones_pacientes(arbol)
        elif opcion == "3":
            menu_gestion_hospitales(grafo)
        elif opcion == "4":
            print("Saliendo del programa...")
        else:
            print("Opción no válida. Intente de nuevo.")

def menu_gestion_pacientes(gestion_pacientes):
    opcion = None
    while opcion != "5":
        print("\nGestión de Pacientes")
        print("1. Agregar un nuevo paciente")
        print("2. Eliminar un paciente existente")
        print("3. Obtener información de un paciente")
        print("4. Actualizar información de un paciente")
        print("5. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = int(input("Ingrese DNI: "))
            nombre = input("Nombre: ")
            fecha_nac = input("Fecha de Nacimiento (YYYY-MM-DD): ")
            historial_enfermedades = input("Historial de Enfermedades (separadas por coma): ").split(",")
            medicamentos = input("Medicamentos (separados por coma): ").split(",")
            paciente = Paciente(id, nombre, fecha_nac, historial_enfermedades, medicamentos)
            gestion_pacientes.agregar_paciente(paciente)
        elif opcion == "2":
            id = int(input("Ingrese DNI del paciente a eliminar: "))
            gestion_pacientes.eliminar_paciente(id)
        elif opcion == "3":
            id = int(input("Ingrese DNI del paciente a obtener: "))
            paciente = gestion_pacientes.obtener_paciente(id)
            print(paciente)
        elif opcion == "4":
            id = int(input("Ingrese DNI del paciente a actualizar: "))
            nombre = input("Nuevo Nombre (dejar en blanco para no cambiar): ")
            fecha_nac = input("Nueva Fecha de Nacimiento (YYYY-MM-DD) (dejar en blanco para no cambiar): ")
            historial_enfermedades = input("Nuevo Historial de Enfermedades (separadas por coma) (dejar en blanco para no cambiar): ").split(",")
            medicamentos = input("Nuevos Medicamentos (separados por coma) (dejar en blanco para no cambiar): ").split(",")
            gestion_pacientes.actualizar_paciente(id, nombre or None, fecha_nac or None, historial_enfermedades or None, medicamentos or None)
        elif opcion == "5":
            print("Volviendo al Menú Principal...")
        else:
            print("Opción no válida. Intente de nuevo.")

def menu_operaciones_pacientes(arbol):
    opcion = None
    while opcion != "4":
        print("\nOperaciones con Pacientes")
        print("1. Registrar un nuevo paciente")
        print("2. Buscar un paciente por DNI")
        print("3. Eliminar un paciente por DNI")
        print("4. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = int(input("Ingrese DNI: "))
            nombre = input("Nombre: ")
            fecha_nac = input("Fecha de Nacimiento (YYYY-MM-DD): ")
            historial_enfermedades = input("Historial de Enfermedades (separadas por coma): ").split(",")
            medicamentos = input("Medicamentos (separados por coma): ").split(",")
            paciente = Paciente(id, nombre, fecha_nac, historial_enfermedades, medicamentos)
            arbol.insertar(paciente)
        elif opcion == "2":
            id = int(input("Ingrese DNI del paciente a buscar: "))
            paciente = arbol.buscar(id)
            print(paciente)
        elif opcion == "3":
            id = int(input("Ingrese DNI del paciente a eliminar: "))
            arbol.eliminar(id)
        elif opcion == "4":
            print("Volviendo al Menú Principal...")
        else:
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
            hospital = input("Nombre del hospital: ")
            grafo.agregar_vertice(hospital)
        elif opcion == "2":
            hospital1 = input("Nombre del primer hospital: ")
            hospital2 = input("Nombre del segundo hospital: ")
            peso = int(input("Peso de la conexión: "))
            grafo.agregar_arista(hospital1, hospital2, peso)
        elif opcion == "3":
            inicio = input("Hospital de inicio: ")
            objetivo = input("Hospital objetivo: ")
            ruta = grafo.dfs(inicio, objetivo)
            print(f"Ruta encontrada: {ruta}")
        elif opcion == "4":
            inicio = input("Hospital de inicio: ")
            objetivo = input("Hospital objetivo: ")
            ruta = grafo.bfs(inicio, objetivo)
            print(f"Ruta encontrada: {ruta}")
        elif opcion == "5":
            inicio = input("Hospital de inicio: ")
            grafo.imprimir_dijkstra(inicio)
        elif opcion == "6":
            print("Volviendo al Menú Principal...")
        else:
            print("Opción no válida. Intente de nuevo.")