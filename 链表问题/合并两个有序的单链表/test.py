# -*- coding: utf-8 -*- # 
# @Time    : 2021-11-23 18:40
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None


def get_list():
    len_list = int(input())
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


def merge(a_head: Node, b_head: Node):
    if a_head is None:
        return b_head
    if b_head is None:
        return a_head
    if a_head.value < b_head.value:  # 设置主链表
        head = a_head
        another_head = b_head
    else:
        head = b_head
        another_head = a_head
    tail = head  # 把tail当作head链表中已经排序好的部分的末尾节点更容易理解
    a_cur_node = head.next  # 因为head是已经确定过大小的 所以直接移动到下一个节点进行判断
    b_cur_node = another_head  # 另一个链表的头节点则是不确定的
    while a_cur_node is not None and b_cur_node is not None:
        if a_cur_node.value < b_cur_node.value:  # 如果主链表上的节点是更小的 则重新设置tail 主链表往右移动
            tail = a_cur_node
            a_cur_node = a_cur_node.next
        else:  # 如果副链表上的节点是更小的 将b_cur_node合并进主链表则需要如下步骤 将tail的next指针指向当前b_cur_node 并使得b_cur_node的next指针指向a_cur_ndoe 随后副链表往右移动 并重新设置tail
            next = b_cur_node.next
            tail.next = b_cur_node
            tail = b_cur_node
            b_cur_node.next = a_cur_node
            b_cur_node = next
    if b_cur_node is None:
        return head
    else:
        tail.next = b_cur_node
        return head


def merge_1(a_head: Node, b_head: Node):
    pre_head = Node(-1)  # 人为添加头节点使得不存在主副链表之分

    prev = pre_head
    while a_head is not None and b_head is not None:
        if a_head.value < b_head.value:
            prev.next = a_head
            a_head = a_head.next
        else:
            prev.next = b_head
            b_head = b_head.next

        prev = prev.next  # 不要在判断分支语句中写prev = a_head|b_head 这样写更为简洁

    if a_head is None:
        prev.next = b_head
    else:
        prev.next = a_head

    return pre_head.next


if __name__ == "__main__":
    test1 = get_list()
    test2 = get_list()
    print_list(merge_1(test1, test2))
