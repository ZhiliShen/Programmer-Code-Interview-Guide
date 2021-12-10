# -*- coding: utf-8 -*- # 
# @Time    : 2021-12-10 14:35
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :


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
        while (index-1)//2 >= 0:
            parent_index = (index-1)//2
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
        while 2*index+1 < self.count:
            child_index = 2*index+1
            if child_index+1 < self.count and self.cmp(self.array, child_index, child_index+1):
                child_index += 1
            if self.cmp(self.array, index, child_index):
                self.array[index], self.array[child_index] = self.array[child_index], self.array[index]
                index = child_index
            else:
                break


def max_heap_cmp(array: list, a_index: int, b_index: int):
    if array[a_index][0] < array[b_index][0]:
        return True
    else:
        return False


def top_k_sum(array_a: list, array_b: list, k: int):
    len_a, len_b = len(array_a), len(array_b)
    index_a, index_b = len_a-1, len_b-1
    max_heap = Heap(max_heap_cmp)
    max_heap.insert((array_a[index_a]+array_b[index_b], index_a, index_b))
    res = []
    res_set = set()
    # 如果弹出来的是(5, 5) 则之后入堆的则是(5, 4) (4, 5) 如果之后弹出的是(5, 4) 则之后入堆的则是(4, 4) (5, 3)
    # 如果之后弹出的是(4, 5) 则之后入堆的则是(4, 4) (3, 5) 此处出现了同一组位置重复入堆的情况 所以需要通过集合避免
    res_set.add((index_a, index_b))
    k = min(k, len_a*len_b)  # 避免越界
    for _ in range(k):
        cur_sum, index_a, index_b = max_heap.del_top()
        res.append(cur_sum)
        if index_a-1 >= 0 and (index_a-1, index_b) not in res_set:
            max_heap.insert((array_a[index_a-1]+array_b[index_b], index_a-1, index_b))
            res_set.add((index_a-1, index_b))
        if index_b-1 >= 0 and (index_a, index_b-1) not in res_set:
            max_heap.insert((array_a[index_a]+array_b[index_b-1], index_a, index_b-1))
            res_set.add((index_a, index_b-1))

    return res


if __name__ == "__main__":
    a, b = map(int, input().split())
    test_a = list(map(int, input().split()))
    test_b = list(map(int, input().split()))
    print(*top_k_sum(test_a, test_b, b))
