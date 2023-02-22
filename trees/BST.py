#!/usr/bin/env python3


class Node:
    def __init__(self, x, left, right):
        self.val = x
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.root = None
    def insert(self, x):
        """inserts x into tree"""
        if self.root is None:
            self.root = Node(x, None, None)
        else:
            p = self.root
            q = self.root
            while p is not None:
                q = p
                if x < p.val:
                    p = p.left
                else:
                    p = p.right
            if x < q.val:
                q.left = Node(x, None, None)
            else:
                q.right = Node(x, None, None)
    def lookup(self, x) -> bool:
        """returns, whether x is in tree"""
        p = self.root
        while p is not None:
            if p.val == x:
                return True
            elif x < p.val:
                p = p.left
            else:
                p = p.right
        return False

    def print_tree(self):
        """
        print_tree outputs a tree in the following format:

        3
          2
            1
              None
              None
            None
          5
            4
              None
              None
            6
              None
              None
        """
        stack = list()
        stack.append({'node': self.root, 'level': 0})
        while len(stack) > 0:
            cur = stack.pop()
            level = cur['level']
            node = cur['node']
            indentation = ''.join([' ' for _ in range(2*level)])
            if node is not None:
                print(indentation, node.val)
                stack.append({'node': node.right, 'level': level+1})
                stack.append({'node': node.left, 'level': level+1})
            else:
                print(indentation, 'None')


if __name__ == '__main__':
    t = Tree()
    # t.insert(3)
    # t.print_tree()
    # print("--------------")

    # t.insert(2)
    # t.print_tree()
    # print("--------------")

    # t.insert(5)
    # t.print_tree()
    # print("--------------")

    # t.insert(1)
    # t.print_tree()
    # print("--------------")

    # t.insert(4)
    # t.print_tree()
    # print("--------------")

    # t.insert(4)
    # t.print_tree()

    # for i in range(5):
    #     t.insert(i)
    # t.print_tree()

    for i in [10,14,52,1,45,13,9]:
        t.insert(i)
    print('Is 10 in tree? ', t.lookup(10))
    print('Is 52 in tree? ', t.lookup(52))
    print('Is 3 in tree? ', t.lookup(3))
