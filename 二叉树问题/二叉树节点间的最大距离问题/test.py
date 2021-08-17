# -*- coding: utf-8 -*- #
# @Time    : 2021/8/6 16:12
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
import sys
from 二叉树问题.utils.utils import Node, build_tree_from_txt, build_tree_from_stdin, print_list
from 二叉树问题.如何较为直观地打印二叉树.test import print_tree


class ReturnType:
    def __init__(self, height, max_distance):
        self.height = height
        self.max_distance = max_distance


def process(node: Node):
    if node is None:
        return ReturnType(0, 0)
    left, right = process(node.left), process(node.right)
    height = max(left.height, right.height) + 1
    left_max_distance = left.max_distance
    right_max_distance = right.max_distance
    max_distance = max(left_max_distance, right_max_distance, left.height+right.height+1)
    return ReturnType(height, max_distance)


def get_max_distance(head: Node):
    return process(head).max_distance


if __name__ == "__main__":
    tree = build_tree_from_stdin()
    print(get_max_distance(tree.head))
