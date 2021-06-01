# -*- coding: utf-8 -*- # 
# @Time    : 2021-05-31 21:45
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
from typing import List
from 二叉树问题.utils.utils import Node, build_tree_from_txt, build_tree_from_stdin, print_list
from collections import deque


def print_by_level(head: Node):
    if head is None:
        return ""
    level = 1
    last = head
    next_last = None
    queue = deque()
    queue.append(head)
    res = []
    while len(queue) != 0:
        cur = queue.popleft()
        res.append(cur)
        if cur.left is not None:
            queue.append(cur.left)
            next_last = cur.left
        if cur.right is not None:
            queue.append(cur.right)
            next_last = cur.right
        if cur == last:
            print("Level {:d} : {:s}".format(level, " ".join([str(temp.value) for temp in res])))
            level += 1
            last = next_last
            next_last = None
            res = []


def print_by_zigzag(head: Node):
    if head is None:
        return ""
    level = 1
    last = head
    next_last = None
    queue = deque()
    queue.appendleft(head)
    flag = True
    res = []
    while len(queue) != 0:
        if flag:
            cur = queue.popleft()
            res.append(cur)
            if cur.left is not None:
                queue.append(cur.left)
                next_last = cur.left if next_last is None else next_last
            if cur.right is not None:
                queue.append(cur.right)
                next_last = cur.right if next_last is None else next_last
        else:
            cur = queue.pop()
            res.append(cur)
            if cur.right is not None:
                queue.appendleft(cur.right)
                next_last = cur.right if next_last is None else next_last
            if cur.left is not None:
                queue.appendleft(cur.left)
                next_last = cur.left if next_last is None else next_last
        if cur == last:
            if flag:
                print("Level {:d} from left to right: {:s}".format(level, " ".join([str(temp.value) for temp in res])))
            else:
                print("Level {:d} from right to left: {:s}".format(level, " ".join([str(temp.value) for temp in res])))
            level += 1
            flag = not flag
            last = next_last
            next_last = None
            res = []


if __name__ == "__main__":
    tree = build_tree_from_txt()
    # tree = build_tree_from_stdin()

    print_by_level(tree.head)
    print_by_zigzag(tree.head)
