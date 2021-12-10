# -*- coding: utf-8 -*- # 
# @Time    : 2021-12-10 17:57
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test2.py
# @Notice  :


class Node:
    def __init__(self, string: str):
        self.value = string
        self.times = 1


class TopKRecord:
    def __init__(self, size):
        self.max_heap = [None for _ in range(size)]
        self.count = 0
        self.string2node = {}
        self.node2index = {}

    def insert(self, string):
        pre_index = -1
        if string not in self.string2node:
            cur_node = Node(string)
            self.string2node[string] = cur_node
            self.node2index[cur_node] = -1
        else:
            cur_node = self.string2node[string]
            cur_node.times += 1
            pre_index = self.node2index[cur_node]
        if pre_index == -1:  # 不在堆中 则根据堆的大小决定相应操作
            if self.count == len(self.max_heap):
                if self.max_heap[0].times < cur_node.times:
                    self.node2index[self.max_heap[0]] = -1
                    self.node2index[cur_node] = 0
                    self.max_heap[0] = cur_node
                    self.sink(0)
            else:
                self.node2index[cur_node] = self.count
                self.max_heap[self.count] = cur_node
                self.swim(self.count)
                self.count += 1
        else:
            self.sink(pre_index)  # 注意这里是小根堆 所以当对应的字符串的出现次数增加时 需要将其进行下沉操作

    def sink(self, index: int):
        while 2*index+1 < self.count:
            child_index = 2*index+1
            if child_index+1 < self.count and self.max_heap[child_index].times > self.max_heap[child_index+1].times:
                child_index += 1
            if self.max_heap[index].times > self.max_heap[child_index].times:
                self.swap(index, child_index)
                index = child_index
            else:
                break

    def swap(self, a_index: int, b_index: int):
        self.node2index[self.max_heap[a_index]] = b_index  # 交换的同时也要改变在字典中对应的位置
        self.node2index[self.max_heap[b_index]] = a_index
        self.max_heap[a_index], self.max_heap[b_index] = self.max_heap[b_index], self.max_heap[a_index]

    def swim(self, index: int):
        while (index-1)//2 >= 0:
            parent_index = (index-1)//2
            if self.max_heap[parent_index].times > self.max_heap[index].times:
                self.swap(parent_index, index)
            else:
                break

    def print_top_k(self):
        for i in range(len(self.max_heap)):
            if self.max_heap[i] is None:
                break
            else:
                print(self.max_heap[i].value, self.max_heap[i].times)


if __name__ == "__main__":
    top_k_record = TopKRecord(3)
    top_k_record.insert('A')
    top_k_record.insert('B')
    top_k_record.insert('A')
    top_k_record.insert('C')
    top_k_record.insert('B')
    top_k_record.print_top_k()
    print(" ")
    top_k_record.insert('A')
    top_k_record.insert('B')
    top_k_record.insert('D')
    top_k_record.insert('D')
    top_k_record.insert('D')
    top_k_record.print_top_k()
    print(" ")
    top_k_record.insert('E')
    top_k_record.insert('E')
    top_k_record.insert('E')
    top_k_record.insert('E')
    top_k_record.insert('E')
    top_k_record.print_top_k()
