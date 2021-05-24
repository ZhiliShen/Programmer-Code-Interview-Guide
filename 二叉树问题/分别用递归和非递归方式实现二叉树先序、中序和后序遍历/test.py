# -*- coding: utf-8 -*- # 
# @Time    : 2021-05-20 14:41
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py.py
# @Notice  :
from typing import List
from collections import deque
from 二叉树问题.utils.utils import Node, build_tree_from_txt, build_tree_from_stdin, print_list


def pre_order(head: Node) -> List[int]:
    res = []
    # pre_order_recur(head, res)
    pre_order_un_recur(head, res)
    return res


def in_order(head: Node) -> List[int]:
    res = []
    # in_order_recur(head, res)
    in_order_un_recur(head, res)
    return res


def post_order(head: Node) -> List[int]:
    res = []
    # pre_order_recur(head, res)
    # post_order_un_recur_with2stack(head, res)
    # post_order_un_recur_with1stack_1(head, res)
    post_order_un_recur_with1stack_2(head, res)
    return res


def in_order_recur(head: Node, res: List):
    if head is None:
        return
    in_order_recur(head.left, res)
    res.append(head.value)
    in_order_recur(head.right, res)


def post_order_recur(head: Node, res: List):
    if head is None:
        return
    post_order_recur(head.left, res)
    post_order_recur(head.right, res)
    res.append(head.value)


def pre_order_recur(head: Node, res: List):
    if head is None:
        return
    res.append(head.value)
    pre_order_recur(head.left, res)
    pre_order_recur(head.right, res)


def pre_order_un_recur(head: Node, res: List):
    if head is not None:
        stack = deque()
        stack.append(head)
        while stack:
            cur = stack.pop()
            res.append(cur.value)
            if cur.right is not None:
                stack.append(cur.right)
            if cur.left is not None:
                stack.append(cur.left)


def in_order_un_recur(head: None, res: List):  # TODO: P96
    if head is not None:
        stack = deque()
        while stack or head is not None:
            if head is not None:
                stack.append(head)
                head = head.left
            else:
                head = stack.pop()
                res.append(head.value)
                head = head.right


def post_order_un_recur_with2stack(head: Node, res: List):  # TODO P98
    if head is not None:
        stack_a = deque()
        stack_b = deque()
        stack_a.append(head)
        while stack_a:
            cur = stack_a.pop()
            stack_b.append(cur)
            if cur.left is not None:
                stack_a.append(cur.left)
            if cur.right is not None:
                stack_a.append(cur.right)
        while stack_b:
            res.append(stack_b.pop().value)


def post_order_un_recur_with1stack_1(head: None, res: List):  # TODO P99
    if head is not None:
        stack = deque()
        before = head
        stack.append(before)  # MISS
        while stack:
            cur = stack[-1]
            if cur.left is not None and cur.left != before and cur.right != before:
                stack.append(cur.left)
            elif cur.right is not None and cur.right != before:
                stack.append(cur.right)
            else:
                res.append(stack.pop().value)
                before = cur  # MISS


def post_order_un_recur_with1stack_2(head: None, res: List):
    if head is not None:
        stack = deque()
        cur = head
        while stack or cur == head:
            while cur is not None:
                stack.append(cur)
                cur = cur.left

            before = None

            while stack:
                cur = stack[-1]
                if cur.right == before:
                    res.append(stack.pop().value)
                    before = cur
                else:
                    cur = cur.right
                    break
            else:
                break


if __name__ == "__main__":
    tree = build_tree_from_txt()
    # tree = build_tree_from_stdin()

    pre_order_res = pre_order(tree.head)
    in_order_res = in_order(tree.head)
    post_order_res = post_order(tree.head)
    print_list(pre_order_res)
    print_list(in_order_res)
    print_list(post_order_res)
