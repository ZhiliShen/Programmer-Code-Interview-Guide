# -*- coding: utf-8 -*- #
# @Time    : 2021/7/23 19:19
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test3.py
# @Notice  :
import sys
from 二叉树问题.utils.utils import Node, build_tree_from_txt, build_tree_from_stdin, print_list
from 二叉树问题.如何较为直观地打印二叉树.test import print_tree


class Record:
    def __init__(self, head: Node):
        self.dict = {}
        self.init_dict(head)
        self.set_dict(head)

    def init_dict(self, node: Node):
        if node is None:
            return
        self.dict[node.value] = {}
        self.init_dict(node.left)
        self.init_dict(node.right)

    def set_dict(self, node: Node):
        if node is None:
            return
        self.head_record(node.left, node)
        self.head_record(node.right, node)
        self.sub_record(node)
        self.set_dict(node.left)
        self.set_dict(node.right)

    def head_record(self, child: Node, parent: Node):
        if child is None:
            return
        self.dict[child.value][parent.value] = parent.value
        self.head_record(child.left, parent)
        self.head_record(child.right, parent)

    def sub_record(self, node: Node):
        if node is None:
            return
        self.sub_record_left(node.left, node.right, node)

    def sub_record_left(self, left: Node, right: Node, parent: Node):
        if left is None:
            return
        self.sub_record_right(left, right, parent)
        self.sub_record_left(left.left, right, parent)
        self.sub_record_left(left.right, right, parent)

    def sub_record_right(self, left: Node, right: Node, parent: Node):
        if right is None:
            return
        self.dict[left.value][right.value] = parent.value
        self.sub_record_left(left, right.left, parent)
        self.sub_record_left(left, right.right, parent)

    def query(self, o1: int, o2: int):
        if o1 == o2:
            return o1
        if self.dict[o1].get(o2, None) is None:
            return self.dict[o2][o1]
        else:
            return self.dict[o1][o2]


if __name__ == "__main__":
    tree = build_tree_from_txt()
    record = Record(tree.head)
    num = int(sys.stdin.readline())
    for _ in range(num):
        o1, o2 = (int(k) for k in sys.stdin.readline().split(" "))
        print(record.query(o1, o2))
