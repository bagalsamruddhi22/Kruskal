class DisjointSet:
    def _init_(self, n):
        self.parent = [i for i in range(n)]

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.parent[root_v] = root_u
            return True
        return False

class Graph:
    def _init_(self):
        self.V = int(input("Enter number of vertices: "))
        E = int(input("Enter number of edges: "))
        self.edges = []
        print("Enter each edge in the format: u v weight")
        for _ in range(E):
            u, v, w = map(int, input().split())
            self.add_edge(u, v, w)

    def add_edge(self, u, v, weight):
        self.edges.append((weight, u, v))

    def kruskal_mst(self):
        self.edges.sort()
        ds = DisjointSet(self.V)
        mst = []
        mst_cost = 0

        for weight, u, v in self.edges:
            if ds.union(u, v):
                mst.append((u, v, weight))
                mst_cost += weight

        print("Edges in the Minimum Spanning Tree:")
        for u, v, weight in mst:
            print(f"{u} -- {v} == {weight}")
        print("Total cost of MST:", mst_cost)

# Sample usage
print("Kruskal's Algorithm - Greedy MST:\n")
g = Graph()
g.kruskal_mst()
