# python-scripts/dijkstra.py

import sys
import json
import heapq

def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    path = {node: None for node in graph}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                path[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, path

if __name__ == "__main__":
    # Reading JSON data from stdin
    data = json.loads(sys.stdin.read())
    graph = data['graph']
    start = data['start']
    distances, path = dijkstra(graph, start)
    result = {'distances': distances, 'path': path}
    print(json.dumps(result))  # Output the result as JSON
