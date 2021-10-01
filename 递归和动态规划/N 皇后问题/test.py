# -*- coding: utf-8 -*- #
# @Time    : 2021-09-30 17:56
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
from typing import List


def auxiliary(index: int, record: List[int], n: int):
    if index == n:
        return 1
    result = 0
    for i in range(n):
        if validate(i, record, index, n):
            record[index] = i
            result += auxiliary(index + 1, record, n)

    return result


def validate(num: int, record: List[int], index: int, n: int):
    for exist_index in range(index):
        if record[exist_index] == num or abs(exist_index - index) == abs(record[exist_index] - num):
            return False

    return True


def n_queens(col_available, col, left_dia, right_dia):
    if col == col_available:  # col_available如果是11111则代表棋盘可以放置的列的为0~5
        return 1
    pos = col_available & (~(col | left_dia | right_dia))   # col_available如果是11111则代表当前棋盘可以放置的列
    result = 0
    while pos != 0:
        most_right_one = pos & (~pos + 1)  # 正数的反码+1 则可以将除了最右边的1保留外 其余位置取反 例如010100->101011->101100 若再将正数与其进行且运算 则可以只保留最右边的1
        pos = pos - most_right_one  # 将pos减去最右边的1 则将最右边的1清零 则表明该位置不能再使用
        result += n_queens(col_available, col | most_right_one, (left_dia | most_right_one) << 1,
                           (right_dia | most_right_one) >> 1)

    return result


if __name__ == "__main__":
    n = int(input())
    test = [0 for i in range(n)]
    print(n_queens(pow(2, n) - 1, 0, 0, 0))
    print(auxiliary(0, test, n))
