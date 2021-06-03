# -*- coding: utf-8 -*- # 
# @Time    : 2021-06-02 16:01
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
from typing import List
from 二叉树问题.如何较为直观地打印二叉树.test import print_tree
from 二叉树问题.utils.utils import Node, build_tree_from_txt, build_tree_from_stdin, print_list
from collections import deque


def get_two_err_nodes(head: Node):
    res = [None, None]
    if head is None:
        return res
    stack = deque()
    pre = None
    while len(stack) != 0 or head is not None:
        if head is not None:
            stack.append(head)
            head = head.left
        else:
            head = stack.pop()
            if pre is not None and pre.value > head.value:
                res[0] = pre if res[0] is None else res[0]
                res[1] = head
            pre = head
            head = head.right
    return res


def get_two_err_nodes_parents(head: Node, e1: Node, e2: Node):
    parents = [None, None]
    if head is None:
        return parents
    stack = deque()
    while len(stack) != 0 or head is not None:
        if head is not None:
            stack.append(head)
            head = head.left
        else:
            head = stack.pop()
            if head.left == e1 or head.right == e1:
                parents[0] = head
            if head.left == e2 or head.right == e2:
                parents[1] = head
            head = head.right
    return parents


def recover_tree(head: Node):
    errs = get_two_err_nodes(head)
    parents = get_two_err_nodes_parents(head, errs[0], errs[1])
    e1 = errs[0]
    e1p = parents[0]
    e1l = e1.left
    e1r = e1.right
    e2 = errs[1]
    e2p = parents[1]
    e2l = e2.left
    e2r = e2.right
    if e1 == head:
        if e1 == e2p:
            e1.left = e2l
            e1.right = e2r
            e2.right = e1
            e2.left = e1l
        elif e2p.left == e2:
            e2p.left = e1
            e2.left = e1l
            e2.right = e1r
            e1.left = e2l
            e1.right = e2r
        else:
            e2p.right = e1
            e2.left = e1l
            e2.right = e1r
            e1.left = e2l
            e1.right = e2r
        head = e2
    elif e2 == head:
        if e2 == e1p:
            e2.left = e1l
            e2.right = e1r
            e1.left = e2
            e1.right = e2r
        elif e1p.left == e1:
            e1p.left = e2
            e1.left = e2l
            e1.right = e2r
            e2.left = e1l
            e2.right = e1r
        else:
            e1p.right = e2
            e1.left = e2l
            e1.right = e2r
            e2.left = e1l
            e2.right = e1r
        head = e1
    else:
        if e1 == e2p:
            if e1p.left == e1:
                e1p.left = e2
                e1.left = e2l
                e1.right = e2r
                e2.left = e1l
                e2.right = e1
            else:
                e1p.right = e2
                e1.left = e2l
                e1.right = e2r
                e2.left = e1l
                e2.right = e1
        elif e2 == e1p:
            if e2p.left == e2:
                e2p.left = e1
                e2.left = e1l
                e2.right = e1r
                e1.left = e2
                e1.right = e2r
            else:
                e2p.right = e1
                e2.left = e1l
                e2.right = e1r
                e1.left = e2
                e1.right = e2r
        else:
            if e1p.left == e1:
                if e2p.left == e2:
                    e1.left = e2l
                    e1.right = e2r
                    e2.left = e1l
                    e2.right = e1r
                    e1p.left = e2
                    e2p.left = e1
                else:
                    e1.left = e2l
                    e1.right = e2r
                    e2.left = e1l
                    e2.right = e1r
                    e1p.left = e2
                    e2p.right = e1
            else:
                if e2p.left == e2:
                    e1.left = e2l
                    e1.right = e2r
                    e2.left = e1l
                    e2.right = e1r
                    e1p.right = e2
                    e2p.left = e1
                else:
                    e1.left = e2l
                    e1.right = e2r
                    e2.left = e1l
                    e2.right = e1r
                    e1p.right = e2
                    e2p.right = e1
    return head


if __name__ == "__main__":
    tree = build_tree_from_txt()
    # tree = build_tree_from_stdin()

    print_tree(recover_tree(tree.head))
