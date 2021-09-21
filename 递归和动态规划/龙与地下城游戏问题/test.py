# -*- coding: utf-8 -*- # 
# @Time    : 2021-09-20 21:32
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
import sys
from typing import List


def dynamic_programming(matrix: List[List[int]]):
    row = len(matrix)
    col = len(matrix[0])
    more = max(row, col)
    less = min(row, col)
    dp = [None for i in range(less)]

    # base case:
    if matrix[row-1][col-1] > 0:
        dp[-1] = 1
    else:
        dp[-1] = 1 - matrix[row-1][col-1]

    for j in range(less-2, -1, -1):  # 递减的时候仔细写是增加还是减少
        dp[j] = max(dp[j+1] - (matrix[row-1][j] if row == more else matrix[j][col-1]), 1)

    # transfer equation
    for i in range(more-2, -1, -1):
        dp[-1] = max(dp[-1] - (matrix[i][-1] if row == more else matrix[-1][i]), 1)
        for j in range(less-2, -1, -1):
            choice_1 = max(dp[j+1] - (matrix[i][j] if row == more else matrix[j][i]), 1)
            choice_2 = max(dp[j] - (matrix[i][j] if row == more else matrix[j][i]), 1)
            dp[j] = min(choice_1, choice_2)

    return dp[0]


if __name__ == "__main__":
    n, m = [int(k) for k in sys.stdin.readline().split(" ")]
    test = []
    for temp in range(n):
        test_col = [int(k) for k in sys.stdin.readline().split(" ")]
        test.append(test_col)
    print(dynamic_programming(test))
