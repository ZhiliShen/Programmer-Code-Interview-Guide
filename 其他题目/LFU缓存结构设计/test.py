# -*- coding: utf-8 -*- # 
# @Time    : 2021-11-30 14:52
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
import collections


#                        next   next
#    bucket 1: node1(head)->node2->node3(tail)  (head_bucket:调用次数最少的桶)  (node1(head):调用发生最新的节点) (node3(tail):调用发生最早的节点)
#     |   ^              <-     <-
# down|   |up            last   last
#     _   |              next   next
#    bucket 2: node4(head)->node5->node6(tail)
#     |   ^              <-     <-
# down|   |up            last   last
#     _   |              next   next
#    bucket 3: node7(head)->node8->node9(tail)
#     |   ^              <-     <-
# down|   |up            last   last
#     _   |              next   next
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.last = None
        self.next = None
        self.times = 0


class Bucket:
    def __init__(self, node: Node):
        self.head = node  # 调用发生最新的节点
        self.tail = node  # 调用发生最早的节点
        self.up = None
        self.down = None

    def add_node_to_head(self, node: Node):  # 在桶中加入节点时 必然是发生set或get操作 因此需要将该节点设为头节点 以表明该节点的调用是最新的
        node.next = self.head
        self.head.last = node
        self.head = node

    def is_empty(self):
        return self.head is None

    def delete_node(self, node: Node):
        if self.head is self.tail:  # 需要删除节点 而当前只有一个节点 所以肯定要删除唯一的节点
            self.head = None
            self.tail = None
        else:
            if node is self.head:  # 如果需要删除的节点是头节点
                self.head = node.next
                self.head.last = None
            elif node is self.tail:  # 如果需要删除的节点是尾节点
                self.tail = node.last
                self.tail.next = None
            else:
                node.last.next = node.next
                node.next.last = node.last
        node.last = None  # 将节点独立出来
        node.next = None


class LFU:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.key2node = {}
        self.node2bucket = {}
        self.head_bucket = None  # 调用次数最少的桶

    def set(self, key: int, value: int):
        if self.capacity == 0:
            return
        if key in self.key2node:
            node = self.key2node[key]
            node.value = value
            node.times += 1
            bucket = self.node2bucket[node]
            self.move(node, bucket)
        else:
            if self.size == self.capacity:  # 如果当前容量已满 则需要删除
                node = self.head_bucket.tail
                self.head_bucket.delete_node(node)
                self.modify_bucket(self.head_bucket)
                self.key2node.pop(node.key)  # 这行代码表明了node需要记录key的原因 方便从self.key2node中删除该节点
                self.node2bucket.pop(node)
                self.size -= 1
            node = Node(key, value)  # 新创建的节点的调用次数必然是1 因此应当加入head_bucket
            if self.head_bucket is None:
                self.head_bucket = Bucket(node)
            else:
                if self.head_bucket.head.times == node.times:  # 如果head_bucket符合次数要求 可以直接将node加入进去
                    self.head_bucket.add_node_to_head(node)
                else:
                    new_bucket = Bucket(node)  # 如果head_bucket不符合次数要求 则node所在的bucket应当设置为head_bucket
                    new_bucket.down = self.head_bucket
                    self.head_bucket.up = new_bucket
                    self.head_bucket = new_bucket
            self.key2node[key] = node
            self.node2bucket[node] = self.head_bucket
            self.size += 1

    def get(self, key):
        if key not in self.key2node:
            return None
        node = self.key2node[key]
        node.times += 1
        cur_bucket = self.node2bucket[node]
        self.move(node, cur_bucket)
        return node.value

    # remove_node_bucket是刚刚减少一个节点的桶 判断刚刚减少一个节点的桶是否为空 同时保证桶之间是双向链表
    def modify_bucket(self, remove_node_bucket: Bucket):
        if remove_node_bucket.is_empty():  # 如果这个减少了一个节点的桶变成了空桶
            if self.head_bucket is remove_node_bucket:  # 如果这个空桶是LRU中调用次数最少的桶
                self.head_bucket = remove_node_bucket.down  # 设置新的调用次数最少的桶
                if self.head_bucket is not None:  # 如果LRU中仍然有桶
                    self.head_bucket.up = None  # 将新的调用次数最少的桶的up指向空
            else:  # 如果这个空桶不是LRU中调用次数最少的桶
                remove_node_bucket.up.down = remove_node_bucket.down  # 去除这个桶
                if remove_node_bucket.down is not None:
                    remove_node_bucket.down.up = remove_node_bucket.up  # 将这个桶下边的桶的up指针指向这个桶上边的桶
            return True  # 如果这个减少了一个节点的桶变成了空桶 则返回True
        else:
            return False  # 如果这个减少了一个节点的桶没有变成空桶 则返回False

    # 该节点在bucket当中 该节点的次数+1 需要从该bucket删除 并放入新桶 同时保证桶之间是双向链表 节点之间是双向链表
    def move(self, node: Node, bucket: Bucket):
        bucket.delete_node(node)  # 首先从桶当中删除该节点
        if self.modify_bucket(bucket):  # 如果这个减少该节点的桶变成了空桶
            pre_bucket = bucket.up  # 若要创建新桶 则该新桶的up则指向减少该节点的桶的上一个桶
        else:
            pre_bucket = bucket  # 否则指向减少该节点的桶
        next_bucket = bucket.down  # 找出可能可以放置新节点的桶
        if next_bucket is None:  # 如果没有这个桶
            new_bucket = Bucket(node)  # 创建新桶
            if pre_bucket is not None:  # 连接pre_bucket与new_bucket
                pre_bucket.down = new_bucket
            new_bucket.up = pre_bucket
            if self.head_bucket is None:  # 如果创建新桶的时候 self.head_bucket仍然为空 则将其记录为self.head_bucket
                self.head_bucket = new_bucket
            self.node2bucket[node] = new_bucket  # 不要忘记更新
        else:
            if next_bucket.head.times == node.times:  # 如果next_bucket符合次数要求 可以直接将node加入进去
                next_bucket.add_node_to_head(node)
                self.node2bucket[node] = next_bucket
            else:  # 如果next_bucket不符合次数要求 不可以直接加入进去
                new_bucket = Bucket(node)
                if pre_bucket is not None:
                    pre_bucket.down = new_bucket
                new_bucket.up = pre_bucket  # 连接pre_bucket与new_bucket new_bucket与next_bucket
                new_bucket.down = next_bucket
                next_bucket.up = new_bucket
                if self.head_bucket is next_bucket:  # 如果创建新桶的时候 self.head_bucket是next_bucket 则将新桶记录为self.head_bucket
                    self.head_bucket = new_bucket
                self.node2bucket[node] = new_bucket


def create_bucket():
    fake_head = Node(0, 0)
    fake_tail = Node(0, 0)
    fake_head.next = fake_tail
    fake_tail.last = fake_head
    return fake_head, fake_tail


class LFU_1:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0
        self.freq2bucket = collections.defaultdict(create_bucket)  # 当字典中的key不存在时 会引发异常 defaultdict在key不存在时提供默认值
        self.key2node = {}

    def delete(self, node: Node):
        if node.last is not None:  # 因为set的时候有可能传进来的node是新创建的 也可能是已存在的 所以需要根据node的不同状态决定node是否需要删除
            node.last.next = node.next
            node.next.last = node.last
            if node.last is self.freq2bucket[node.times] and node.next is self.freq2bucket[node.times][-1]:  # 如果该node所在的bucket已经为空 则需要从字典中删除该bucket
                self.freq2bucket.pop(node.times)
            return node

    def increase(self, node: Node):
        node.times += 1
        self.delete(node)
        pre_node = self.freq2bucket[node.times][-1].last
        node.last = pre_node
        node.next = pre_node.next
        pre_node.next.last = node
        pre_node.next = node
        if node.times == 1:
            self.min_freq = 1
        elif self.min_freq == node.times - 1:  # 如果最小频次对应的桶已经为空 则需要对最小频次进行更新
            head, tail = self.freq2bucket[self.min_freq]
            if head.next is tail:
                self.min_freq = node.times

    def get(self, key: int):
        if key in self.key2node:
            self.increase(self.key2node[key])
            return self.key2node[key].value
        return None

    def set(self, key, value):
        if self.capacity == 0:
            return
        if key in self.key2node:
            node = self.key2node[key]
            node.value = value
        else:
            node = Node(key, value)
            self.key2node[key] = node
            self.size += 1
        if self.size > self.capacity:
            self.size -= 1
            delete_node = self.delete(self.freq2bucket[self.min_freq][0].next)
            self.key2node.pop(delete_node.key)
        self.increase(node)


if __name__ == "__main__":
    a, b = map(int, input().split())
    lfu = LFU_1(b)
    for _ in range(a):
        a, *b = map(int, input().split())
        if a == 1:
            lfu.set(b[0], b[-1])
        else:
            print('-1' if lfu.get(b[0]) is None else lfu.get(b[0]))
