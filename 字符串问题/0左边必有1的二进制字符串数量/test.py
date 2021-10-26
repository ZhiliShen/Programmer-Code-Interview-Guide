# -*- coding: utf-8 -*- #
# @Time    : 2021-10-26 20:09
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
from typing import List


# process(i, num)代表的是[0,i-1]位置上的字符已经确定且符合要求 而且i-1位置上的字符是1的情况下 [i,N-1]上的位置还能产生多少种满足要求的字符串
# 在n=5的情况下 [0,3-1]可以是101 111 之后[3, 4]可以是01 11 10 所以process(3, 5)的值为3
# 那么process(1, num)的值则代表0位置上的字符是1 而且只能是1的情况下 [1,N-1]上的位置还能产生多少种满足要求的字符串 正是我们寻求的答案
# 如果i-1位置上的字符是1的情况下 i位置上的字符可以是1 在这种情况下[i,N-1]上的位置还能产生多少种满足要求的字符串就等于[i+1,N-1]上的位置还能产生多少种满足要求的字符串
# 如果i-1位置上的字符是1的情况下 i位置上的字符可以是0 但i+1上必须是1 在这种情况下[i,N-1]上的位置还能产生多少种满足要求的字符串就等于[i+2,N-1]上的位置还能产生多少种满足要求的字符串
# 所以我们就能归纳出process(num, num)=1 process(num-1, num)=2  process(i, num)= process(i+1, num)+process(i+2, num)
# 进一步观察发现其在num为1 2 3 4 5的情况下 答案分别为1 2 3 5 8 所以其也就是初始项为1 2的斐波那契数列、
# 代入初始项可以得出相应的状态矩阵为((1, 1), (1, 0))
# 之后使用快速幂可以进一步加速求解过程
def get_num_1(num: int):
    return process(1, num)  # 这里是1


def process(index: int, num: int):
    if num < 1:
        return 0
    if index == num:
        return 1
    if index == num - 1:
        return 2
    return process(index + 1, num) + process(index + 2, num)


def get_num_2(num: int):
    if num < 1:
        return 0
    if num == 1 or num == 2:
        return num
    pre, cur, tmp = 1, 2, 0
    for _ in range(3, num + 1):
        tmp = cur
        cur += pre
        pre = tmp
    return cur


def get_num_3(num: int):
    if num < 1:
        return 0
    if num == 1 or num == 2:
        return num
    base = [[1, 1], [1, 0]]
    res = matrix_power(base, num - 2)
    return 2 * res[0][0] + res[1][0]


def matrix_power(matrix: List[List[int]], pow_num: int):
    row_len, col_len = len(matrix), len(matrix[0])
    res = [[0 for _ in range(col_len)] for _ in range(row_len)]
    # 先把res初始化为单位矩阵 单位矩阵乘以其他矩阵等于其他矩阵
    for i in range(row_len):
        res[i][i] = 1
    tmp = matrix
    while pow_num != 0:
        if pow_num & 1 != 0:
            res = multi_matrix(res, tmp)
        tmp = multi_matrix(tmp, tmp)
        pow_num >>= 1
    return res


def multi_matrix(a_matrix: List[List[int]], b_matrix: List[List[int]]):
    res = [[0 for _ in range(len(b_matrix[0]))] for _ in range(len(a_matrix))]
    for i in range(len(a_matrix)):
        for j in range(len(b_matrix[0])):
            for k in range(len(a_matrix[0])):
                res[i][j] = (res[i][j] + a_matrix[i][k] * b_matrix[k][j]) % (2 ** 29)
    return res


if __name__ == "__main__":
    a = int(input())
    print(get_num_3(a) % (2 ** 29))
