# -*- coding: utf-8 -*- # 
# @Time    : 2021-11-18 19:43
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :


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


# 要想象在这个列表后面又复制了一遍这个列表 这样第一次遍历时候k为0的位置与第一个列表结束的位置的距离是n-k 所以第二次遍历的时候k恢复为0 则说明又走了n-k 所以k此时的位置与第二个列表结束的位置正好为k
def remove_last_k_node(head: Node, k: int):
    if head is None or k < 1:
        return head
    cur_node = head
    while cur_node is not None:
        k -= 1
        cur_node = cur_node.next

    if k == 0:
        return head.next
    elif k > 0:
        return head
    else:
        cur_node = head
        while k + 1 < 0:  # 注意这里写的是k+1
            cur_node = cur_node.next
            k += 1
        cur_node.next = cur_node.next.next

    return head


class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.last = None
        self.next = None


def remove_last_k_double_node(head: DoubleNode, k: int):
    if head is None or k < 1:
        return head
    cur_node = head
    while cur_node is not None:
        k -= 1
        cur_node = cur_node.next

    if k == 0:
        head = head.next
        head.last = None
    elif k > 0:
        return head
    else:
        cur_node = head
        while k + 1 < 0:
            cur_node = cur_node.next
            k += 1
        next = cur_node.next.next
        cur_node.next = next
        if next is not None:
            next.last = cur_node

    return head


if __name__ == "__main__":
    a, b = map(int, input().split())
    test1 = get_list()
    print_list(remove_last_k_node(test1, b))
