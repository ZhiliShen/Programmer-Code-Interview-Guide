# -*- coding: utf-8 -*- # 
# @Time    : 2021-11-22 16:53
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


def print_list(head: Node):
    res = []
    cur = head
    while cur is not None:
        res.append(cur.value)
        cur = cur.next
    print(*res)


def selection_sort(head: Node):
    tail = None  # 排序部分的尾部
    cur_node = head  # 未排序部分的头部
    while cur_node is not None:
        small = cur_node  # 未排序部分中最小节点 每一轮都需要初始化为cur_node 假如1-2-3 1已经是最小节点 则small_pre为None 此时small为cur_node 所以需要在每一轮让small指向cur
        small_pre = get_smallest_pre_node(cur_node)  # 未排序部分中最小节点的前一个节点
        if small_pre is not None:  # 如果找到的最小节点不是当前节点 需要记录最小节点 并将最小节点的前一个节点的next指针指向最小节点的下一个节点
            small = small_pre.next
            small_pre.next = small.next
        if cur_node == small:  # 如果找到的最小节点是当前节点 则不需要更新最小节点 也不需要进行指针的变换 未排序部分的头部往右移动
            cur_node = cur_node.next
        else:  # 如果找到的最小节点不是当前节点 则继续检查当前节点
            cur_node = cur_node
        if tail is None:  # 如果是第一次找到最小节点 则排序过后的头节点是当前的最小节点
            head = small
        else:  # 如果不是第一次找到最小节点 则将排序部分的尾部的next指针指向当前的最小节点
            tail.next = small
        tail = small  # 当前排序部分的尾部为当前的最小节点
    return head


def get_smallest_pre_node(head: Node):
    small_pre = None
    small = head
    pre = head
    cur_node = head.next
    while cur_node is not None:
        if cur_node.value < small.value:
            small_pre = pre
            small = cur_node
        pre = cur_node
        cur_node = cur_node.next
    return small_pre  # 如果当前节点非降序 则small_pre为空


if __name__ == "__main__":
    test = get_list()
    print_list(selection_sort(test))
