# -*- coding: utf-8 -*- # 
# @Time    : 2021-11-18 20:36
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
from math import ceil

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


def remove_k_node(head: Node, k: int):
    if head is None or k < 0:
        return head
    fake_head = Node(-1)  # 假如k是1 要删除第一个节点 人为添加头节点使得删除第一个节点变得简单
    fake_head.next = head
    cur_node = fake_head
    while k > 1:
        cur_node = cur_node.next
        k -= 1
    cur_node.next = cur_node.next.next

    return fake_head.next


def remove_mid_node(head: Node):
    if head is None or head.next is None:  # 如果链表为空或长度为1则不用删除任何节点
        return head

    if head.next.next is None:  # 如果链表的长度为2则删除最后一个节点
        return head.next

    slow_head, quick_head = head, head.next.next  # 快指针的移动速度是慢指针的移动的两倍 所以快指针到头的时候 慢指针就指向中间指针的前一个位置

    while quick_head.next is not None and quick_head.next.next is not None:
        slow_head = slow_head.next
        quick_head = quick_head.next.next

    slow_head.next = slow_head.next.next
    return head


def remove_by_ratio_node(head: Node, a: int, b: int):
    if a < 1 or a > b:
        return head
    len_list = 0
    cur = head
    while cur is not None:
        len_list += 1
        cur = cur.next
    k = int(ceil(a*len_list/b))  # 注意这里是向上取整
    if k == 1:
        head = head.next
    if k > 1:
        cur = head
        while k-1 > 1:
            cur = cur.next
            k -= 1
        cur.next = cur.next.next

    return head


if __name__ == "__main__":
    a, b = map(int, input().split())
    test1 = get_list()
    print_list(remove_k_node(test1, b))
