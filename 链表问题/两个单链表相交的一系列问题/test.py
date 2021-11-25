# -*- coding: utf-8 -*- # 
# @Time    : 2021-11-24 15:50
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


# 如果链表有环则返回入环节点 否则返回None 假设头节点到入环节点距离为a 入环节点到第一次相遇节点距离为b 环的长度为c 则到slow与fast相遇时 slow走过的距离为a+b+n1*c 因为fast的速度是slow的两倍
# 所以fast走过的距离为2(a+b+n1*c) 因为fast与slow在相遇节点相遇 所以fast比slow多走的距离a+b+n1*c一定是环的整数倍n2 即a+b+n1*c=n2*c 即a+b=(n2-n1)*c
# 此时fast从开始节点出发 走过a到达入环节点 此时slow从b也走过a 此时a+b是环的整数倍 因此slow也会到达入环节点 因为fast一定会在slow没有走完一圈环的时候与其相遇 因此其时间复杂度为O(N) 可以用极限的思想
# 假设a为0 即两者都是从入环节点开始移动 fast也是在slow刚刚结束第一圈的时候追上的 而事实上fast比slow更快进入环 因此能更早追上
def get_loop_node(head: Node):
    if head is None or head.next is None or head.next.next is None:  # 当链表为空 长度为1且末尾为None 长度为2且末尾为None 则该链表无环
        return None
    slow = head.next
    fast = head.next.next
    while slow != fast:
        if fast.next is None or fast.next.next is None:  # 如果快指针能够走到头 则说明链表无环
            return None
        slow = slow.next
        fast = fast.next.next

    node = head  # 将fast指针移回开始位置 并放慢移动速度
    while node != slow:
        node = node.next
        slow = slow.next

    return node


# 找出两个无环链表的第一个相交位置
# 先通过判断两个无环链表的最后一个节点是否一致 来判断两者是否相交
# 如果相交 则让较长的链表先走两者长度差值 然后再一起走 则最后会在第一个相交点上相遇
def intersect_no_loop(a_head: Node, b_head: Node):
    if a_head is None or b_head is None:
        return None
    a_cur, b_cur = a_head, b_head
    a_len_minus_b_len = 0  # 这里记录的是差值 而并不是每个链表的长度
    while a_cur.next is not None:  # 这里判断的是next指针是否为空
        a_len_minus_b_len += 1
        a_cur = a_cur.next
    while b_cur.next is not None:
        a_len_minus_b_len -= 1
        b_cur = b_cur.next
    if a_cur != b_cur:
        return None
    else:
        if a_len_minus_b_len > 0:
            node_1 = a_head
            node_2 = b_head
        else:
            node_1 = b_head
            node_2 = a_head
        for _ in range(abs(a_len_minus_b_len)):  # 这里需要取绝对值
            node_1 = node_1.next
        while node_1 != node_2:
            node_1 = node_1.next
            node_2 = node_2.next
        return node_1


# 找出两个有环链表的第一个相交位置
# 不会存在一个无环链表与一个有环链表相交的情况 因为相交意味着共享部分链表 则无环链表会拥有有环链表中环的部分 因此变为有环链表
def intersect_both_loop(a_head: Node, b_head: Node, a_loop: Node, b_loop: Node):
    # 如果入环节点一致 则说明两个链表在入环之前相交 使用找出无环链表第一个相交节点判断即可 区别在于结束标志为走到入环节点
    # 而且不用考虑没有找到的情况 在这种情况下是一定能找到的
    if a_loop == b_loop:
        a_cur, b_cur = a_head, b_head
        a_len_minus_b_len = 0
        while a_cur.next != a_loop:
            a_len_minus_b_len += 1
            a_cur = a_cur.next
        while b_cur.next != b_loop:
            a_len_minus_b_len -= 1
            b_cur = b_cur.next
        if a_len_minus_b_len > 0:
            node_1 = a_head
            node_2 = b_head
        else:
            node_1 = b_head
            node_2 = a_head
        for _ in range(abs(a_len_minus_b_len)):
            node_1 = node_1.next
        while node_1 != node_2:
            node_1 = node_1.next
            node_2 = node_2.next
        return node_1
    # 如果入环节点不一致 则有两种情况
    # 第一种情况是两有环链表不相交 第二种情况则是两有环链表共享环
    # 让其中一个有环链表从其入环链表开始不断移动 若能遇上另一个有环链表的入环节点 则说明其共享环 返回任意其任意一个入环节点即可
    # 若回到其入环位置都没有遇到 则说明两有环链表不相交
    else:
        node = a_loop.next
        while node != a_loop:
            if node == b_loop:
                return a_loop
            node = node.next
        return None


def get_intersect_node(a_head: Node, b_head: Node):
    if a_head is None or b_head is None:
        return None
    a_loop = get_loop_node(a_head)
    b_loop = get_loop_node(b_head)
    if a_loop is None and b_loop is None:
        return intersect_no_loop(a_head, b_head)
    if a_loop is not None and b_loop is not None:
        return intersect_both_loop(a_head, b_head, a_loop, b_loop)
    return None
