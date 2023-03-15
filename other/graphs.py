#!/usr/bin/env python3

def edge_list_to_adj_matrix(v: int, edges: list[(int, int)]) -> list[list[bool]]:
    """Convert list of edges to adjacency matrix."""
    mas = [[False for _ in range(v)] for _ in range(v)]
    for i, j in edges:
        mas[i][j] = True
    return mas


if __name__ == '__main__':
    print(edge_list_to_adj_matrix(3, [(0,1), (1,2)]))
