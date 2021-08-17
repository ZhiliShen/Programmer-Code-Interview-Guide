# -*- coding: utf-8 -*- #
# @Time    : 2021/7/23 18:30
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test2.py
# @Notice  :
import sys
from 二叉树问题.utils.utils import Node, build_tree_from_txt, build_tree_from_stdin, print_list


class Record:
    def __init__(self, head: Node):
        self.dic = {}
        if head is not None:
            self.dic[head.value] = None
        self.set_map(head)

    def set_map(self, node: Node):
        if node is None:
            return
        if node.left is not None:
            self.dic[node.left.value] = node.value
        if node.right is not None:
            self.dic[node.right.value] = node.value
        self.set_map(node.left)
        self.set_map(node.right)

    def query(self, node1: int, node2: int):
        path = set()
        while node1 is not None:
            path.add(node1)
            node1 = self.dic[node1]
        while node2 is not None:
            if node2 in path:
                return node2
            node2 = self.dic[node2]


if __name__ == "__main__":
    tree = build_tree_from_stdin()
    record = Record(tree.head)
    num = int(sys.stdin.readline())
    for _ in range(num):
        o1, o2 = (int(k) for k in sys.stdin.readline().split(" "))
        print(record.query(o1, o2))
