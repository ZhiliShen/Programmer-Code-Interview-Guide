# -*- coding: utf-8 -*- # 
# @Time    : 2021-12-10 15:25
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test1.py
# @Notice  :
from collections import defaultdict


class Heap:
    def __init__(self, cmp):
        self.count = 0
        self.array = []
        self.cmp = cmp

    def insert(self, num):
        self.array.append(num)
        self.swim(self.count)
        self.count += 1

    # i->2*i+1 2*i+2 i->(i-1)//2
    def swim(self, index: int):
        while (index - 1) // 2 >= 0:
            parent_index = (index - 1) // 2
            if self.cmp(self.array, parent_index, index):
                self.array[parent_index], self.array[index] = self.array[index], self.array[parent_index]
                index = parent_index
            else:
                break

    def top(self):
        if self.count > 0:
            return self.array[0]

    def del_top(self):
        if self.count > 0:
            top_ele = self.array[0]
            self.array[0] = self.array[-1]
            self.array.pop(-1)
            self.count -= 1
            self.sink(0)
            return top_ele

    def sink(self, index: int):
        while 2 * index + 1 < self.count:
            child_index = 2 * index + 1
            if child_index + 1 < self.count and self.cmp(self.array, child_index, child_index + 1):
                child_index += 1
            if self.cmp(self.array, index, child_index):
                self.array[index], self.array[child_index] = self.array[child_index], self.array[index]
                index = child_index
            else:
                break


def min_heap_cmp(array: list, a_index: int, b_index: int):
    if array[a_index][1] > array[b_index][1]:
        return True
    elif array[a_index][1] < array[b_index][1]:
        return False
    elif array[a_index][0] < array[b_index][0]:
        return True
    else:
        return False


def tuple_cmp(a_tuple: tuple, b_tuple: tuple):
    if a_tuple[1] > b_tuple[1]:
        return True
    elif a_tuple[1] < b_tuple[1]:
        return False
    elif a_tuple[0] < b_tuple[0]:  # 这里很重要 决定出现次数相等的字母谁出堆谁入堆
        return True
    else:
        return False


def print_top_k_and_rank(array: list, k: int):
    char2count = defaultdict(int)
    for char in array:
        char2count[char] += 1
    min_heap = Heap(min_heap_cmp)
    count = 0
    for key, value in char2count.items():
        if count != k:
            min_heap.insert((key, value))
            count += 1
        else:
            if tuple_cmp((key, value), min_heap.top()):
                min_heap.del_top()
                min_heap.insert((key, value))

    # 将数字从小到大排列需要的是大根堆 因为这样每次都能确定一个最大的数 并将其放在最后
    # 而此时我们需要将其从大到小排列 因此此时需要的最小堆
    for _ in range(k):
        min_heap.array[0], min_heap.array[min_heap.count - 1] = min_heap.array[min_heap.count - 1], min_heap.array[0]
        min_heap.count -= 1
        min_heap.sink(0)

    return min_heap.array


if __name__ == "__main__":
    a, b = map(int, input().split())
    test = []
    for _ in range(a):
        test.append(input())
    for temp in print_top_k_and_rank(test, b):
        print(temp[0], temp[1])
