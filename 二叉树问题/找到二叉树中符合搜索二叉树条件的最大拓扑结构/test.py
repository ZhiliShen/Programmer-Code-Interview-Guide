# -*- coding: utf-8 -*- # 
# @Time    : 2021-05-28 20:52
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
from typing import List
from 二叉树问题.utils.utils import Node, build_tree_from_txt, build_tree_from_stdin, print_list


class Record:
    def __init__(self, left, right):
        self.left = left
        self.right = right


def bst_topo_size_1(head: Node):
    if head is None:
        return 0
    max_cur = max_topo(head, head)
    max_cur = max(max_cur, bst_topo_size_1(head.left))
    max_cur = max(max_cur, bst_topo_size_1(head.right))
    return max_cur


def max_topo(head: Node, cur: Node):
    if head is not None and cur is not None and is_bst_node(head, cur):
        return max_topo(head, cur.left) + max_topo(head, cur.right) + 1
    return 0


def is_bst_node(head: Node, cur: Node):
    if head is None:
        return False
    if head == cur:
        return True
    return is_bst_node(head.left if cur.value < head.value else head.right, cur)


def bst_topo_size_2(head: Node):
    dic = {}
    return pos_order(head, dic)


def pos_order(head: Node, dic: dict):
    if head is None:
        return 0
    l = pos_order(head.left, dic)
    r = pos_order(head.right, dic)
    modify_map(head.left, head.value, dic, True)
    modify_map(head.right, head.value, dic, False)
    l_cur = dic.get(head.left, None)
    r_cur = dic.get(head.right, None)
    l_bst = 0 if l_cur is None else l_cur.left + l_cur.right + 1
    r_bst = 0 if r_cur is None else r_cur.left + r_cur.right + 1
    dic[head] = Record(l_bst, r_bst)
    return max(l_bst+r_bst+1, l, r)


def modify_map(cur: Node, head_value: int, dic: dict, flag: bool):
    if cur is None or dic.get(cur, None) is None:
        return 0
    cur_rec = dic[cur]
    if (flag and cur.value > head_value) or (not flag and cur.value < head_value):
        dic.pop(cur)
        return cur_rec.left + cur_rec.right + 1
    else:
        minus = modify_map(cur.right if flag else cur.left, head_value, dic, flag)
        if flag:
            cur_rec.right -= minus
        else:
            cur_rec.left -= minus
        dic[cur] = cur_rec
        return minus


if __name__ == "__main__":
    tree = build_tree_from_txt()
    # tree = build_tree_from_stdin()

    print(bst_topo_size_2(tree.head))
