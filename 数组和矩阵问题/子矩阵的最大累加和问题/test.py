# -*- coding: utf-8 -*- # 
# @Time    : 2021-11-11 16:52
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
from typing import List


def max_sum(matrix: List[List[int]]):
    row, col = len(matrix), len(matrix[0])
    res = -float("inf")
    for i in range(row):
        dp = [0 for _ in range(col)]
        for j in range(i, row):
            for k in range(len(dp)):
                dp[k] += matrix[j][k]
            cur = 0
            for num in dp:
                if cur < 0:
                    cur = 0
                cur = cur + num
                res = max(res, cur)

    return res


if __name__ == "__main__":
    a, b = map(int, input().split())
    test = []
    for _ in range(a):
        test.append(list(map(int, input().split())))
    print(max_sum(test))
