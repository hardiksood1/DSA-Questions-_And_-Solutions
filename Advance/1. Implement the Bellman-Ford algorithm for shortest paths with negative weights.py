# 1.Implement the Bellman-Ford algorithm for shortest paths with negative weights.

# The Bellman-Ford Algorithm is used to find the shortest paths from a single source vertex to all other vertices in a weighted graph.
# Unlike Dijkstra’s, it can handle negative weight edges, and it also detects negative weight cycles.

class BellmanFord:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []  # List of edges in form (u, v, w)

    def add_edge(self, u, v, w):
        self.edges.append((u, v, w))

    def run(self, src):
        # Step 1: Initialize distances
        dist = [float("inf")] * self.V
        dist[src] = 0

        # Step 2: Relax all edges V-1 times
        for _ in range(self.V - 1):
            for u, v, w in self.edges:
                if dist[u] != float("inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # Step 3: Check for negative weight cycles
        for u, v, w in self.edges:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle!")
                return None

        return dist


# Example usage
if __name__ == "__main__":
    g = BellmanFord(5)  # 5 vertices (0 to 4)

    g.add_edge(0, 1, -1)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 2)
    g.add_edge(1, 4, 2)
    g.add_edge(3, 2, 5)
    g.add_edge(3, 1, 1)
    g.add_edge(4, 3, -3)

    dist = g.run(0)  # source = 0
    if dist:
        print("Vertex Distance from Source")
        for i in range(len(dist)):
            print(f"{i}\t {dist[i]}")


#Result

# Vertex Distance from Source
# 0        0 
# 1        -1
# 2        2 
# 3        -2
# 4        1 
