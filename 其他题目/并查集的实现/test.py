# -*- coding: utf-8 -*- #
# @Time    : 2021-12-02 19:56
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
from collections import deque


class UnionFindSet:
    def __init__(self, num: int):
        self.value2father = {}
        self.father2rank = {}
        for value in range(1, num + 1):
            self.value2father[value] = value
            self.father2rank[value] = 1

    def find_head(self, value):
        stack = deque()
        while value != self.value2father[value]:
            stack.append(value)
            value = self.value2father[value]
        while len(stack) != 0:
            self.value2father[stack.pop()] = value
        return value

    def is_same_set(self, a_value, b_value):
        if a_value in self.value2father and b_value in self.value2father:
            return self.find_head(a_value) == self.find_head(b_value)
        return False

    def union(self, a_value, b_value):
        if a_value in self.value2father and b_value in self.value2father:
            a_father, b_father = self.find_head(a_value), self.find_head(b_value)
            if a_father != b_father:
                big_father = a_father if self.father2rank[a_father] > self.father2rank[b_father] else b_father
                small_father = b_father if big_father is a_father else a_father
                self.value2father[small_father] = big_father
                self.father2rank[big_father] = self.father2rank[a_father] + self.father2rank[b_father]
                self.father2rank.pop(small_father)


class UnionFindSet_1:
    def __init__(self, num: int):
        self.value2father = list(range(num + 1))
        self.father2rank = [1 for _ in range(num + 1)]

    def find_head(self, value):
        if self.value2father[value] == value:
            return value
        return self.find_head(self.value2father[value])

    def is_same_set(self, a_value, b_value):
        return self.find_head(a_value) == self.find_head(b_value)

    def union(self, a_value, b_value):
        a_father, b_father = self.find_head(a_value), self.find_head(b_value)
        if a_father != b_father:
            if self.father2rank[a_father] < self.father2rank[b_father]:
                self.value2father[a_father] = b_father  # 没必要清空father2rank[a_father]的值 因为以后不会用到了
                self.father2rank[b_father] = self.father2rank[a_father] + self.father2rank[b_father]
            else:
                self.value2father[b_father] = a_father
                self.father2rank[a_father] = self.father2rank[b_father] + self.father2rank[a_father]


if __name__ == "__main__":
    a, b = map(int, input().split())
    union_find_set = UnionFindSet_1(a)
    for _ in range(b):
        c, *d = map(int, input().split())
        if c == 1:
            print('Yes' if union_find_set.is_same_set(d[0], d[-1]) else 'No')
        else:
            union_find_set.union(d[0], d[-1])
