# -*- coding: utf-8 -*- #
# @Time    : 2021/11/13 16:57
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :


class heap:
    def __init__(self, cmp, size):
        self.cmp = cmp
        self.size = size
        self.count = 0
        self.array = [(0, 0) for _ in range(self.size + 1)]

    # 索引是从1开始的 索引为i的节点的子节点是2*i与2*i+1 父节点是i//2
    def insert(self, program: tuple):
        self.count += 1
        self.array[self.count] = program
        self.swim(self.count)

    def del_top(self):
        if self.count > 0:
            top_ele = self.array[1]
            self.array[1] = self.array[self.count]
            self.array[self.count] = (0, 0)
            self.count -= 1  # 不要忘记将当前元素个数减1
            self.sink(1)  # 先将堆的计数器减小 再进行下沉操作!!!
            return top_ele
        else:
            return None

    def top(self):
        if self.count > 0:
            return self.array[1]
        else:
            return None

    def sink(self, index: int):
        while index * 2 <= self.count:
            child_index = 2 * index
            if child_index + 1 <= self.count and self.cmp(self.array, child_index, child_index + 1):
                child_index += 1
            if self.cmp(self.array, index, child_index):
                self.array[index], self.array[child_index] = self.array[child_index], self.array[index]
                index = child_index
            else:
                break

    def swim(self, index: int):
        while index // 2 >= 1:
            parent_index = index // 2
            if self.cmp(self.array, parent_index, index):
                self.array[index], self.array[parent_index] = self.array[parent_index], self.array[index]
                index = parent_index
            else:
                break


def program_cost_cmp(array: list, a_index: int, b_index: int):
    if array[a_index][0] > array[b_index][0]:
        return True
    else:
        return False


def program_profit_cmp(array: list, a_index: int, b_index: int):
    if array[a_index][1] < array[b_index][1]:
        return True
    else:
        return False


def get_max_money(w, k, programs: list):
    if w < 0 or k < 0 or programs is None:
        return w

    cost_min_heap, profit_max_heap = heap(program_cost_cmp, len(programs)), heap(program_profit_cmp, len(programs))
    for program in programs:
        cost_min_heap.insert(program)

    for _ in range(k):  # 这个逻辑写得很好
        # 如果有项目而且有可以做的项目 则将其解锁
        while cost_min_heap.count > 0 and cost_min_heap.top()[0] <= w:
            profit_max_heap.insert(cost_min_heap.del_top())
        # 如果没有可以做的项目 则直接返回
        if profit_max_heap.count == 0:
            return w
        # 每次新做一个项目都意味折可以解锁新的项目 所以在下一轮的循环中需要重新解锁
        w += profit_max_heap.del_top()[1]

    return w


if __name__ == "__main__":
    a, b, c = map(int, input().split())
    d = list(map(int, input().split()))
    e = list(map(int, input().split()))
    test = []
    for i, j in zip(d, e):
        test.append((i, j))
    print(get_max_money(b, c, test))
