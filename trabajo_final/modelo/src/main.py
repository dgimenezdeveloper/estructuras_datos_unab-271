# src/main.py

from paciente import Paciente
from arbol_binario import ArbolBinarioBusqueda
from arbol_general import ArbolGeneral
from cola_prioridades import ColaPrioridades
from grafo import Grafo

def main():
    # Ejemplo de hospitales públicos de Buenos Aires
    hospital_1 = "Hospital Elizalde"
    hospital_2 = "Hospital Garrahan"
    hospital_3 = "Hospital Fernández"
    hospital_4 = "Hospital Pirovano"
    hospital_5 = "Hospital Durand"

    # Se crean pacientes
    paciente1 = Paciente(1, "Juan Pérez", '1986-09-21', ["Diabetes"], ["Metformina"])
    paciente2 = Paciente(2, "María López", '1979-07-05', ["Hipertensión"], ["Losartán"])
    paciente3 = Paciente(3, "Carlos Gómez", '1990-03-15', ["Asma"], ["Salbutamol"])
    paciente4 = Paciente(4, "Ana Torres", '1982-11-30', ["Alergia"], ["Loratadina"])

    # Árbol Binario de Búsqueda
    arbol = ArbolBinarioBusqueda()
    arbol.insertar(paciente1)
    arbol.insertar(paciente2)
    arbol.insertar(paciente3)
    arbol.insertar(paciente4)
    print("Búsqueda en Árbol Binario de Búsqueda:")
    print(arbol.buscar(1).paciente)
    print(arbol.buscar(2).paciente)
    print(arbol.buscar(3).paciente)
    print(arbol.buscar(4).paciente)

    # Árbol General
    arbol_general = ArbolGeneral("Consulta Inicial")
    nodo1 = arbol_general.agregar_evento(arbol_general.raiz, "Diagnóstico")
    nodo2 = arbol_general.agregar_evento(nodo1, "Pruebas de Laboratorio")
    arbol_general.agregar_evento(nodo2, "Tratamiento")
    print("\nÁrbol General:")
    print(f"Raíz: {arbol_general.raiz.evento}")
    for hijo in arbol_general.raiz.hijos:
        print(f"Hijo de Raíz: {hijo.evento}")
        for nieto in hijo.hijos:
            print(f"Hijo de {hijo.evento}: {nieto.evento}")

    # Cola de Prioridades
    cola = ColaPrioridades()
    cola.agregar_paciente(1, paciente1)
    cola.agregar_paciente(3, paciente3)
    cola.agregar_paciente(2, paciente2)
    cola.agregar_paciente(4, paciente4)
    print("\nCola de Prioridades:")
    print('Paciente atendido:')
    print(cola.obtener_paciente())
    print('Paciente atendido:')
    print(cola.obtener_paciente())
    print('Paciente atendido:')
    print(cola.obtener_paciente())
    print('Paciente atendido:')
    print(cola.obtener_paciente())

    # Grafo
    grafo = Grafo()
    grafo.agregar_vertice(hospital_1)
    grafo.agregar_vertice(hospital_2)
    grafo.agregar_vertice(hospital_3)
    grafo.agregar_vertice(hospital_4)
    grafo.agregar_vertice(hospital_5)
    grafo.agregar_arista(hospital_1, hospital_2, 10)
    grafo.agregar_arista(hospital_2, hospital_3, 20)
    grafo.agregar_arista(hospital_3, hospital_4, 30)
    grafo.agregar_arista(hospital_4, hospital_5, 40)
    grafo.agregar_arista(hospital_1, hospital_5, 100)
    print("\nDFS en Grafo:")
    print(grafo.dfs(hospital_1, hospital_5))
    print("\nBFS en Grafo:")
    print(grafo.bfs(hospital_1, hospital_5))
    print("\nDijkstra en Grafo:")
    grafo.imprimir_dijkstra(hospital_1)

    # Ordenamiento Topológico
    grafo_diagnostico = Grafo()
    
    # Se agregan vértices (pasos del diagnóstico)
    grafo_diagnostico.agregar_vertice("Fiebre")
    grafo_diagnostico.agregar_vertice("Tos")
    grafo_diagnostico.agregar_vertice("Dolor de Cabeza")
    grafo_diagnostico.agregar_vertice("Prueba de Sangre")
    grafo_diagnostico.agregar_vertice("Prueba de Radiografía")
    grafo_diagnostico.agregar_vertice("Prueba de PCR")
    grafo_diagnostico.agregar_vertice("Diagnóstico de Gripe")
    grafo_diagnostico.agregar_vertice("Diagnóstico de Neumonía")
    grafo_diagnostico.agregar_vertice("Diagnóstico de COVID-19")


    # Se agregan aristas (dependencias entre los pasos)
    grafo_diagnostico.agregar_arista("Fiebre", "Prueba de Sangre")
    grafo_diagnostico.agregar_arista("Tos", "Prueba de Radiografía")
    grafo_diagnostico.agregar_arista("Dolor de Cabeza", "Prueba de PCR")
    grafo_diagnostico.agregar_arista("Prueba de Sangre", "Diagnóstico de Gripe")
    grafo_diagnostico.agregar_arista("Prueba de Radiografía", "Diagnóstico de Neumonía")
    grafo_diagnostico.agregar_arista("Prueba de PCR", "Diagnóstico de COVID-19")


    # Se realiza el ordenamiento topológico
    print("\nOrdenamiento Topológico para el Diagnóstico:")
    orden = grafo_diagnostico.ordenamiento_topologico()
    print(" -> ".join(orden))
    
    # Impresion de los pasos necesarios para cada diagnóstico
    diagnosticos = ["Diagnóstico de Gripe", "Diagnóstico de Neumonía", "Diagnóstico de COVID-19"]
    for diagnostico in diagnosticos:
        print(f"\nPasos necesarios para {diagnostico}:")
        camino = grafo_diagnostico.dfs("Fiebre", diagnostico) or grafo_diagnostico.dfs("Tos", diagnostico) or grafo_diagnostico.dfs("Dolor de Cabeza", diagnostico)
        if camino:
            print(" -> ".join(camino))
        else:
            print("No se encontraron pasos para este diagnóstico.")


if __name__ == "__main__":
    main()