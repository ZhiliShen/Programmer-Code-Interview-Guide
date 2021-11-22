# -*- coding: utf-8 -*- #
# @Time    : 2021-11-22 10:40
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


def remove_replicates(head: Node):
    if head is None:
        return None
    value_set = set()
    cur_node = head
    pre = head  # 头节点是一定不会被删除的
    value_set.add(cur_node.value)
    cur_node = cur_node.next
    while cur_node is not None:
        if cur_node.value in value_set:
            pre.next = cur_node.next  # 如果已经存在重复 则将上一个未删除节点的next指针指向当前节点的下一个节点
        else:
            value_set.add(cur_node.value)
            pre = cur_node  # 如果不存在重复 则将当前节点设置为上一个未删除的节点
        cur_node = cur_node.next

    return head


def remove_replicates_1(head: Node):
    cur_node = head
    while cur_node is not None:
        pre = cur_node  # 每一次都要更新当前未删除节点
        next = cur_node.next
        while next is not None:
            if cur_node.value == next.value:
                pre.next = next.next
            else:
                pre = next  # 更新当前未删除节点
            next = next.next
        cur_node = cur_node.next
    return head


if __name__ == "__main__":
    test = get_list()
    print_list(remove_replicates_1(test))
