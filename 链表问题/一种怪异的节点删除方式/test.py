# -*- coding: utf-8 -*- # 
# @Time    : 2021-11-23 13:17
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
    target_node = int(input())  # 这里的target_node是指了链表中的第几个节点需要删除
    node_head = Node(list_content[0])
    cur_node = node_head
    if target_node == 1:
        target_node = cur_node
    for idx, num in enumerate(list_content[1:]):
        cur_node.next = Node(num)
        cur_node = cur_node.next
        if idx+2 == target_node:
            target_node = cur_node
    return node_head, target_node


def print_list(head: Node):
    res = []
    cur = head
    while cur is not None:
        res.append(cur.value)
        cur = cur.next
    print(*res)


def remove_node_wired(node: Node):
    if node is None:
        return
    next = node.next
    if next is None:
        raise Exception("can not remove last node.")
    node.value = next.value  # 将下一个节点的值赋值给当前节点
    node.next = next.next  # 将下一个节点删除


if __name__ == "__main__":
    test, a = get_list()
    remove_node_wired(a)
    print_list(test)
