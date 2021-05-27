# -*- coding: utf-8 -*- # 
# @Time    : 2021-05-23 12:14
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
from typing import List
from collections import deque
from 二叉树问题.utils.utils import Node, build_tree_from_txt


def serial_by_pre(head: Node):
    if head is None:
        return "#!"
    res = str(head.value) + "!"
    res += serial_by_pre(head.left)
    res += serial_by_pre(head.right)
    return res


def recon_by_pre_string(pre_str: str):
    node_res = pre_str.split("!")
    node_res = node_res[:-1]
    return recon_pre_order(node_res)


def recon_pre_order(queue: List):
    value = queue.pop(0)
    if value == "#":
        return
    head = Node(int(value))
    head.left = recon_pre_order(queue)
    head.right = recon_pre_order(queue)
    return head


def serial_by_level(head: Node):
    if head is None:
        return "#!"
    res = str(head.value) + "!"
    queue = deque()
    queue.append(head)
    while queue:
        head = queue.popleft()
        if head.left is not None:
            res += str(head.left.value) + "!"
            queue.append(head.left)
        else:
            res += "#!"
        if head.right is not None:
            res += str(head.right.value) + "!"
            queue.append(head.right)
        else:
            res += "#!"
    return res


def recon_by_level_string(level_str: str):
    node_res = level_str.split("!")
    node_res = node_res[:-1]
    head = gen_node_by_string(node_res.pop(0))
    queue = deque()
    if head is not None:
        queue.append(head)
    while queue:
        node = queue.popleft()
        node.left = gen_node_by_string(node_res.pop(0))
        node.right = gen_node_by_string(node_res.pop(0))
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return head


def gen_node_by_string(val: str):
    if val == "#":
        return None
    return Node(int(val))


if __name__ == "__main__":
    tree = build_tree_from_txt()

    print(serial_by_pre(tree.head))
    print(serial_by_level(tree.head))
