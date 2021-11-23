# -*- coding: utf-8 -*- # 
# @Time    : 2021-11-23 21:32
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


def relocate(head: Node):
    if head is None or head.next is None:
        return head
    # 1-2-3 目标为1 1-2-3-4目标为2
    mid = head
    fast = head.next
    while fast.next is not None and fast.next.next is not None:  # 不要写成while fast is not None and fast.next is not None:
        mid = mid.next
        fast = fast.next.next
    right = mid.next
    mid.next = None  # 需要将左半区链表与右半区链表断开 这也是为什么要找左半区最后一个节点的原因
    return merge_lr_1(head, right)


def merge_lr(left: Node, right: Node):
    fake_head = Node(-1)
    cur_node = fake_head
    # 例如需要合并1-2-3 5-6-7
    while left is not None:
        left_next = left.next  # 先存档1.next
        cur_node.next = left  # cur_node-1
        left.next = right  # cur_node-1-5
        cur_node = right  # 当前最后一个节点为right
        left = left_next  # left更新
        right = right.next  # right更新
    return fake_head.next  # 记得返回的是fake_head.next


def merge_lr_1(left: Node, right: Node):
    head = left
    # 例如需要合并1-2-3 5-6-7
    while left.next is not None:  # 这里不能处理末尾节点 因为如果处理1-2-3 4-5-6-7时 会使6指向None
        next = right.next
        right.next = left.next  # 5-2
        left.next = right  # 1-5-2
        left = right.next  # left更新
        right = next  # right更新
    left.next = right
    return head


if __name__ == "__main__":
    test = get_list()
    print_list(relocate(test))
