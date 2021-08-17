# -*- coding: utf-8 -*- #
# @Time    : 2021/8/7 0:22
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test2.py
# @Notice  :
import sys


class ReturnType:
    def __init__(self, with_max, without_max):
        self.with_max = with_max
        self.without_max = without_max


def process(x: int):
    if len(subordinate_list[x]) == 0:
        return ReturnType(happy_list[x], 0)
    with_x_max = happy_list[x]
    without_x_max = 0
    for employee in subordinate_list[x]:
        employee_info = process(employee)
        with_employee_max, without_employee_max = employee_info.with_max, employee_info.without_max
        with_x_max += without_employee_max
        without_x_max += max(with_employee_max, without_employee_max)
    return ReturnType(with_x_max, without_x_max)


def generate_max_happy(boss: int):
    boss_info = process(boss)
    return max(boss_info.with_max, boss_info.without_max)


if __name__ == "__main__":
    n, boss = map(int, sys.stdin.readline().split())
    happy_list = [0] + list(map(int, sys.stdin.readline().split()))
    subordinate_list = [[] for i in range(n+1)]
    for i in range(n-1):
        u, v = map(int, sys.stdin.readline().split())
        subordinate_list[u].append(v)
    print(generate_max_happy(boss))
