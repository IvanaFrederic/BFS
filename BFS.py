from collections import deque

def bfs(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    queue = deque([start])

    while queue:
        current_node = queue.popleft()
        print(f"Visiting node: {current_node}")

        for neighbor in graph[current_node]:
            if distances[neighbor] == float('inf'):
                distances[neighbor] = distances[current_node] + 1
                queue.append(neighbor)

    return distances

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}

start_node = 'A'
distances = bfs(graph, start_node)

print(f"\nDistances from node {start_node}: {distances}")
