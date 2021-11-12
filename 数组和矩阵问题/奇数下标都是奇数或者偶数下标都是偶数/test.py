# -*- coding: utf-8 -*- #
# @Time    : 2021/11/12 20:16
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :


def modify(array: list):
    if array is None or len(array) < 2:
        return
    even, odd = 0, 1
    while even < len(array) and odd < len(array):  # 请注意题目中的或者!
        if (array[len(array) - 1] & 1) == 0:
            array[even], array[len(array) - 1] = array[len(array) - 1], array[even]
            even += 2
        else:
            array[odd], array[len(array) - 1] = array[len(array) - 1], array[odd]
            odd += 2


if __name__ == "__main__":
    a = map(int, input().split())
    test = list(map(int, input().split()))
    modify(test)
    print(*test)
