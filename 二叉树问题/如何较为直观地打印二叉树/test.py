# -*- coding: utf-8 -*- # 
# @Time    : 2021-05-23 11:35
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py.py
# @Notice  :
from 二叉树问题.utils.utils import Node, build_tree_from_txt, build_tree_from_stdin, print_list


def print_tree(head: Node):
    print("Binary Tree:")
    print_in_order(head, 0, 'H', 17)


def print_in_order(head: Node, height: int, to: str, length: int):
    if head is None:
        return
    print_in_order(head.right, height + 1, 'v', length)
    val = to + str(head.value) + to
    len_left = int((length - len(val)) / 2)
    len_right = length - len_left - len(val)
    res = [" " * height*length, " " * len_left, val, " " * len_right]
    print("".join(res))
    print_in_order(head.left, height+1, '^', length)


if __name__ == "__main__":
    tree = build_tree_from_txt()
    # tree = build_tree_from_stdin()

    print_tree(tree.head)
