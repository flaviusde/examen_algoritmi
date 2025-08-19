# Problema 8 – Bonus (15p) – Clasa Graph

from collections import deque
from typing import Dict, List
import heapq


class Graph:
    def __init__(self):
        self.adj: Dict[str, List[str]] = {}

    def add_node(self, v: str):
        self.adj[v].append("")

    def add_edge(self, u: str, v: str, undirected: bool = True):
        self.adj[].append([u, v, undirected])

    def bfs(self, start: str) -> List[str]:
        visited = set()
        coada = deque(start)

        while coada:
            node = coada.popleft()
            if node not in visited:
                #procesez nodul
                visited.add(node)
                for neighbor in self.adj[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
        return []

    def shortest_path(self, start: str, end: str) -> List[str]:
        # m-am gandit ca poate ar merge Dijaskra.
        # M-am gandit si la Kruskal dar nu avem distante pe muchii. Sigur e ceva ce nu inteleg
        dist = {nod: float("inf") for nod in self.adj}
        dist[start] = 0
        heap = [start]

        while heap:
            current_dist, current_node = heapq.heappop(heap)
            for neighbor, distance in self.adj[current_node]:
                if current_dist + distance < dist[neighbor]:
                    dist[neighbor] = current_dist + distance
                    heapq.heappush(heap, (dist[neighbor], neighbor))
        return dist

if __name__ == "__main__":
    g = Graph()
    # TODO: test
