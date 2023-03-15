#!/usr/bin/env python3

def edge_list_to_adj_matrix(v: int, edges: list[(int, int)]) -> list[list[bool]]:
    """Convert list of edges to adjacency matrix."""
    mas = [[False for _ in range(v)] for _ in range(v)]
    for i, j in edges:
        mas[i][j] = True
    return mas


def adj_matrix_to_adj_lists(a: list[list[bool]]) -> list[list[int]]:
    """Convert adjacency matrix to adjacency lists."""
    pass


if __name__ == '__main__':
    a = edge_list_to_adj_matrix(3, [(0,1), (1,2)])
    print(a)
    print(adj_matrix_to_adj_lists(a))
