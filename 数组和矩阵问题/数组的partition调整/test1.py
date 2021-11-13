# -*- coding: utf-8 -*- # 
# @Time    : 2021-11-12 17:04
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test1.py
# @Notice  :


def left_unique(array: list):
    if array is None or len(array) < 2:
        return
    unique = 0
    for index in range(1, len(array)):
        if array[index] != array[unique]:
            unique += 1
            array[unique], array[index] = array[index], array[unique]


if __name__ == "__main__":
    a = map(int, input().split())
    test = list(map(int, input().split()))
    left_unique(test)
    print(*test)
