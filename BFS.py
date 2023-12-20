from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, vertex, neighbors):
        self.graph[vertex] = neighbors

    def bfs(self, start):
        visited = set()
        queue = deque([start])

        while queue:
            current_vertex = queue.popleft()
            if current_vertex not in visited:
                print(current_vertex, end=" ")
                visited.add(current_vertex)
                queue.extend(neighbor for neighbor in self.graph[current_vertex] if neighbor not in visited)

# Example usage:
g = Graph()
g.add_edge('A', ['B', 'C'])
g.add_edge('B', ['A', 'D', 'E'])
g.add_edge('C', ['A', 'F', 'G'])
g.add_edge('D', ['B'])
g.add_edge('E', ['B', 'F'])
g.add_edge('F', ['C', 'E'])
g.add_edge('G', ['C'])

print("BFS starting from vertex 'A':")
g.bfs('A')
