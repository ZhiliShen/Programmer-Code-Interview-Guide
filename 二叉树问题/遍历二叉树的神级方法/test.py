# -*- coding: utf-8 -*- # 
# @Time    : 2021-05-23 15:16
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
from typing import List
from collections import deque
from 二叉树问题.utils.utils import Node, build_tree_from_txt, build_tree_from_stdin, print_list


def morris(head: Node):
    if head is None:
        return
    cur = head
    while cur:
        most_right = cur.left
        if most_right is not None:
            while most_right.right is not None and most_right.right != cur:
                most_right = most_right.right
            if most_right.right is None:
                most_right.right = cur
                cur = cur.left
            else:
                most_right.right = None
                cur = cur.right
        else:
            cur = cur.right


def morris_pre(head: Node):
    res = []
    if head is None:
        return res
    cur = head
    while cur:
        most_right = cur.left
        if most_right is not None:
            while most_right.right is not None and most_right.right != cur:
                most_right = most_right.right
            if most_right.right is None:  # most_right.right!
                res.append(cur.value)
                most_right.right = cur
                cur = cur.left
            else:
                most_right.right = None
                cur = cur.right
        else:
            res.append(cur.value)
            cur = cur.right
    return res


def morris_in(head: Node):
    res = []
    if head is None:
        return res
    cur = head
    while cur:
        most_right = cur.left
        if most_right is not None:
            while most_right.right is not None and most_right.right != cur:
                most_right = most_right.right
            if most_right.right is None:
                most_right.right = cur
                cur = cur.left
            else:
                most_right.right = None
                res.append(cur.value)
                cur = cur.right
        else:
            res.append(cur.value)
            cur = cur.right
    return res


def morris_pos(head: Node):
    res = []
    if head is None:
        return res
    cur = head
    while cur:
        most_right = cur.left
        if most_right is not None:
            while most_right.right is not None and most_right.right != cur:
                most_right = most_right.right
            if most_right.right is None:
                most_right.right = cur
                cur = cur.left
            else:
                most_right.right = None
                print_edge(cur.left, res)
                cur = cur.right
        else:
            cur = cur.right
    print_edge(head, res)
    return res


def print_edge(head: Node, res):
    tail = reverse_edge(head)
    cur = tail
    while cur is not None:
        res.append(cur.value)
        cur = cur.right
    reverse_edge(tail)


def reverse_edge(cur: Node):
    pre = None
    while cur:
        next = cur.right
        cur.right = pre
        pre = cur
        cur = next
    return pre  # pre! not cur!


if __name__ == "__main__":
    tree = build_tree_from_txt()
    # tree = build_tree_from_stdin()

    print_list(morris_pre(tree.head))
    print_list(morris_in(tree.head))
    print_list(morris_pos(tree.head))
