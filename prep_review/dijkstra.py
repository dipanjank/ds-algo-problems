"""Dijkstra's Algorithm for Shortest path in a graph with positive weights."""
import heapq
from collections import defaultdict
from typing import List, Dict, Tuple


def shortest_path(vertices: List[int], edges: Dict[Tuple[int, int], int], source: int, dest: int):
    visited = {v: False for v in vertices}

    # tracks the shortest path from source to all other vertices
    # initially set all distances to +inf, except shortest_dists[source] = 0
    shortest_dists = {v: float("inf") for v in vertices}
    shortest_dists[source] = 0

    adj_list = defaultdict(set)
    for e in edges:
        adj_list[e[0]].add(e[1])

    # Priority queue to find the unvisited vertex with the smallest distance from source at every turn
    q = [(0, source)]

    while q:
        # u is the unvisited vertex with the smallest distance from source
        u = heapq.heappop(q)[1]
        visited[u] = True

        # For each unvisited neighbour v of u, check if shortest_dists[v] can be updated
        # this happens if shortest_dists[u] + the weight of the edge from u -> v is less than shortest_dists[v]
        # If this happens, add (sd_u + w, v) to the heap
        neighbours = [n for n in adj_list[u] if not visited[n]]
        sd_u = shortest_dists[u]
        for v in neighbours:
            w = edges[(u, v)]
            if sd_u + w < shortest_dists[v]:
                shortest_dists[v] = sd_u + w
                heapq.heappush(q, (sd_u + w, v))

    return shortest_dists[dest]



if __name__ == '__main__':
    vertices = [1, 2, 3, 4, 5, 6]
    edges = {
        (1, 2): 1,
        (2, 1): 1,
        (1, 3): 9,
        (3, 1): 9,
        (1, 6): 14,
        (6, 1): 14,
        (2, 3): 10,
        (3, 2): 10,
        (2, 4): 15,
        (4, 2): 15,
        (3, 4): 11,
        (4, 3): 11,
        (3, 6): 2,
        (6, 3): 2,
        (4, 5): 6,
        (5, 4): 6,
        (5, 6): 9,
        (6, 5): 9,
    }

    ans = shortest_path(vertices, edges, 1, 6)
    print(ans)
