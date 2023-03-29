#!/usr/bin/env python3


def edge_list_to_adj_matrix(v: int, edges: list[(int, int)]) -> list[list[bool]]:
    """Convert list of edges to adjacency matrix."""
    mas = [[False for _ in range(v)] for _ in range(v)]
    for i, j in edges:
        mas[i][j] = True
    return mas


def adj_matrix_to_adj_lists(a: list[list[bool]]) -> list[list[int]]:
    """Convert adjacency matrix to adjacency lists."""
    v = len(a)
    r = []
    for i in range(v):
        ri = []
        for j in range(v):
            if a[i][j]:
                ri.append(j)
        r.append(ri)
    return r


def adj_lists_to_edge_list(a: list[list[int]]) -> list[(int,int)]:
    """Convert adjacency list to edge list."""
    m = []
    for i in range(len(a)):
        for j in a[i]:
            m.append((i,j))
    return m


if __name__ == '__main__':
    a = edge_list_to_adj_matrix(3, [(0,1), (1,2)])
    print(a)
    b = adj_matrix_to_adj_lists(a)
    print(b)
    c = adj_lists_to_edge_list(b)
    print(c)
