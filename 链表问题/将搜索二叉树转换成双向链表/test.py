# -*- coding: utf-8 -*- # 
# @Time    : 2021-11-22 13:09
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
import sys
from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_tree_from_stdin():
    tree_dict = {}
    num = int(input())
    head_value, left_child_value, right_child_value = map(int, input().split())
    head = Node(head_value)
    tree_dict[head_value] = head
    head.left = Node(left_child_value) if left_child_value != 0 else None
    head.right = Node(right_child_value) if right_child_value != 0 else None
    tree_dict[left_child_value] = head.left
    tree_dict[right_child_value] = head.right
    for _ in range(num - 1):
        cur_value, left_child_value, right_child_value = map(int, input().split())
        cur_node = tree_dict[cur_value]
        cur_node.left = Node(left_child_value) if left_child_value != 0 else None
        cur_node.right = Node(right_child_value) if right_child_value != 0 else None
        tree_dict[left_child_value] = cur_node.left
        tree_dict[right_child_value] = cur_node.right

    return head


def print_list(head: Node):
    res = []
    cur = head
    while cur is not None:
        res.append(cur.value)
        cur = cur.right
    print(*res)


def convert(head: Node):
    queue = deque()
    in_order2queue(head, queue)
    if len(queue) == 0:
        return head
    head = queue.popleft()
    pre = head
    pre.left = None  # 头节点的last指针设置为None
    while len(queue) != 0:
        cur = queue.popleft()
        pre.right = cur  # 上一个节点的next指针指向当前节点
        cur.left = pre  # 当前节点的last指针指向上一个节点
        pre = cur
    pre.right = None  # 尾节点的next指针指向None
    return head


def in_order2queue(head: Node, queue: deque):
    if head is None:
        return
    in_order2queue(head.left, queue)
    queue.append(head)
    in_order2queue(head.right, queue)


def convert_2(head: Node):
    if head is None:
        return None
    return process(head)[0]


# process(node)会将以node为head的树变为双向链表
def process(node: Node):
    if node is None:
        return None, None
    left_part = process(node.left)
    right_part = process(node.right)
    if left_part[-1] is not None:  # 将左子树转换而来的双向链表尾节点的next指针指向当前节点
        left_part[-1].right = node
    node.left = left_part[-1]  # 将当前节点的last指针指向左子树转换而来的双向链表尾节点
    node.right = right_part[0]  # 将当前节点的next指针指向右子树转换而来的双向链表头节点
    if right_part[0] is not None:  # 将右子树转换而来的双向链表头节点的last指针指向当前节点
        right_part[0].left = node

    return left_part[0] if left_part[0] is not None else node, right_part[-1] if right_part[-1] is not None else node


if __name__ == "__main__":
    test = build_tree_from_stdin()
    print_list(convert_2(test))
