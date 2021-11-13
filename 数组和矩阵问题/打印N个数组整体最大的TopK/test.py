# -*- coding: utf-8 -*- # 
# @Time    : 2021-11-11 14:35
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
from typing import List


class MaxHeap:
    def __init__(self, size):
        self.size = size
        self.element_num = 0
        self.array = [(0, 0, 0) for _ in range(size + 1)]  # 把该元素在对应数组的位置也放进元组中是一个很不错的想法

    def insert(self, num: tuple):
        self.element_num += 1
        self.array[self.element_num] = num
        self.swim(self.element_num)

    def del_max(self):
        if self.element_num > 0:
            max_num = self.array[1]  # 时刻铭记堆顶是1
            self.swap(1, self.element_num)
            self.array[self.element_num] = (0, 0, 0)
            self.element_num -= 1  # 先将堆的计数器减小 再进行下沉操作!!!
            self.sink(1)
            return max_num

    # 1 2 3 4 5 6
    # 这个最大堆是从1开始的 所以索引为i的元素 其两个子节点的索引分别为2*i 2*i+1 其父节点的索引为i//2
    def sink(self, index: int):
        while 2 * index <= self.element_num:
            child_index = 2 * index
            if child_index + 1 <= self.element_num and self.array[child_index][0] < self.array[child_index + 1][0]:
                child_index += 1
            if self.array[index][0] < self.array[child_index][0]:
                self.swap(index, child_index)
                index = child_index
            else:
                break

    def swim(self, index: int):
        while index // 2 >= 1:
            parent_index = index // 2
            if self.array[parent_index][0] < self.array[index][0]:
                self.swap(parent_index, index)
                index = parent_index
            else:
                break

    def swap(self, a_index: int, b_index: int):
        self.array[a_index], self.array[b_index] = self.array[b_index], self.array[a_index]


def print_top_k(array: List[List[int]], k):
    n = len(array)
    max_heap = MaxHeap(n)
    res = []
    for i in range(n):  # 这个是一定能正常进行的
        index = len(array[i]) - 1
        max_heap.insert((array[i][index], i, index))

    for _ in range(k):
        if max_heap.size == 0:
            break
        value, array_index, value_index = max_heap.del_max()
        res.append(str(value))
        if value_index != 0:
            max_heap.insert((array[array_index][value_index - 1], array_index, value_index - 1))
        else:
            max_heap.size -= 1  # 当发现有一个数组被取空的话 需要将最大堆的大小减一 原因是有可能所有数组的所有元素加起来的数目都没有k大 所以需要通过最大堆的大小进行提前中止

    return res


if __name__ == "__main__":
    a, b = map(int, input().split())
    test = []
    for _ in range(a):
        temp = list(map(int, input().split()))
        if len(temp) == 1:  # 这是因为测试用例中可能存在空数组 所以需要提前过滤掉
            continue
        test.append(temp[1:])

    print(' '.join(print_top_k(test, b)))
