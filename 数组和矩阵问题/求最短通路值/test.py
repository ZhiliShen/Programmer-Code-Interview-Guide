# -*- coding: utf-8 -*- # 
# @Time    : 2021-11-10 21:12
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
from typing import List
from collections import deque


def min_path_value(matrix: List[List[int]]):
    row, col = len(matrix), len(matrix[0])
    if row == 0 or col == 0 or matrix[0][0] != 1 or matrix[row - 1][col - 1] != 1:
        return -1
    res = -1
    dp = [[0 for _ in range(col)] for _ in range(row)]
    dp[0][0] = 1  # 不要忘记初始化
    queue = deque()
    queue.append((0, 0))
    while len(queue) != 0:
        cur_row, cur_col = queue.popleft()
        if cur_row == row - 1 and cur_col == col - 1:
            return dp[row - 1][col - 1]
        walk_to(dp[cur_row][cur_col], cur_row - 1, cur_col, dp, matrix, queue)
        walk_to(dp[cur_row][cur_col], cur_row + 1, cur_col, dp, matrix, queue)
        walk_to(dp[cur_row][cur_col], cur_row, cur_col - 1, dp, matrix, queue)
        walk_to(dp[cur_row][cur_col], cur_row, cur_col + 1, dp, matrix, queue)

    return res


def walk_to(cur: int, des_row: int, des_col: int, dp: List[List[int]], matrix: List[List[int]], queue: deque):
    row, col = len(matrix), len(matrix[0])
    if des_row < 0 or des_row > row - 1 or des_col < 0 or des_col > col - 1 or matrix[des_row][des_col] != 1 or \
            dp[des_row][des_col] != 0:
        return
    dp[des_row][des_col] = cur + 1
    queue.append((des_row, des_col))


if __name__ == "__main__":
    a, b = map(int, input().split())
    test = []
    for _ in range(a):
        test.append([int(i) for i in input()])
    print(min_path_value(test))
