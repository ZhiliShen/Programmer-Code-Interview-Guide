# -*- coding: utf-8 -*- # 
# @Time    : 2021-11-19 16:25
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :


class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None


def get_list():
    len_list = map(int, input().split())
    list_content = list(map(int, input().split()))
    node_head = Node(list_content[0])
    cur_node = node_head
    for num in list_content[1:]:
        cur_node.next = Node(num)
        cur_node = cur_node.next
    return node_head


class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.last = None
        self.next = None


def get_double_list():
    len_list = map(int, input().split())
    list_content = list(map(int, input().split()))
    node_head = DoubleNode(list_content[0])
    cur_node = node_head
    prev_node = None
    for num in list_content[1:]:
        cur_node.next = DoubleNode(num)
        cur_node.last = prev_node
        prev_node = cur_node
        cur_node = cur_node.next
    return node_head


def print_list(head):
    res = []
    cur = head
    while cur is not None:
        res.append(cur.value)
        cur = cur.next
    print(*res)


def reverse_list(head: Node):
    prev = None
    while head is not None:
        next = head.next
        head.next = prev
        prev = head
        head = next

    return prev


def reverse_double_list(head: DoubleNode):
    prev = None
    while head is not None:
        next = head.next
        head.next = prev
        head.last = next
        prev = head
        head = next

    return prev


if __name__ == "__main__":
    test1 = get_list()
    test2 = get_double_list()
    print_list(reverse_list(test1))
    print_list(reverse_double_list(test2))
