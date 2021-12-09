# -*- coding: utf-8 -*- # 
# @Time    : 2021-12-08 20:56
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :

class Heap:
    def __init__(self, cmp):
        self.array = []
        self.count = 0
        self.cmp = cmp

    # 在以0开始的数组中 索引为i的子节点为2*i+1与2*(i+1) 索引为i的父节点为(i-1)//2
    def insert(self, num):
        self.array.append(num)
        self.swim(self.count)
        self.count += 1

    def swim(self, index: int):
        while (index - 1) // 2 >= 0:  # 这里一定要打括号！
            parent_index = (index - 1) // 2
            if self.cmp(self.array, parent_index, index):
                self.array[parent_index], self.array[index] = self.array[index], self.array[parent_index]
                index = parent_index
            else:
                break

    def del_top(self):
        if self.count > 0:
            top_ele = self.array[0]
            self.array[0] = self.array[-1]
            self.array.pop(-1)
            self.count -= 1
            self.sink(0)
            return top_ele
        else:
            return None

    def sink(self, index):
        while 2 * index + 1 < self.count:
            child_index = 2 * index + 1
            if child_index + 1 < self.count and self.cmp(self.array, child_index, child_index + 1):
                child_index += 1
            if self.cmp(self.array, index, child_index):
                self.array[index], self.array[child_index] = self.array[child_index], self.array[index]
                index = child_index
            else:
                break

    def top(self):
        if self.count > 0:
            return self.array[0]
        else:
            return None


def min_cmp(array: list, a_index: int, b_index: int):
    if array[a_index] > array[b_index]:
        return True
    else:
        return False


def max_cmp(array: list, a_index: int, b_index: int):
    if array[a_index] < array[b_index]:
        return True
    else:
        return False


class MedianHolder:
    def __init__(self):
        self.max_heap = Heap(max_cmp)
        self.min_heap = Heap(min_cmp)

    def insert(self, num):
        if self.max_heap.count == 0 or num <= self.max_heap.top():  # 普通班没有人 或者分数比普通班最厉害的人低 就进入普通班
            self.max_heap.insert(num)
        else:
            self.min_heap.insert(num)
        self.modify_two_heaps()  # 入学考试之后 不要忘记调平班级人数

    def modify_two_heaps(self):
        if self.max_heap.count == self.min_heap.count + 2:  # 当普通班的人数比实验班的人多的时候
            self.min_heap.insert(self.max_heap.del_top())  # 向实验班中输送普通班中分数最高的人
        if self.min_heap.count == self.max_heap.count + 2:  # 当实验班的人数比普通班的人多的时候
            self.max_heap.insert(self.min_heap.del_top())  # 向普通班中输送实验班中分数最低的人

    def get_median(self):
        if self.max_heap.count == 0:
            return None
        if self.max_heap.count == self.min_heap.count:
            return (self.max_heap.top() + self.min_heap.top()) / 2
        else:
            if self.max_heap.count > self.min_heap.count:
                return self.max_heap.top()
            else:
                return self.min_heap.top()
