# -*- coding: utf-8 -*- #
# @Time    : 2021-05-24 16:27
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
import sys
from 二叉树问题.utils.utils import Node, build_value_tree_from_txt


def get_max_length(head: Node, k: int):
    dic = {0: 0}
    return pre_order(head, k, 0, 1, 0, dic)


def pre_order(head: Node, k: int, pre_sum: int, level: int, max_length: int, sum_map: dict):
    if head is None:
        return max_length
    cur_sum = pre_sum + head.value
    sum_map.setdefault(cur_sum, level)
    j = sum_map.get(cur_sum - k)
    if j is not None:
        max_length = max(level - j, max_length)
    max_length = pre_order(head.left, k, cur_sum, level + 1, max_length, sum_map)
    max_length = pre_order(head.right, k, cur_sum, level + 1, max_length, sum_map)
    if sum_map.get(cur_sum) == level:
        sum_map.pop(cur_sum)
    return max_length


if __name__ == "__main__":
    tree = build_value_tree_from_txt()
    for i in sys.stdin:
        k = int(i)
        break

    print(get_max_length(tree.head, k))
