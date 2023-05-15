from typing import List
from collections import defaultdict


def topsort(vertices: List[str], edges: List[List[str]]) -> List[str]:
    """Return a Topological ordering of the nodes in vertices of a Directed Graph."""
    top_ordering = []
    in_degrees = {v: 0 for v in vertices}

    # edges[i, j] -> an edge from vertex i to vertex j
    # adj_matrix[i] -> vertices which have an incoming edge from vertex i
    adj_matrix = defaultdict(set)
    for i, j in edges:
        in_degrees[j] += 1
        adj_matrix[i].add(j)

    # In each iteration, select the nodes with no incoming edge go in top_ordering
    while in_degrees:
        next_set = [v for v, count in in_degrees.items() if count == 0]
        if next_set:
            for u in next_set:
                # For every vertex with no incoming edge, add it to top_ordering
                # and decrement the top_ordering of every vertex connected to this vertex
                del in_degrees[u]
                for v in adj_matrix[u]:
                    in_degrees[v] -= 1
                top_ordering.append(u)
        else:
            # No node found with in-degree 0
            break

    if in_degrees:
        raise ValueError("Topological ordering is not possible.")

    return top_ordering


def main():
    v = list("ABCDE")
    e = [("A", "D"), ("C", "D"), ("E", "A"), ("E", "C"), ("A", "C"), ("B", "E"), ("B", "C")]
    top = topsort(v, e)
    print(top)


if __name__ == '__main__':
    main()
