import heapq
from collections import deque

class Graph:
    def __init__(self, V=(), E=()):
        """Initialize the graph with vertices and edges."""
        self.vertices = set(V)
        self.edges = {v: {} for v in self.vertices}
        for u, v, weight in E:
            self.add_edge(u, v, weight)

    def add_vertex(self, v):
        """Add a vertex if it doesn't exist."""
        if v not in self.vertices:
            self.vertices.add(v)
            self.edges[v] = {}

    def remove_vertex(self, v):
        """Remove a vertex and its associated edges."""
        if v in self.vertices:
            self.vertices.remove(v)
            self.edges.pop(v, None)
            for u in self.edges:
                if v in self.edges[u]:
                    del self.edges[u][v]

    def add_edge(self, u, v, weight):
        """Add an undirected edge between u and v with the given weight."""
        self.add_vertex(u)
        self.add_vertex(v)
        self.edges[u][v] = weight
        self.edges[v][u] = weight

    def remove_edge(self, u, v, weight):
        """Remove the edge between u and v if the weight matches."""
        if (u in self.edges and v in self.edges[u] and 
            self.edges[u][v] == weight):
            del self.edges[u][v]
            del self.edges[v][u]

    def nbrs(self, v):
        """Return an iterator over the neighbors of vertex v."""
        return iter(self.edges.get(v, {}))

    def fewest_flights(self, city):
        """
        Uses Breadth-First Search (BFS) to compute for each vertex 
        the predecessor in the path from the source city minimizing stops.
        """
        visited = {city: None}
        queue = deque([city])
        while queue:
            current = queue.popleft()
            for nbr in self.nbrs(current):
                if nbr not in visited:
                    visited[nbr] = current
                    queue.append(nbr)
        return visited

    def shortest_path(self, city):
        """
        Uses Dijkstra's algorithm to compute the shortest path (by distance)
        from the source city to every other vertex.
        Returns a dictionary mapping vertex to (predecessor, total_distance).
        """
        dist = {v: float('inf') for v in self.vertices}
        prev = {v: None for v in self.vertices}
        dist[city] = 0
        heap = [(0, city)]
        
        while heap:
            current_dist, current = heapq.heappop(heap)
            if current_dist > dist[current]:
                continue
            for nbr in self.nbrs(current):
                weight = self.edges[current][nbr]
                new_dist = current_dist + weight
                if new_dist < dist[nbr]:
                    dist[nbr] = new_dist
                    prev[nbr] = current
                    heapq.heappush(heap, (new_dist, nbr))
                    
        return {v: (prev[v], dist[v]) for v in self.vertices}

    def minimum_salt(self, city):
        """
        Uses Prim's algorithm to compute the Minimum Spanning Tree (MST)
        starting from the source city. The MST minimizes the total miles used
        (or "salt" in a winter roads analogy).
        
        Returns a tuple:
         - path_tree: dict with key = (u, v) edge and value = weight of that edge.
         - vertex_weights: dict mapping each vertex to the weight of the edge
                           connecting it into the MST (0 for the source).
        """
        visited = set()
        path_tree = {}
        vertex_weights = {}
        heap = [(0, city, None)]
        
        while heap:
            weight, current, prev = heapq.heappop(heap)
            if current in visited:
                continue
            visited.add(current)
            vertex_weights[current] = weight
            if prev is not None:
                path_tree[(prev, current)] = weight
            for nbr, edge_weight in self.edges[current].items():
                if nbr not in visited:
                    heapq.heappush(heap, (edge_weight, nbr, current))
        return path_tree, vertex_weights