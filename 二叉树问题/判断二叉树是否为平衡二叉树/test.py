# -*- coding: utf-8 -*- #
# @Time    : 2021/7/21 12:01
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
from typing import List
from 二叉树问题.utils.utils import Node, build_tree_from_txt, build_tree_from_stdin, print_list


class ReturnType:
    def __init__(self, isAVL: bool, height: int):
        self.isAVL = isAVL
        self.height = height


def process(x: Node):
    if x is None:
        return ReturnType(True, 0)
    left_info = process(x.left)
    right_info = process(x.right)
    return ReturnType(left_info.isAVL and right_info.isAVL and abs(left_info.height - right_info.height) <= 1,
                      max(left_info.height, right_info.height) + 1)


def is_AVL(h: Node):
    return process(h).isAVL


if __name__ == "__main__":
    tree = build_tree_from_txt()
    if is_AVL(tree.head):
        print("true")
    else:
        print("false")
