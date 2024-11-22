# src/grafo.py
from cola_prioridades import ColaPrioridades

class Grafo:
    def __init__(self):
        self.vertices = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []

    def agregar_arista(self, vertice1, vertice2, peso=1):
        if vertice1 in self.vertices and vertice2 in self.vertices:
            self.vertices[vertice1].append((vertice2, peso))
            self.vertices[vertice2].append((vertice1, peso))

    def dfs(self, inicio, objetivo, visitados=None):
        if visitados is None:
            visitados = set()
        visitados.add(inicio)
        if inicio == objetivo:
            return [inicio]
        for vecino, _ in self.vertices[inicio]:
            if vecino not in visitados:
                camino = self.dfs(vecino, objetivo, visitados)
                if camino:
                    return [inicio] + camino
        return None

    def bfs(self, inicio, objetivo):
        visitados = set()
        cola = [(inicio, [inicio])]
        while cola:
            vertice, camino = cola.pop(0)
            if vertice not in visitados:
                visitados.add(vertice)
                for vecino, _ in self.vertices[vertice]:
                    if vecino == objetivo:
                        return camino + [vecino]
                    else:
                        cola.append((vecino, camino + [vecino]))
        return None

    def dijkstra(self, inicio):
        distancias = {vertice: float('infinity') for vertice in self.vertices}
        distancias[inicio] = 0
        cola_prioridad = ColaPrioridades()
        cola_prioridad.agregar_paciente(0, inicio)
    
        while cola_prioridad.elementos:
            vertice_actual = cola_prioridad.obtener_paciente()
            distancia_actual = distancias[vertice_actual]
    
            for vecino, peso in self.vertices[vertice_actual]:
                distancia = distancia_actual + peso
    
                if distancia < distancias[vecino]:
                    distancias[vecino] = distancia
                    cola_prioridad.agregar_paciente(distancia, vecino)
    
        return distancias
    
    def imprimir_dijkstra(self, inicio):
        distancias = self.dijkstra(inicio)
        for hospital, distancia in distancias.items():
            print(f"Distancia desde {inicio} a {hospital}: {distancia}")
    
    def _dfs_topologico(self, vertice, visitados, orden):
        visitados.add(vertice)
        for vecino, _ in self.vertices[vertice]:
            if vecino not in visitados:
                self._dfs_topologico(vecino, visitados, orden)
        orden.append(vertice)

    def ordenamiento_topologico(self):
        visitados = set()
        orden = []
        for vertice in self.vertices:
            if vertice not in visitados:
                self._dfs_topologico(vertice, visitados, orden)
        orden.reverse()
        return orden