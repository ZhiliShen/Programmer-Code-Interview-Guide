# -*- coding: utf-8 -*- #
# @Time    : 2021/7/22 9:46
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
from typing import List
from collections import deque
from 二叉树问题.utils.utils import Node, build_tree_from_txt, build_tree_from_stdin, print_list


def morris(head: Node):
    morris_serial = []
    if head is None:
        return morris_serial
    cur = head
    while cur is not None:
        morris_serial.append(cur.value)
        if cur.left is None:  # cur change to it right child or back to its parent
            cur = cur.right
        else:
            most_right = cur.left
            while most_right.right is not None and most_right.right != cur:  # most_right.right is not cur is vital
                most_right = most_right.right  # find cur.left's most right child
            if most_right.right is None:  # most right child is None -> cur.left has not been visited
                most_right.right = cur
                cur = cur.left
            else:
                most_right.right = None  # most right child is not None -> cur.left has been visited reset
                cur = cur.right
    return morris_serial


def morris_pre(head: Node):
    pre_serial = []
    if head is None:
        return None
    cur = head
    while cur is not None:
        if cur.left is None:
            pre_serial.append(cur.value)
            cur = cur.right
        else:
            most_right = cur.left
            while most_right.right is not None and most_right.right != cur:
                most_right = most_right.right
            if most_right.right is None:
                most_right.right = cur
                pre_serial.append(cur.value)
                cur = cur.left
            else:
                most_right.right = cur
                cur = cur.right
    return pre_serial


def morris_in(head: Node):
    res = True
    if head is None:
        return res
    cur = head
    pre = None
    while cur is not None:
        if cur.left is None:
            if pre is not None and pre.value > cur.value:  # this judgement must before assignment
                res = False
            pre = cur
            cur = cur.right
        else:
            most_right = cur.left
            while most_right.right is not None and most_right.right != cur:
                most_right = most_right.right
            if most_right.right is None:
                most_right.right = cur
                cur = cur.left
            else:
                most_right.right = None
                if pre is not None and pre.value > cur.value:
                    res = False
                pre = cur
                cur = cur.right
    return res


def morris_pos(head: Node):
    pos_serial = []
    if head is None:
        return None
    cur = head
    while cur is not None:
        if cur.left is None:
            cur = cur.right
        else:
            most_right = cur.left
            while most_right.right is not None and most_right.right != cur:
                most_right = most_right.right
            if most_right.right is None:
                most_right.right = cur
                cur = cur.left
            else:
                most_right.right = None
                print_edge(cur.left, pos_serial)
                cur = cur.right
    print_edge(head, pos_serial)
    return pos_serial


def print_edge(node: Node, pos_serial: List):
    tail = reverse_edge(node)
    cur = tail
    while cur is not None:
        pos_serial.append(cur.value)
        cur = cur.right
    reverse_edge(tail)


def reverse_edge(start: Node):
    pre_node = None
    while start is not None:
        next_node = start.right
        start.right = pre_node
        pre_node = start
        start = next_node
    return pre_node


def is_CBT(head: Node):
    if head is None:
        return True
    queue = deque()
    leaf = False
    queue.append(head)
    while len(queue) != 0:
        node = queue.popleft()
        left = node.left
        right = node.right
        if (leaf and (left is not None or right is not None)) or (left is None and right is not None):
            return False
        if left is not None:
            queue.append(left)
        if right is not None:
            queue.append(right)
        else:  # indicate that we have arrived last layer
            leaf = True
    return True


if __name__ == "__main__":
    tree = build_tree_from_txt()
    if morris_in(tree.head):
        print("true")
    else:
        print("false")
    if is_CBT(tree.head):
        print("true")
    else:
        print("false")
