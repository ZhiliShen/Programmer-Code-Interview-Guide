# -*- coding: utf-8 -*- # 
# @Time    : 2021-11-20 20:58
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.random = None


def copy_list_with_rand(head: Node):
    if head is None:
        return None
    node2node = {}
    cur_node = head
    while cur_node is not None:
        node2node[cur_node] = Node(cur_node.val)
        cur_node = cur_node.next

    cur_node = head

    while cur_node is not None:
        node2node[cur_node].next = node2node.get(cur_node.next, None)  # 注意cur_node.next可能为None
        node2node[cur_node].random = node2node.get(cur_node.random, None)  # 注意cur_node.random可能为None
        cur_node = cur_node.next

    return node2node[head]

# 该种解法先把1-2-3转换为1-1-2-2-3-3 这样在复制随机指针的时候 可以直接根据cur_node.random.next找到复制目标
def copy_list_with_rand_2(head: Node):
    if head is None:
        return None
    # 1-2-3 -> 1-1-2-2-3-3
    cur_node = head
    while cur_node is not None:
        next = cur_node.next
        copy_node = Node(cur_node.val)
        cur_node.next = copy_node
        copy_node.next = next
        cur_node = next

    # 复制随机指针
    cur_node = head
    while cur_node is not None:
        next = cur_node.next.next
        copy_node = cur_node.next
        copy_node.random = cur_node.random.next if cur_node.random is not None else None
        # copy_node = next.next  # 不能这样写 因为next有可能为空
        cur_node = next

    # 拆分指针
    cur_node, res_head = head, head.next  # 一定要在此时保留好复制链表的头节点 因为一旦拆分结束 head.next就不再是复制过后的链表
    while cur_node is not None:
        next = cur_node.next.next
        copy_node = cur_node.next
        cur_node.next = next
        copy_node.next = next.next if next is not None else None
        cur_node = next

    return res_head
