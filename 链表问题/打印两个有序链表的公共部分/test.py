# -*- coding: utf-8 -*- # 
# @Time    : 2021-11-18 19:28
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


def print_common_part(a_head: Node, b_head: Node):
    res = []
    while a_head is not None and b_head is not None:
        if a_head.value == b_head.value:
            res.append(a_head.value)
            a_head = a_head.next
            b_head = b_head.next
        elif a_head.value < b_head.value:
            a_head = a_head.next
        else:
            b_head = b_head.next
    return res


if __name__ == "__main__":
    test1 = get_list()
    test2 = get_list()
    print(*print_common_part(test1, test2))
