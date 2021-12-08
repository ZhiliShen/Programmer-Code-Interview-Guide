# -*- coding: utf-8 -*- #
# @Time    : 2021-12-08 17:23
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None


class MessageBox:
    def __init__(self):
        self.head2node = {}
        self.tail2node = {}
        self.last_print = 0

    def receive(self, value: int):
        if value < 1:
            return
        cur_node = Node(value)
        self.head2node[value] = cur_node
        self.tail2node[value] = cur_node
        if value+1 in self.head2node:
            cur_node.next = self.head2node[value+1]
            # self.head2node[value] = cur_node  # 之前操作过了 就不用再写一遍了
            self.head2node.pop(value+1)
            self.tail2node.pop(value)  # 记得将其从尾节点映射表中删除
        if value-1 in self.tail2node:
            pre_node = self.tail2node[value-1]
            pre_node.next = cur_node
            # self.tail2node[value] = cur_node  # 之前操作过了 就不用再写了
            self.tail2node.pop(value-1)
            self.head2node.pop(value)  # 记得将其从头节点映射表中删除
        if self.last_print+1 in self.head2node:
            self.print_1(value)

    def print_1(self, value: int):
        self.last_print += 1
        node = self.head2node[self.last_print]
        self.head2node.pop(self.last_print)
        while node is not None:
            print(node.value, value)
            node = node.next
            self.last_print += 1
        self.last_print -= 1  # 这里不要忘记把last_print恢复为原来的样子
        self.tail2node.pop(self.last_print)


if __name__ == "__main__":
    a = int(input())
    test = list(map(int, input().split()))
    message_box = MessageBox()
    for temp in test:
        message_box.receive(temp)
