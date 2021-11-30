# -*- coding: utf-8 -*- # 
# @Time    : 2021-11-30 10:40
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :


# 双向链表节点
class Node:
    def __init__(self, value):
        self.value = value
        self.last = None
        self.next = None


# 双向链表结构
class NodeDoubleLinkedList:
    def __init__(self):
        self.head = None  # 优先级最低的节点是头节点
        self.tail = None  # 优先级最高的节点是尾节点

    def add_node(self, node: Node):  # 当加入一个新的节点时 将新加入的节点放在尾部 并将该节点设置为新的尾节点
        if node is None:
            return
        if self.head is None:  # 如果是第一个节点 则头节点与尾节点都设置为该加入节点
            self.head = node
            self.tail = node
        else:  # 将尾节点的next指向该节点 并将该节点的last指向尾节点 同时将其设置为新的尾节点
            self.tail.next = node
            node.last = self.tail
            self.tail = node

    def move_node_to_tail(self, node: Node):  # 支持将双向链表中的任意节点分离并放到尾部
        if node == self.tail:  # 如果node已经是尾节点 则不进行任何操作
            return
        if node == self.head:  # 如果node是头节点
            self.head = self.head.next
            self.head.last = None
        else:
            node.next.last = node.last
            node.last.next = node.next
        self.tail.next = node
        node.last = self.tail
        node.next = None  # 不要忘了将node的next指向None
        self.tail = node

    def remove_head(self):  # 移除头节点 并返回该节点 同时将原头节点的next指向的节点设置为头节点
        if self.head is None:
            return
        node = self.head
        if self.head == self.tail:  # 如果双向链表只有一个节点
            self.head = None
            self.tail = None
        else:
            self.head = node.next
            self.head.last = None
            node.next = None  # 不要忘了将node的next指向None
        return node


# 写LRU需要注意
# 先写双向链表节点 再写双向链表 最后再写LRU结构时需要有node与key的双向映射
class LRU:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key2node = {}
        self.node2key = {}
        self.node_list = NodeDoubleLinkedList()

    def get(self, key):
        if key in self.key2node:
            res = self.key2node[key]
            self.node_list.move_node_to_tail(res)  # 每一次get都需要将当前node放置在尾部
            return res.value
        else:
            return None

    def set(self, key, value):
        if key in self.key2node:
            res = self.key2node[key]
            res.value = value
            self.node_list.move_node_to_tail(res)  # 当更改键的值时需要将当前node放置在尾部
        else:
            node = Node(value)
            self.key2node[key] = node
            self.node2key[node] = key
            self.node_list.add_node(node)  # 直接添加新节点时 会直接将node放置在尾部 因此不用再进行move_node_to_tail操作
            if len(self.key2node) == self.capacity + 1:  # 当LRU容量到达上限时需要移除最不常用元素
                self.remove_most_unused_cache()

    def remove_most_unused_cache(self):
        remove_node = self.node_list.remove_head()
        remove_key = self.node2key[remove_node]
        self.node2key.pop(remove_node)  # 需要同时从两张映射表中进行删除
        self.key2node.pop(remove_key)


if __name__ == "__main__":
    a, b = map(int, input().split())
    lru = LRU(b)
    for _ in range(a):
        a, *b = map(int, input().split())
        if a == 1:
            lru.set(b[0], b[-1])
        else:
            print('-1' if lru.get(b[0]) is None else lru.get(b[0]))
