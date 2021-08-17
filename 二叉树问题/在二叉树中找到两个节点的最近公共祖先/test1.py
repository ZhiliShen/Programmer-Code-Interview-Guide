# -*- coding: utf-8 -*- #
# @Time    : 2021/7/22 21:28
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test1.py
# @Notice  :
import sys
from 二叉树问题.utils.utils import Node, build_tree_from_txt, build_tree_from_stdin, print_list


def lowest_ancestor(head: Node, o1: int, o2: int):
    if head is None or head.value == o1 or head.value == o2:
        return head
    left = lowest_ancestor(head.left, o1, o2)
    right = lowest_ancestor(head.right, o1, o2)
    if left is not None and right is not None:  # means o1 and o2 cross in the node return the node
        return head
    if left is None and right is None:  # nothing has been found in the head
        return None
    return left if left is not None else right  # means one if child has found the lowest ancestor  this condition has
    # above condition so we can throw if left is None and right is None


if __name__ == "__main__":
    tree = build_tree_from_txt()
    o1, o2 = (int(k) for k in sys.stdin.readline().split(" "))
    print(lowest_ancestor(tree.head, o1, o2).value)
