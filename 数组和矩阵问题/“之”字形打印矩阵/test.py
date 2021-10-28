# -*- coding: utf-8 -*- # 
# @Time    : 2021-10-28 13:05
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
from typing import List


def print_matrix_zigzag(matrix: List[List[str]]):
    top_row, top_col = 0, 0
    bot_row, bot_col = 0, 0
    row, col = len(matrix) - 1, len(matrix[0]) - 1
    result = []
    direction = True
    while top_row != row+1 and bot_col != col+1:  # 这里的边界条件是+1 而且其实两个条件只要一个达成即可 不要有bot_row = row+1 因为内部判断就已经已经断绝了此类的可能
        print_level(result, matrix, top_row, top_col, bot_row, bot_col, direction)
        if top_col < col:
            top_col += 1
        else:
            top_row += 1
        if bot_row < row:
            bot_row += 1
        else:
            bot_col += 1
        direction = not direction

    print(' '.join(result))


def print_level(result: List[str], matrix: List[List[str]], top_row: int, top_col: int, bot_row: int, bot_col: int,
                direction: bool):
    if not direction:
        while top_row != bot_row+1:
            result.append(matrix[top_row][top_col])
            top_row += 1
            top_col -= 1
    else:
        while bot_row != top_row-1:  # top_row-1代表在上面
            result.append(matrix[bot_row][bot_col])
            bot_row -= 1
            bot_col += 1


if __name__ == "__main__":
    a, b = map(int, input().split())
    test = []
    for _ in range(a):
        test.append(input().split())
    print_matrix_zigzag(test)
