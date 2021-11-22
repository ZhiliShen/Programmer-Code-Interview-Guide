# -*- coding: utf-8 -*- #
# @Time    : 2021-11-21 21:33
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


def reverse_k_node(head: Node, k: int):
    if k < 2:
        return head
    stack = deque()
    new_head, cur_node, pre, next = head, head, None, None  # 这里new_head写head 不要写None 因为如果k小于链表长度 最后会返回None
    # 1-2-3-4-5-6 -> 3-2-1-6-5-4
    while cur_node is not None:
        next = cur_node.next
        stack.append(cur_node)
        if len(stack) == k:
            # 1-2-3 该待逆序区间的前一个节点为None 后一个节点为4 最后逆转后为3-2-1 其中1是下一个逆序区间的前一个节点
            pre = resign(stack, pre, next)  # 这里的pre是逆序区间的前一个节点 next是逆序区间的后一个节点
            if new_head == head:  # 如果当前逆序区间的前一个节点为None 3是当前节点也是逆序后的链表的头节点
                new_head = cur_node
        cur_node = next

    return new_head


def resign(stack: deque, left: Node, right: Node):
    node = stack.pop()
    if left is not None:  # 如果有上一组的话 把上一组的尾节点连接上这一组的头节点
        left.next = node
    while len(stack) != 0:
        next = stack.pop()
        node.next = next
        node = next
    node.next = right  # 逆序后把这一组的尾节点和下一组的头节点连接上
    return node


# 该种解法不需要栈
def reverse_k_node_1(head: Node, k: int):
    if k < 2:
        return head
    cur_node, pre = head, None  # 这里可以不用new_head
    count = 0
    while cur_node is not None:
        next = cur_node.next
        count += 1
        if count == k:
            if pre is None:
                start = head
                head = cur_node  # 1-2-3逆序后3就会成为新的头节点 而cur_node此时就是3
            else:
                start = pre.next
                head = head
            resign_1(pre, start, cur_node, next)
            pre = start  # 上一组的尾节点是1 也是下一组的头节点的上一个节点
            count = 0
        cur_node = next

    return head


def resign_1(left, start, end, right):
    pre = start
    cur_node = start.next
    while cur_node != right:
        next = cur_node.next
        cur_node.next = pre
        pre = cur_node
        cur_node = next
    if left is not None:
        left.next = end  # 如果有上一组的话 把上一组的尾节点连接上这一组的头节点 注意此时的头节点变为end
    start.next = right  # 逆序后把这一组的尾节点和下一组的头节点连接上 注意此时的尾节点变为start


if __name__ == "__main__":
    test = get_list()
    a = int(input())
    print_list(reverse_k_node_1(test, a))
