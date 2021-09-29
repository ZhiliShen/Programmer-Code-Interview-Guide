# -*- coding: utf-8 -*- #
# @Time    : 2021/7/20 11:08
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
from 二叉树问题.utils.utils import Node, build_2_tree_from_txt
from 二叉树问题.二叉树的序列化和反序列化.test import serial_by_pre
from 其他题目.KMP算法.test import search


def contains(t1: Node, t2: Node):
    if t2 is None:
        return True
    if t1 is None:
        return False
    return check(t1, t2) or contains(t1.left, t2) or contains(t1.right, t2)


def check(head: Node, t2: Node):
    if t2 is None and head is None:
        return True
    if t2 is None and head is not None:
        return False
    if t2 is not None and head is None:
        return False
    return (True if head.value == t2.value else False) and check(head.left, t2.left) and check(head.right, t2.right)


if __name__ == "__main__":
    if -1 in search(*map(serial_by_pre, [tree.head for tree in build_2_tree_from_txt()])):
        print(False)
    else:
        print(True)

