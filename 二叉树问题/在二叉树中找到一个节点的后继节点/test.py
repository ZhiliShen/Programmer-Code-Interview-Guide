# -*- coding: utf-8 -*- #
# @Time    : 2021/7/22 18:38
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
class Node:
    def __init__(self, value, left, right, parent):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def get_next_node(node: Node):
    if node is None:
        return None
    if node.right is not None:
        return get_most_left(node.right)
    else:
        parent = node.parent
        while parent is not None and parent.left != node:
            node = parent
            parent = parent.parent
        return parent


def get_most_left(node: Node):
    if node is None:
        return node
    most_left = node
    while most_left.left is not None:
        most_left = most_left.left
    return most_left
