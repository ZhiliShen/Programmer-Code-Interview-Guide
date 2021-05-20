# -*- coding: utf-8 -*- # 
# @Time    : 2021-05-20 14:41
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py.py
# @Notice  :
import sys
from typing import List
from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class Tree:
    def __init__(self, head):
        self.head = head


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
    tree_dict = {}
    counter = 0
    for idx, line in enumerate(sys.stdin):
        if idx == 0:
            temp = [int(k) for k in line.split()]
            num, head_value = temp
            head_node = Node(head_value)
            tree = Tree(head_node)
            tree_dict[head_value] = head_node
        else:
            temp = [int(k) for k in line.split()]
            value, left_child, right_child = temp
            node = tree_dict[value]
            left_node = Node(left_child) if left_child != 0 else None
            right_node = Node(right_child) if right_child != 0 else None
            tree_dict[left_child] = left_node
            tree_dict[right_child] = right_node
            node.left = left_node
            node.right = right_node
            counter += 1
            if num == counter:
                break
    pre_order_res = pre_order(tree.head)
    in_order_res = in_order(tree.head)
    post_order_res = post_order(tree.head)
    print(" ".join([str(k) for k in pre_order_res]))
    print(" ".join([str(k) for k in in_order_res]))
    print(" ".join([str(k) for k in post_order_res]))
