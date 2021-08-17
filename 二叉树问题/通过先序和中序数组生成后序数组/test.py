# -*- coding: utf-8 -*- #
# @Time    : 2021/8/8 11:13
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
import sys
from typing import List


def get_pos_arr(pre_arr: List, in_arr: List):
    if len(pre_arr) == 0:
        return
    global n
    pos_arr[n-1] = pre_arr[0]
    n -= 1
    index = in_arr.index(pre_arr[0])
    get_pos_arr(pre_arr[index+1:], in_arr[index+1:])
    get_pos_arr(pre_arr[1:index+1], in_arr[:index])


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split(" ")))
    b = list(map(int, sys.stdin.readline().split(" ")))
    pos_arr = [None for i in range(n)]
    get_pos_arr(a, b)
    print(" ".join([str(k) for k in pos_arr]))
