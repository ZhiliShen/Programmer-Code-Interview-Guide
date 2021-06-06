# -*- coding: utf-8 -*- # 
# @Time    : 2021-06-04 19:15
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
from typing import List
from 二叉树问题.如何较为直观地打印二叉树.test import print_tree
from 二叉树问题.utils.utils import Node, build_2_tree_from_txt, build_tree_from_stdin, print_list
from collections import deque


def contains(t1: Node, t2: Node):
    if t2 is None:
        return True
    if t1 is None:
        return False
    return check(t1, t2) or contains(t1.left, t2) or contains(t1.right, t2)


def check(head: Node, t2: Node):
    if t2 is None:
        return True
    if head is None:
        return False
    return (True if head.value == t2.value else False) and check(head.left, t2.left) and check(head.right, t2.right)
    # can not write True if head.value == t2.value else False and check(head.left, t2.left) and check(head.right, t2.right)
    # python will treat it likes True if head.value == t2.value else (False and check(head.left, t2.left) and check(head.right, t2.right))


if __name__ == "__main__":
    tree_1, tree_2 = build_2_tree_from_txt()
    # tree_1, tree_2 = build_2_tree_from_stdin()

    print(str(contains(tree_1.head, tree_2.head)).lower())
