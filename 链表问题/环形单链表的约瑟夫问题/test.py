# -*- coding: utf-8 -*- # 
# @Time    : 2021-11-25 10:31
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None


def get_list(num):
    list_content = [i + 1 for i in range(num)]
    node_head = Node(list_content[0])
    cur_node = node_head
    for num in list_content[1:]:
        cur_node.next = Node(num)
        cur_node = cur_node.next
    cur_node.next = node_head
    return node_head


def josephus_kill(head: Node, m: int):
    if head is None or head.next == head or m < 1:  # 如果链表为空或链表为单链表自形成环 则直接返回
        return head
    last = head  # 因为该链表有环 所以需要找到该环的最后一个节点 方便报数
    while last.next != head:
        last = last.next
    count = 1
    while head != last:
        if count == m:
            last.next = head.next  # head是需要消除的节点 last需要移动
            count = 1  # 消除后重新报数
        else:
            last = last.next  # 当当前head不是需要消除的节点 则last不需要移动
            count += 1
        head = last.next
    print(head.value)


# 首先一个节点的报号数和编号数的关系是 编号数=(报号数-1)%i+1 这里是i是指环的长度 例如 编号1报1 编号2报2 编号3报3 编号1报4 编号2报5
# 其次一个节点没有后 新编号和老编号的关系是 老编号=(新编号+没有的节点的编号数-1)%i+1 例如 原本是旧编号1 2 3 4 5 6 当4没有后是3 4 5 1 2
# 因此可得到老编号=(新编号+(报号数-1)%i+1-1)%i+1 -> 老编号=(新编号+(报号数-1)%i)%i+1 -> 老编号=(新编号+报号数-1)%i+1
def josephus_kill_1(head: Node, m: int):
    if head is None or head.next == head or m < 1:
        return head
    cur_node = head.next
    list_len = 1
    while cur_node != head:
        list_len += 1
        cur_node = cur_node.next
    last_live = get_live_1(list_len, m)
    while last_live != 1:
        head = head.next
        last_live -= 1
    head.next = head
    print(head.value)


def get_live(i: int, m: int):  # 推导式的递归写法
    if i == 1:
        return 1
    return (get_live(i - 1, m) + m - 1) % i + 1


def get_live_1(i: int, m: int):  # 推导式的动态规划写法
    # base case
    result = 1
    # transfer equation
    for index in range(i - 1):
        result = (result + m - 1) % (index + 2) + 1
    return result


if __name__ == "__main__":
    a, b = map(int, input().split())
    test = get_list(a)
    josephus_kill_1(test, b)
