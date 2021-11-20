# -*- coding: utf-8 -*- # 
# @Time    : 2021-11-20 14:11
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


def is_palindrome_1(head: Node):
    stack = deque()
    cur_node = head
    while cur_node is not None:
        stack.append(cur_node)
        cur_node = cur_node.next

    while len(stack) != 0:
        top_node = stack.pop()
        if top_node.value != head.value:  # 两者指向的并非是同一个对象
            print('false')
            return
        head = head.next

    print('true')


#  这种解法的空间只需要压入链表中的一半区域即可 1-2-3-2-1则1-2是右边的一半 2-1是左边的一半 1-2-3-3-2-1则1-2-3是左边的一半 3-2-1是右边的一半
def is_palindrome_2(head: Node):
    stack = deque()
    cur_node = head
    right_part_start = head.next  # 一定要初始化为第二个节点 1-2-3-2-1 cur_node一共会跳2次 则right_part_start会跳到2 满足要求 | 1-2-3-3-2-1 cur_node一共会跳2次 则right_part_start会跳到第2个3 满足要求
    while cur_node.next is not None and cur_node.next.next is not None:
        right_part_start = right_part_start.next
        cur_node = cur_node.next.next

    while right_part_start is not None:
        stack.append(right_part_start)
        right_part_start = right_part_start.next

    while len(stack) != 0:
        top_node = stack.pop()
        if top_node.value != head.value:
            print('false')
            return
        head = head.next

    print('true')


def is_palindrome_3(head: Node):
    if head is None:
        print('true')
        return
    # 1-2-3-3-2-1 -> 1-2-3-None   1-2-3-2-1 -> 1-2-3-None
    #                   |                         |
    #               1-2-3                       1-2
    # 上面就是我们希望得到最终的链表结构 之后两个端点同时往中间走 开始判断

    # 和is_palindrome_3解法的区别在于 这次需要找的是right_start_part的前一个节点 因为其也需要修改链表结构
    cur_node, right_start_part_prev = head, head
    while cur_node.next is not None and cur_node.next.next is not None:
        right_start_part_prev = right_start_part_prev.next
        cur_node = cur_node.next.next

    # 找到后 再找到right_start_part
    right_start_part = right_start_part_prev.next
    # 此时先让3的下一个节点指向3
    right_start_part_prev.next = None

    # 开始逆转2-1
    while right_start_part is not None:
        next = right_start_part.next
        right_start_part.next = right_start_part_prev
        right_start_part_prev = right_start_part
        right_start_part = next

    # 保留右半区的开始端点与头节点 因为后续恢复为原始链表结构的时候需要这两个节点
    right_start_part = right_start_part_prev
    left_start_part = head

    flag = True

    # 开始从两端往中间走
    while left_start_part is not None:
        if left_start_part.value != right_start_part_prev.value:
            flag = False
            break
        left_start_part = left_start_part.next
        right_start_part_prev = right_start_part_prev.next

    # 把1的下一个节点指向None
    right_start_part_next = right_start_part.next
    right_start_part.next = None
    # 开始恢复为原始链表结构
    while right_start_part_next is not None:
        next = right_start_part_next.next
        right_start_part_next.next = right_start_part
        right_start_part = right_start_part_next
        right_start_part_next = next

    if flag:
        print('true')
    else:
        print('false')


if __name__ == "__main__":
    test = get_list()
    is_palindrome_3(test)
