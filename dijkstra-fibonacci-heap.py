from fibonacci_heap_mod import Fibonacci_heap

# Sample graph: adjacency list with travel times (weights)
graph = {
    "warehouse": {"A": 3, "B": 1},
    "A": {"C": 3, "D": 4},
    "B": {"A": 1, "D": 2},
    "C": {"D": 1, "delivery1": 6},
    "D": {"delivery1": 2, "delivery2": 4},
    "delivery1": {},
    "delivery2": {}
}

graph2 = {
    "warehouse": {"A": 2},
    "A": {"B": 3},
    "B": {},
    "C": {}  # Unreachable node test
}
infinity = 1e9

#Dijkstra's algorithm using a Fibonacci Heap
def dijkstra_with_fib_heap(graph, start):
    heap = Fibonacci_heap()
    nodes = {}
    distances = {}
    parents = {}
    processed = set()

    for vertex in graph:
        if vertex == start:
            node = heap.enqueue(vertex, 0)
            distances[vertex] = 0
        else:
            node = heap.enqueue(vertex, infinity)
            distances[vertex] = infinity
        nodes[vertex] = node
        parents[vertex] = None

    while True:
        try:
            current = heap.dequeue_min()
        except:
            break  #Heap is empty

        if current is None:
            break

        current_node = current.get_value()
        if current_node in processed:
            continue
        current_distance = distances[current_node]

        for neighbor, weight in graph[current_node].items():
            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                parents[neighbor] = current_node
                heap.decrease_key(nodes[neighbor], new_distance)

        processed.add(current_node)

    return distances, parents

#Reconstructs the path from the source to the given end node
def reconstruct_path(parents, end):
    path = []
    while end is not None:
        path.append(end)
        end = parents[end]
    return list(reversed(path))

# Run dijkstra_with_fib_heap
distances, parents = dijkstra_with_fib_heap(graph, "warehouse")

# Print results
print("Shortest paths from warehouse:\n")
for node in distances:
    path = reconstruct_path(parents, node)
    print(f"{node}: Distance = {distances[node]}, Path = {' -> '.join(path)}")