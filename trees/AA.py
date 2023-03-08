#!/usr/bin/env python3


class Node:
    """A node of tree."""

    def __init__(self, k: int, v: int, lvl: int, left, right):
        """Create a node."""
        self.key = k
        self.val = v
        self.level = lvl
        self.left = left
        self.right = right


def insert(root: Node, k: int, v: int) -> Node:
    """Insert a node with key=k and value=v into root."""
    if root is None:
        return Node(k, v, 1, None, None)
    elif k < root.key:
        root.left = insert(root.left, k,v)
        return split(skew(root))
    else:
        root.right = insert(root.right, k,v)
        return split(skew(root))


def remove(root: Node, k: int) -> Node:
    """Remove a node with key=k from root."""
    if root is not None:
        if root.key == k:
            if root.left is not None and root.right is not None:
                heir = root.left
                while heir.right is not None:
                    heir = heir.right
                root.key = heir.key
                root.val = heir.val
                root.left = remove(root.left, root.key)
            elif root.left is None:
                root = root.right
            else:
                root = root.left
        elif k < root.key:
            root.left = remove(root.left, k)
        else:
            root.right = remove(root.right, k)
        root = level_down(root)
        root = split(skew(root))
    return root


def lookup(root: Node, k: int) -> Node:
    """Look up a node with key=k."""
    if root is None:
        return None
    elif k < root.key:
        return lookup(root.left, k)
    elif k > root.key:
        return lookup(root.right, k)
    else:
        return root


def minimum(root: Node) -> Node:
    """Minimum in a tree."""
    if root is None:
        return None
    p = root
    while p.right is not None:
        p = p.right
    return p


def maximum(root: Node) -> Node:
    """Maximum in a tree."""
    if root is None:
        return None
    p = root
    while p.left is not None:
        p = p.left
    return p


# TODO: add implementation
def succ(root: Node, k: int) -> Node:
    """Return successor of a node key=k."""
    return None


# TODO: add implementation
def pred(root: Node, k: int) -> Node:
    """Return predesessor of a node key=k."""
    return None


def skew(root: Node) -> Node:
    r"""Skew a tree.

    |          |               |
    |    L <-- T               L -> T
    |   / \\    \\       =>   /    / \\
    |  A   B     R           A    B   R
    """
    if root is None or root.left is None:
        return root
    if root.left.level == root.level:
        tmp = root
        root = root.left
        tmp.left = root.right
        root.right = tmp
    root.right = skew(root.right)
    return root


def split(root: Node) -> Node:
    r"""Split a tree.

    |    |                        |
    |    T -> R -> X              R
    |   /    /           =>      / \\
    |  A    B                   T   X
    |                          / \\
    |                         A   B
    """
    if root is None or root.right is None or root.right.right is None:
        return root
    if root.right.right.level == root.level:
        tmp = root
        root = root.right
        tmp.right = root.left
        root.left = tmp
        root.level += 1
        root.right = split(root.right)
    return root


def level_down(root: Node) -> Node:
    """Level down a tree."""
    if root is None:
        return root
    if root.left is not None and root.left.level < root.level - 1 or \
       root.right is not None and root.right.level < root.level - 1:
        root.level -= 1
        if root.right is not None and root.right.level > root.level:
            root.right.level = root.level
    return root


def print_node(n: Node):
    """Print a node. Print -1 if None."""
    if n is None:
        print(-1)
    else:
        print(n.val, n.key)


def print_tree(root: Node):
    """Print a tree."""
    stack = list()
    stack.append({'node': root, 'level': 0})
    while len(stack) > 0:
        cur = stack.pop()
        level = cur['level']
        node = cur['node']
        indentation = ''.join([' ' for _ in range(2*level)])
        if node is not None:
            print(indentation, node.key, ':', node.val, ' @', node.level)
            stack.append({'node': node.right, 'level': level+1})
            stack.append({'node': node.left, 'level': level+1})
        else:
            print(indentation, 'None')


