# -*- coding: utf-8 -*- #
# @Time    : 2021/8/17 16:56
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
from 二叉树问题.utils.utils import Node, build_tree_from_txt


def bs(node: Node, l: int, h: int):
    if h == l:
        return 1
    if most_left_level(node.right, l) < h:
        return pow(2, h-l-1) - 1 + 1 + bs(node.left, l+1, h)
    else:
        return pow(2, h-l) - 1 + 1 + bs(node.right, l+1, h)


def most_left_level(node: Node, level: int):
    if node is None:
        return level
    return most_left_level(node.left, level+1)


def node_num(head: Node):
    if head is None:
        return 0
    return bs(head, 1, most_left_level(head, 0))


if __name__ == "__main__":
    tree = build_tree_from_txt()
    print(node_num(tree.head))
