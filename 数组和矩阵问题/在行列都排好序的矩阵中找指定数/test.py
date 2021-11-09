# -*- coding: utf-8 -*- # 
# @Time    : 2021-11-09 11:12
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
from typing import List


def is_contains(matrix: List[List[int]], k: int):
    row = len(matrix)
    col = len(matrix[0])

    cur_row, cur_col = 0, col - 1
    while cur_row <= row - 1 and cur_col >= 0:
        if matrix[cur_row][cur_col] == k:
            return 'Yes'
        elif matrix[cur_row][cur_col] > k:
            cur_col -= 1
        else:
            cur_row += 1
    return 'No'


if __name__ == "__main__":
    a, b, c = map(int, input().split())
    test = []
    for _ in range(a):
        test.append(list(map(int, input().split())))
    print(is_contains(test, c))
