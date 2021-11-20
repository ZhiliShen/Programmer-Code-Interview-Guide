# -*- coding: utf-8 -*- # 
# @Time    : 2021-11-20 16:05
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


def list_partition(head: Node, pivot: int):
    if head is None:
        return head
    array = []
    cur_node = head
    while cur_node is not None:
        array.append(cur_node.value)
        cur_node = cur_node.next

    array_partition(array, pivot)

    node_head = Node(array[0])
    cur_node = node_head
    for num in array[1:]:
        cur_node.next = Node(num)
        cur_node = cur_node.next

    return node_head


def array_partition(array: list, pivot: int):
    left, mid, right = -1, 0, len(
        array)  # [0, left]<pivot (left, mid)==pivot [mid, right) not sure [right, len(array)-1]>pivot
    while mid < right:
        if array[mid] == pivot:
            mid += 1
        elif array[mid] < pivot:
            left += 1
            array[left], array[mid] = array[mid], array[left]
            mid += 1
        else:
            right -= 1
            array[right], array[mid] = array[mid], array[right]

# 该种解法的空间复杂度为常量级别
def list_partition_1(head: Node, pivot: int):
    small_start, median_start, larger_start = None, None, None
    small_end, median_end, larger_end = None, None, None
    while head is not None:
        next = head.next
        head.next = None  # 这一步确保每一个节点都是干净的 为后面的节点合并提供方便
        if head.value < pivot:
            if small_start is None:
                small_start = head
                small_end = head
            else:
                small_end.next = head  # 先和以前的节点进行连接 再进行更新
                small_end = head
        elif head.value == pivot:
            if median_start is None:
                median_start = head
                median_end = head
            else:
                median_end.next = head
                median_end = head
        else:
            if larger_start is None:
                larger_start = head
                larger_end = head
            else:
                larger_end.next = head
                larger_end = head
        head = next

    if small_end is not None:
        small_end.next = median_start
        if median_end is None:
            median_end = small_end
        else:
            median_end = median_end

    if median_end is not None:
        median_end.next = larger_start

    if small_start is not None:
        return small_start
    else:
        if median_start is not None:
            return median_start
        else:
            return larger_start


if __name__ == "__main__":
    a, b = list(map(int, input().split()))
    test = get_list()
    print_list(list_partition_1(test, b))
