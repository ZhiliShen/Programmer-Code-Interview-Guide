# -*- coding: utf-8 -*- #
# @Time    : 2021-10-27 18:25
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
from typing import List


def spiral_order_print(matrix: List[List[str]]):
    top_row, top_col = 0, 0
    bottom_row, bottom_col = len(matrix) - 1, len(matrix[0]) - 1
    result = []
    while top_col <= bottom_col and top_row <= bottom_row:  # 当矩阵大小为1x1时 此时四个值均相等 但还是需要进行打印 因此边界条件需要注意
        print_edge(result, matrix, top_row, top_col, bottom_row, bottom_col)
        top_row += 1
        top_col += 1
        bottom_row -= 1
        bottom_col -= 1
    print(' '.join(result))


def print_edge(result: List[str], matrix: List[List[str]], top_row: int, top_col: int, bottom_row: int,
               bottom_col: int):
    if top_row == bottom_row:  # 子矩阵只有一行的时候 处理逻辑是不一样的
        for i in range(top_col, bottom_col + 1):
            result.append(matrix[top_row][i])
        return  # 注意return的缩进
    if top_col == bottom_col:  # 子矩阵只有一列的时候 处理逻辑是不一样的
        for i in range(top_row, bottom_row + 1):
            result.append(matrix[i][top_col])
        return  # 注意return的缩进
    cur_col = top_col
    while cur_col != bottom_col:
        result.append(matrix[top_row][cur_col])
        cur_col += 1
    cur_row = top_row
    while cur_row != bottom_row:
        result.append(matrix[cur_row][bottom_col])
        cur_row += 1
    while cur_col != top_col:
        result.append(matrix[bottom_row][cur_col])
        cur_col -= 1
    while cur_row != top_row:
        result.append(matrix[cur_row][top_col])
        cur_row -= 1


if __name__ == "__main__":
    a, b = map(int, input().split())
    test = []
    for _ in range(a):
        test.append(input().split())
    spiral_order_print(test)
