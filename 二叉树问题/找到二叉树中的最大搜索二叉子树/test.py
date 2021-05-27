# -*- coding: utf-8 -*- # 
# @Time    : 2021-05-26 12:47
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
from typing import List
from 二叉树问题.utils.utils import Node, build_tree_from_txt, build_tree_from_stdin, print_list


class return_type:
    def __init__(self, max_bst_head: Node, max_bst_size: int, min_value: float, max_value: float):
        self.max_bst_head = max_bst_head
        self.max_bst_size = max_bst_size
        self.min_value = min_value
        self.max_value = max_value


def process(x: Node) -> return_type:
    if x is None:
        return return_type(None, 0, float('inf'), float('-inf'))
    l_data = process(x.left)
    r_data = process(x.right)
    min_value = min(x.value, l_data.min_value, r_data.min_value)  # x.value!
    max_value = max(x.value,l_data.max_value, r_data.max_value)  # x.value!
    max_bst_size = max(l_data.max_bst_size, r_data.max_bst_size)
    max_bst_head = l_data.max_bst_head if l_data.max_bst_size >= r_data.max_bst_size else r_data.max_bst_head
    if l_data.max_bst_head == x.left and r_data.max_bst_head == x.right and l_data.max_value < x.value < r_data.min_value:
        max_bst_size = l_data.max_bst_size + r_data.max_bst_size + 1
        max_bst_head = x
    return return_type(max_bst_head, max_bst_size, min_value, max_value)


def get_max_bst(head: Node):
    return process(head).max_bst_size


if __name__ == "__main__":
    tree = build_tree_from_txt()
    # tree = build_tree_from_stdin()

    print(get_max_bst(tree.head))
