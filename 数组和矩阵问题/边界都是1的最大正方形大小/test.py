# -*- coding: utf-8 -*- #
# @Time    : 2021/11/12 21:25
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
from typing import List


def set_border_map(matrix: List[List[int]]):
    row, col = len(matrix), len(matrix[0])
    down, right = [[0 for _ in range(col)] for _ in range(row)], [[0 for _ in range(col)] for _ in range(row)]

    # base case
    if matrix[row - 1][col - 1] == 1:
        right[row - 1][col - 1], down[row - 1][col - 1] = 1, 1

    for i in range(row - 2, -1, -1):
        if matrix[i][col - 1] == 1:
            down[i][col - 1], right[i][col - 1] = down[i + 1][col - 1] + 1, 1
        else:
            down[i][col - 1], right[i][col - 1] = 0, 0  # 这里其实不用写 因为初始化就是0

    for i in range(col - 2, -1, -1):
        if matrix[row - 1][i] == 1:
            down[row - 1][i], right[row - 1][i] = 1, right[row - 1][i + 1] + 1
        else:
            down[row - 1][i], right[row - 1][i] = 0, 0

    # transfer equation
    for i in range(row - 2, -1, -1):
        for j in range(col - 2, -1, -1):
            if matrix[i][j] == 1:
                down[i][j], right[i][j] = down[i + 1][j] + 1, right[i][j + 1] + 1
            else:
                down[i][j], right[i][j] = 0, 0

    return down, right


def get_max_size(matrix: List[List[int]]):
    down, right = set_border_map(matrix)
    size = min(len(matrix), len(matrix[0]))
    for try_size in range(size, 0, -1):  # 这是不能处理全为0的情况
        if has_size_of_border(try_size, down, right):
            return try_size

    return 0


def has_size_of_border(size: int, down: List[List[int]], right: List[List[int]]):
    for i in range(0, len(right) - size + 1):  # 这里不是len(right)-size
        for j in range(0, len(right[0]) - size + 1):
            if right[i][j] >= size and down[i][j] >= size and right[i + size - 1][j] >= size and down[i][
                j + size - 1] >= size:
                return True
    return False


if __name__ == "__main__":
    a = int(input())
    test = []
    for _ in range(a):
        test.append(list(map(int, input().split())))
    print(get_max_size(test))
