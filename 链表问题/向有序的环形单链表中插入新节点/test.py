# -*- coding: utf-8 -*- # 
# @Time    : 2021-11-23 16:20
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None


def get_list():
    len_list = int(input())
    list_content = list(map(int, input().split()))
    node_head = Node(list_content[0])
    cur_node = node_head
    for idx, num in enumerate(list_content[1:]):
        cur_node.next = Node(num)
        cur_node = cur_node.next
    cur_node.next = node_head
    return node_head, len_list


def print_list(head: Node, len_list: int):
    res = []
    cur = head
    for _ in range(len_list + 1):
        res.append(cur.value)
        cur = cur.next
    print(*res)


def insert_num(head: Node, num: int):
    node = Node(num)
    if head is None:
        return node
    pre = head
    cur_node = head.next
    while cur_node != head:  # 此时循环的中止条件是cur_node不等于head
        if pre.value <= num <= cur_node.value:
            break
        pre = cur_node
        cur_node = cur_node.next
    pre.next = node
    node.next = cur_node
    if num < head.value:
        return node
    else:
        return head


if __name__ == "__main__":
    test, a = get_list()
    b = int(input())
    print_list(insert_num(test, b), a)
