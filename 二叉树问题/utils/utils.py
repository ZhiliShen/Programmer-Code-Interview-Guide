# -*- coding: utf-8 -*- # 
# @Time    : 2021-05-21 22:39
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : utils.py
# @Notice  :
import sys
from typing import List


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, head):
        self.head = head


def build_tree_from_stdin():
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
    return tree


def print_list(res: List):
    print(" ".join([str(k) for k in res]))


def build_tree_from_txt():
    tree_dict = {}
    counter = 0
    with open("../utils/examples.txt", "r") as f:
        for idx, line in enumerate(f.readlines()):
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
    return tree


def build_2_tree_from_txt():
    tree_dict_1 = {}
    tree_dict_2 = {}
    counter = 0
    with open("../utils/examples.txt", "r") as f:
        for idx, line in enumerate(f.readlines()):
            if idx == 0:
                temp_1 = [int(k) for k in line.split()]
                num_1, head_value_1 = temp_1
                head_node_1 = Node(head_value_1)
                tree_1 = Tree(head_node_1)
                tree_dict_1[head_value_1] = head_node_1
            elif 0 < idx <= num_1:
                temp = [int(k) for k in line.split()]
                value, left_child, right_child = temp
                node = tree_dict_1[value]
                left_node = Node(left_child) if left_child != 0 else None
                right_node = Node(right_child) if right_child != 0 else None
                tree_dict_1[left_child] = left_node
                tree_dict_1[right_child] = right_node
                node.left = left_node
                node.right = right_node
            elif idx == num_1+1:
                temp_2 = [int(k) for k in line.split()]
                num_2, head_value_2 = temp_2
                head_node_2 = Node(head_value_2)
                tree_2 = Tree(head_node_2)
                tree_dict_2[head_value_2] = head_node_2
            else:
                temp = [int(k) for k in line.split()]
                value, left_child, right_child = temp
                node = tree_dict_2[value]
                left_node = Node(left_child) if left_child != 0 else None
                right_node = Node(right_child) if right_child != 0 else None
                tree_dict_2[left_child] = left_node
                tree_dict_2[right_child] = right_node
                node.left = left_node
                node.right = right_node
                counter += 1
                if num_2 == counter:
                    break
    return tree_1, tree_2


def build_2_tree_from_stdin():
    tree_dict_1 = {}
    tree_dict_2 = {}
    counter = 0
    for idx, line in enumerate(sys.stdin):
        if idx == 0:
            temp_1 = [int(k) for k in line.split()]
            num_1, head_value_1 = temp_1
            head_node_1 = Node(head_value_1)
            tree_1 = Tree(head_node_1)
            tree_dict_1[head_value_1] = head_node_1
        elif 0 < idx <= num_1:
            temp = [int(k) for k in line.split()]
            value, left_child, right_child = temp
            node = tree_dict_1[value]
            left_node = Node(left_child) if left_child != 0 else None
            right_node = Node(right_child) if right_child != 0 else None
            tree_dict_1[left_child] = left_node
            tree_dict_1[right_child] = right_node
            node.left = left_node
            node.right = right_node
        elif idx == num_1 + 1:
            temp_2 = [int(k) for k in line.split()]
            num_2, head_value_2 = temp_2
            head_node_2 = Node(head_value_2)
            tree_2 = Tree(head_node_2)
            tree_dict_2[head_value_2] = head_node_2
        else:
            temp = [int(k) for k in line.split()]
            value, left_child, right_child = temp
            node = tree_dict_2[value]
            left_node = Node(left_child) if left_child != 0 else None
            right_node = Node(right_child) if right_child != 0 else None
            tree_dict_2[left_child] = left_node
            tree_dict_2[right_child] = right_node
            node.left = left_node
            node.right = right_node
            counter += 1
            if num_2 == counter:
                break
    return tree_1, tree_2


def build_value_tree_from_txt():
    tree_dict = {}
    counter = 0
    with open("../utils/examples.txt", "r") as f:
        for idx, line in enumerate(f.readlines()):
            if idx == 0:
                temp = [int(k) for k in line.split()]
                num, head_index = temp
                head_node = Node(head_index)
                tree = Tree(head_node)
                tree_dict[head_index] = head_node
            else:
                temp = [int(k) for k in line.split()]
                index, left_child, right_child, value = temp
                node = tree_dict[index]
                node.value = value
                left_node = Node(left_child) if left_child != 0 else None
                right_node = Node(right_child) if right_child != 0 else None
                tree_dict[left_child] = left_node
                tree_dict[right_child] = right_node
                node.left = left_node
                node.right = right_node
                counter += 1
                if num == counter:
                    break
    return tree


def build_value_tree_from_stdin():
    tree_dict = {}
    counter = 0
    for idx, line in enumerate(sys.stdin):
        if idx == 0:
            temp = [int(k) for k in line.split()]
            num, head_index = temp
            head_node = Node(head_index)
            tree = Tree(head_node)
            tree_dict[head_index] = head_node
        else:
            temp = [int(k) for k in line.split()]
            index, left_child, right_child, value = temp
            node = tree_dict[index]
            node.value = value
            left_node = Node(left_child) if left_child != 0 else None
            right_node = Node(right_child) if right_child != 0 else None
            tree_dict[left_child] = left_node
            tree_dict[right_child] = right_node
            node.left = left_node
            node.right = right_node
            counter += 1
            if num == counter:
                break
    return tree

