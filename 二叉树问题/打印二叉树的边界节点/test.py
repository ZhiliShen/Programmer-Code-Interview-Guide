# -*- coding: utf-8 -*- #
# @Time    : 2021-05-21 17:18
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
from typing import List
from 二叉树问题.utils.utils import Node, build_tree_from_txt, build_tree_from_stdin, print_list


def print_edge_1(head: Node):  # TODO P101
    res = []
    if head is None:
        return res
    height = get_height(head)
    edge_map = [[None, None] for _ in range(height)]
    set_edge_map(head, 0, edge_map)
    for i in edge_map:
        res.append(i[0])
    print_leaf_not_in_map(head, 0, edge_map, res)
    for i in reversed(edge_map):
        if i[-1] != i[0]:
            res.append(i[-1])
    return res


def print_leaf_not_in_map(head: Node, height: int, edge_map, res: List):
    if head is None:
        return
    if head.left is None and head.right is None and head.value != edge_map[height][0] and head.value != \
            edge_map[height][-1]:
        res.append(head.value)
    print_leaf_not_in_map(head.left, height + 1, edge_map, res)
    print_leaf_not_in_map(head.right, height + 1, edge_map, res)


def set_edge_map(head: Node, height: int, edge_map: List[List]):
    if head is None:
        return
    edge_map[height][0] = head.value if edge_map[height][0] is None else edge_map[height][0]
    edge_map[height][-1] = head.value
    set_edge_map(head.left, height + 1, edge_map)
    set_edge_map(head.right, height + 1, edge_map)


def get_height(head: Node):
    if head is None:
        return 0
    return max(get_height(head.left) + 1, get_height(head.right) + 1)


def print_edge_2(head: Node):  # TODO P103
    res = []
    if head is None:
        return res
    res.append(head.value)
    if head.left is not None and head.right is not None:
        print_left_edge(head.left, True, res)
        print_right_edge(head.right, True, res)
    else:
        print_edge_2(head.left if head.left is not None else head.right)
    return res


def print_left_edge(head: Node, flag: bool, res: List):
    if head is None:
        return
    if flag or head.left is None and head.right is None:
        res.append(head.value)
    print_left_edge(head.left, flag, res)
    print_left_edge(head.right, flag and True if head.left is None else False, res)


def print_right_edge(head: Node, flag: bool, res: List):
    if head is None:
        return
    print_right_edge(head.left, flag and True if head.right is None else False, res)
    print_right_edge(head.right, flag, res)
    if flag or head.left is None and head.right is None:
        res.append(head.value)


if __name__ == "__main__":
    tree = build_tree_from_txt()
    # tree = build_tree_from_stdin()

    print_list(print_edge_1(tree.head))
    print_list(print_edge_2(tree.head))
