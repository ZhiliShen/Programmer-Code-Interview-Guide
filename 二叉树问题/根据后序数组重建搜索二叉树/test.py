# -*- coding: utf-8 -*- #
# @Time    : 2021/7/21 20:24
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
import sys
from typing import List
from 二叉树问题.如何较为直观地打印二叉树.test import print_tree
from 二叉树问题.utils.utils import Node, build_2_tree_from_txt, build_tree_from_stdin, print_list


def is_BST(serial_post: List):
    if len(serial_post) == 1 or len(serial_post) == 0:
        return True
    root = serial_post[-1]
    flag = True
    is_bst = True
    for i in range(len(serial_post) - 1):
        if flag and serial_post[i] > root:
            flag = False
            left_serial_post = serial_post[:i]
            right_serial_post = serial_post[i:-1]
            continue
        if (not flag) and serial_post[i] < root:
            is_bst = False
    if flag:
        left_serial_post = serial_post[:-1]
        right_serial_post = []
    return is_bst and is_BST(left_serial_post) and is_BST(right_serial_post)


def is_post_array(arr: List):
    if arr is None or len(arr) == 0:
        return False
    return is_post(arr, 0, len(arr) - 1)


def is_post(arr: List, start: int, end: int):
    if start == end:
        return True
    less, more = -1, end
    for index in range(start, end):
        if arr[end] > arr[index]:
            less = index
        else:
            more = index if more == end else more
    if less == -1 or more == end:
        return is_post(arr, start, end - 1)
    else:
        return True if less < more else False and is_post(arr, start, less) and is_post(arr, more, end - 1)


def post_array_to_bst(post_arr: List):
    if post_arr is None or len(post_arr) == 0:
        return None
    return post_to_array(post_arr, 0, len(post_arr)-1)


def post_to_array(pos_arr: List, start: int, end: int):
    if start > end:
        return None
    less, more = -1, end
    head = Node(pos_arr[end])
    for index in range(start, end):
        if pos_arr[end] > pos_arr[index]:
            less = index
        else:
            more = index if more == end else more
    head.left = post_to_array(pos_arr, start, less)
    head.right = post_to_array(pos_arr, more, end-1)
    return head


if __name__ == "__main__":
    num = int(sys.stdin.readline())
    serial_post = [int(k) for k in sys.stdin.readline().split(" ")]
    if is_post_array(serial_post):
        print("true")
    else:
        print("false")
    print_tree(post_array_to_bst(serial_post))


