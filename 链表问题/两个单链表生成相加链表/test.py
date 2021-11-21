# -*- coding: utf-8 -*- #
# @Time    : 2021-11-21 19:59
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
from collections import deque


class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None


def get_list():
    list_content = list(map(int, input().split()))
    node_head = Node(list_content[0])
    cur_node = node_head
    for num in list_content[1:]:
        cur_node.next = Node(num)
        cur_node = cur_node.next
    return node_head


def print_list(head: Node):
    res = []
    cur = head
    while cur is not None:
        res.append(cur.value)
        cur = cur.next
    print(*res)


def add_list(a_head: Node, b_head: Node):
    a_stack, b_stack = deque(), deque()
    a_cur, b_cur = a_head, b_head
    while a_cur is not None:
        a_stack.append(a_cur)
        a_cur = a_cur.next
    while b_cur is not None:
        b_stack.append(b_cur)
        b_cur = b_cur.next

    node, pre = None, None
    count = 0
    while len(a_stack) != 0 or len(b_stack) != 0:
        a_num = a_stack.pop().value if len(a_stack) != 0 else 0
        b_num = b_stack.pop().value if len(b_stack) != 0 else 0
        pre = node
        node = Node((a_num + b_num + count) % 10)
        node.next = pre
        count = (a_num + b_num + count) // 10  # 这里不要忘记让count参与计算

    if count == 1:
        pre = node
        node = Node(1)
        node.next = pre

    return node


def add_list_1(a_head: Node, b_head: Node):
    a_reverse_head = reverse_list(a_head)
    b_reverse_head = reverse_list(b_head)
    a_start, b_start = a_reverse_head, b_reverse_head

    node, pre = None, None
    count = 0
    while a_start is not None or b_start is not None:
        a_num = a_start.value if a_start is not None else 0
        b_num = b_start.value if b_start is not None else 0
        pre = node
        node = Node((a_num + b_num + count) % 10)
        node.next = pre
        count = (a_num + b_num + count) // 10
        a_start = a_start.next if a_start is not None else None  # 注意为None时候的情况
        b_start = b_start.next if b_start is not None else None
    if count == 1:
        pre = node
        node = Node(1)
        node.next = pre

    reverse_list(a_reverse_head)
    reverse_list(b_reverse_head)

    return node


def reverse_list(head: Node):
    cur_node, pre = head, None
    while cur_node is not None:
        next = cur_node.next
        cur_node.next = pre
        pre = cur_node
        cur_node = next
    return pre


if __name__ == "__main__":
    a, b = map(int, input().split())
    test1 = get_list()
    test2 = get_list()
    print_list(add_list_1(test1, test2))
