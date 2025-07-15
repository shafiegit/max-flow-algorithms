from collections import deque

def edmonds_karp(graph, source, sink):
    flow = 0
    residual = {u: {v: cap for v, cap in adj.items()} for u, adj in graph.items()}
    for u in list(graph.keys()):
        for v in graph[u]:
            if v not in residual:
                residual[v] = {}
            if u not in residual[v]:
                residual[v][u] = 0
    while True:
        parent = {node: None for node in residual}
        parent[source] = source
        bottleneck = {node: 0 for node in residual}
        bottleneck[source] = float('inf')
        queue = deque([source])
        found_path = False
        while queue and not found_path:
            u = queue.popleft()
            for v, cap in residual[u].items():
                if cap > 0 and parent[v] is None:
                    parent[v] = u
                    bottleneck[v] = min(bottleneck[u], cap)
                    if v == sink:
                        found_path = True
                        break
                    queue.append(v)
        if not found_path:
            break
        flow += bottleneck[sink]
        v = sink
        while v != source:
            u = parent[v]
            residual[u][v] -= bottleneck[sink]
            residual[v][u] += bottleneck[sink]
            v = u
    return flow

# Example usage:
graph = {
    's': {'A': 5, 'B': 2},
    'A': {'B': 2, 'C': 3},
    'B': {'D': 4},
    'C': {'D': 1, 'T': 2},
    'D': {'T': 5},
    'T': {}
}
max_flow_value = edmonds_karp(graph, 's', 'T')
print("Max Flow =", max_flow_value)
