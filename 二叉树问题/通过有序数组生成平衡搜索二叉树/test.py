# -*- coding: utf-8 -*- #
# @Time    : 2021/7/22 18:25
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
import sys
from typing import List
from 二叉树问题.utils.utils import Node
from 二叉树问题.如何较为直观地打印二叉树.test import print_tree


def generate_tree(sort_arr: List):
    if len(sort_arr) == 0:
        return None
    return generate(sort_arr, 0, len(sort_arr) - 1)


def generate(sort_arr: List, start: int, end: int):
    if start > end:
        return None
    mid = start + (end - start) // 2
    node = Node(sort_arr[mid])
    node.left = generate(sort_arr, start, mid - 1)
    node.right = generate(sort_arr, mid + 1, end)
    return node


if __name__ == "__main__":
    sort_arr = [int(k) for k in sys.stdin.readline().split(" ")]
    head = generate_tree(sort_arr)
    print_tree(head)
