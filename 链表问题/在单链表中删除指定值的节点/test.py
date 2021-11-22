# -*- coding: utf-8 -*- # 
# @Time    : 2021-11-22 12:52
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
    len_list = map(int, input().split())
    list_content = list(map(int, input().split()))
    node_head = Node(list_content[0])
    cur_node = node_head
    for num in list_content[1:]:
        cur_node.next = Node(num)
        cur_node = cur_node.next
    return node_head


def print_list(head):
    res = []
    cur = head
    while cur is not None:
        res.append(cur.value)
        cur = cur.next
    print(*res)


def remove_value(head: Node, value: int):
    if head is None:
        return None
    stack = deque()
    cur_node = head
    while cur_node is not None:  # 往栈中放节点的过程是不涉及节点的next指针的改变 所以不需要保留next指针
        if cur_node.value != value:
            stack.append(cur_node)
        cur_node = cur_node.next

    while len(stack) != 0:  # 当前cur_node为None 正好可以作为尾节点的next指针
        stack[-1].next = cur_node
        cur_node = stack.pop()

    return cur_node


def remove_value_1(head: Node, value: int):
    fake_head = Node(-1)  # 人为添加头节点使得找到pre节点更为容易
    fake_head.next = head
    pre = fake_head
    while head is not None:
        next = head.next
        if head.value == value:
            pre.next = next
        else:
            pre = head
        head = next
    return fake_head.next


if __name__ == "__main__":
    test = get_list()
    a = int(input())
    print_list(remove_value_1(test, a))
