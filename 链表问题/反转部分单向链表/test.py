# -*- coding: utf-8 -*- # 
# @Time    : 2021-11-19 17:02
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


def print_list(head):
    res = []
    cur = head
    while cur is not None:
        res.append(cur.value)
        cur = cur.next
    print(*res)


def reverse_part(head: Node, start: int, end: int):
    start_prev, end_next = None, None
    cur_len, cur_node = 0, head
    while cur_node is not None:
        cur_len += 1
        if cur_len == start - 1:  # 找到需要逆转的起始节点的前一个节点
            start_prev = cur_node
        if cur_len == end + 1:  # 找到需要逆转的末尾节点的后一个节点
            end_next = cur_node
        cur_node = cur_node.next  # 始终记得在while循环中移动标志量

    # 起止范围需要合法
    if start < 1 or start > end or end > cur_len:  # 这里没必要写start<1 or start>cur_len or end<1 or end>cur_len or start>end
        return head

    # 以1-2-3-4-5-6 需要逆转3-4-5为例子 需要最后得到1-2-5-4-3-6 | 需要逆转1-2-3为例 需要最后得到3-2-1-4-5-6
    # 如果start是1 则此时start_prev为空 所以我们需要额外考虑
    if start_prev is None:
        a_node = head  # 此时a_node为1
    else:
        a_node = start_prev.next  # 此时start_prev为2 a_node为3
    b_node = a_node.next  # b_node为4 | b_node为2
    a_node.next = end_next  # 3-6 | 1-4
    while b_node != end_next:  # 开始逆转4-5 最后得到5-4-3-6 | 开始逆转2-3 最后得到3-2-1-4-5-6
        next = b_node.next
        b_node.next = a_node
        a_node = b_node
        b_node = next

    if start_prev is None:
        return a_node  # 如果start是1 则此时start_prev为空 而目前得到链表就是想要的 头节点应当是a_node
    # 此时2仍然指向3 需要改指向5 此时因为b_node跳出循环 所以b_node为6 而a_node恰好为5
    start_prev.next = a_node

    return head


def reverse_part_1(head: Node, start: int, end: int):
    fake_head = Node(-1)  # 人为添加头节点使得后续的start_prev不会为空 从而避免更多的条件判断
    fake_head.next = head
    start_prev, end_next = None, None
    cur_len, cur_node = 0, fake_head
    while cur_node is not None:
        cur_len += 1
        if cur_len == start:
            start_prev = cur_node
        if cur_len == end+2:
            end_next = cur_node
        cur_node = cur_node.next

    # 起止范围需要合法
    if start < 1 or start > end or end > cur_len-1:  # 这里没必要写start<1 or start>cur_len or end<1 or end>cur_len or start>end
        return head
    a_node = start_prev.next
    b_node = a_node.next
    a_node.next = end_next
    while b_node != end_next:
        next = b_node.next
        b_node.next = a_node
        a_node = b_node
        b_node = next

    start_prev.next = a_node
    return fake_head.next


if __name__ == "__main__":
    test = get_list()
    a, b = map(int, input().split())
    print_list(reverse_part_1(test, a, b))
