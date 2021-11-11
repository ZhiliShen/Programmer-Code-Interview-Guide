# -*- coding: utf-8 -*- # 
# @Time    : 2021-11-11 20:40
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :


def sort_1(array: list):  # 该解法有着完美洗牌的味道 最终形成的也是一个多米诺骨牌
    for i in range(len(array)):
        temp = array[i]
        while array[i] != i + 1:
            next_target = array[temp - 1]
            array[temp - 1] = temp
            temp = next_target


def sort_2(array: list):  # 该解法就把当前的位置当作了中转站
    for i in range(len(array)):
        while array[i] != i + 1:
            temp = array[i]
            array[i], array[temp - 1] = array[temp - 1], array[i]


if __name__ == "__main__":
    a = map(int, input().split())
    test = list(map(int, input().split()))
    sort_1(test)
    print(*test)
