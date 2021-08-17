# -*- coding: utf-8 -*- #
# @Time    : 2021/8/16 11:15
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test2.py
# @Notice  :
from 二叉树问题.utils.utils import Node


def generate(start: int, end: int):
    res = []
    if start > end:
        res.append(None)
    for i in range(start, end + 1):
        left_sub = generate(start, i - 1)
        right_sub = generate(i + 1, end)
        for left_node in left_sub:
            for right_node in right_sub:
                head = Node(i)
                head.left = left_node
                head.right = right_node
                res.append(head)
    return res


def clone_tree(head: Node):  # only use while head = Node(i) in first circle
    if head is None:
        return None
    res = Node(head.value)
    res.left = clone_tree(head.left)
    res.right = clone_tree(head.right)
    return res


def generate_trees(n: int):
    return generate(1, n)

