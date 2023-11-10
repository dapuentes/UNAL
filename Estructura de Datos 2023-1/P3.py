class Graph:
    def __init__(self):
        self.graph = {}

    def print_graph(self):
        for vertex in self.graph:
            print(vertex, ':', self.graph[vertex])

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = {}
            return True
        return False

    def add_edge(self, v1, v2, weight):
        if v1 in self.graph and v2 in self.graph:
            self.graph[v1][v2] = weight
            self.graph[v2][v1] = weight

    def remove_edge(self, v1, v2):
        if v1 in self.graph and v2 in self.graph:
            del self.graph[v1][v2]
            del self.graph[v2][v1]

    def remove_vertex(self, vertex):
        if vertex in self.graph:
            for neighbor in self.graph[vertex]:
                del self.graph[neighbor][vertex]
            del self.graph[vertex]
            return True
        return False 

    def get_distance(self, v1, v2):
        if v1 in self.graph and v2 in self.graph:
            if v2 in self.graph[v1]:
                return self.graph[v1][v2]
        return float("inf")
    
    def dfs(self, start_vertex, visited=None):
        if visited is None:
            visited = []

        visited.append(start_vertex)        

        for neighbor in self.graph[start_vertex]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)
        return visited

    def bfs(self, start_vertex):
        visited = []
        queue = [start_vertex]

        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.append(vertex)
                neighbors = self.graph[vertex]
                queue.extend(neighbors)
        return visited


    def dijkstra(self, origin, destination):
        distances = {vertex: float('inf') for vertex in self.graph}
        distances[origin] = 0
        
        previous = {vertex: None for vertex in self.graph}        
        visited = set()

        while len(visited) != len(self.graph):
            current_vertex = None
            min_distance = float('inf')

            for vertex in self.graph:
                if distances[vertex] < min_distance and vertex not in visited:
                    current_vertex = vertex
                    min_distance = distances[vertex]

            visited.add(current_vertex)
            print(visited)

            if current_vertex == destination:
                break

            for neighbor, weight in self.graph[current_vertex].items():
                distance = distances[current_vertex] + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_vertex

        best_route = []
        current_vertex = destination
        while current_vertex != origin:
            previous_vertex = previous[current_vertex]
            edge = (previous_vertex, current_vertex)
            best_route.insert(0, edge)
            current_vertex = previous_vertex

        return distances[destination], best_route

# Example usage
graph = Graph()

graph.add_vertex('M1')
graph.add_vertex('M2')
graph.add_vertex('M3')
graph.add_vertex('M4')
graph.add_vertex('M5')
graph.add_vertex('M6')
graph.add_vertex('M7')
graph.add_vertex('M8')
graph.add_vertex('M9')
graph.add_vertex('M10')
graph.add_edge('M1','M2',10)
graph.add_edge('M2','M9',2)
graph.add_edge('M2','M8',15)
graph.add_edge('M8','M7',4)
graph.add_edge('M8','M9',12)
graph.add_edge('M9','M3',12)
graph.add_edge('M10','M3',3)
graph.add_edge('M7','M4',3)
graph.add_edge('M4','M3',3)
graph.add_edge('M3','M5',2)
graph.add_edge('M7','M5',3)
graph.add_edge('M7','M6',3)
graph.add_edge('M6','M5',8)
graph.print_graph()

# Agrega los vértices y las aristas al grafo...

start_vertex = 'M8'
end_vertex = 'M4'

# Realiza la búsqueda DFS
path = graph.bfs(start_vertex)

if end_vertex in path:
    # Encuentra el índice del vértice de destino en el camino
    end_index = path.index(end_vertex)

    # Extrae el subcamino desde el inicio hasta el destino
    sub_path = path[:end_index+1]

    # Imprime el camino encontrado
    print("Camino encontrado:", ' -> '.join(sub_path))
else:
    print("No se encontró un camino entre", start_vertex, "y", end_vertex)