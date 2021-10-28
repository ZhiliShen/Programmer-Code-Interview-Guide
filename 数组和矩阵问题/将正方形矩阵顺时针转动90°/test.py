# -*- coding: utf-8 -*- # 
# @Time    : 2021-10-28 12:43
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
from typing import List


def rotate(matrix: List[List[str]]):
    top_col, top_row = 0, 0
    bot_col, bot_row = len(matrix)-1, len(matrix[0])-1
    while top_col < bot_col and top_row < bot_row:
        rotate_edge(matrix, top_row, top_col, bot_row, bot_col)
        top_col += 1
        top_row += 1
        bot_col -= 1
        bot_row -= 1


def rotate_edge(matrix: List[List[str]], top_row: int, top_col: int, bot_row: int, bot_col: int):
    num = bot_col - top_col
    for i in range(num):
        tmp = matrix[top_row][top_col+i]
        matrix[top_row][top_col+i] = matrix[bot_row-i][top_col]
        matrix[bot_row-i][top_col] = matrix[bot_row][bot_col-i]
        matrix[bot_row][bot_col-i] = matrix[top_row+i][bot_col]
        matrix[top_row+i][bot_col] = tmp


if __name__ == "__main__":
    a, b = map(int, input().split())
    test = []
    for _ in range(a):
        test.append(input().split())
    rotate(test)
    for row in test:
        print(' '.join(row))
