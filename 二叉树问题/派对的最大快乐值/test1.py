# -*- coding: utf-8 -*- #
# @Time    : 2021/8/6 16:48
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test1.py
# @Notice  :
import sys
from typing import List


class Employee:
    def __init__(self, happy, subordinates: List):
        self.happy = happy
        self.subordinates = subordinates


class ReturnType:
    def __init__(self, with_max, without_max):
        self.with_max = with_max
        self.without_max = without_max


def process(x: Employee):
    if len(x.subordinates) == 0:
        return ReturnType(x.happy, 0)
    with_x_max = x.happy
    without_x_max = 0
    for employee in x.subordinates:
        employee_info = process(employee)
        with_employee_max, without_employee_max = employee_info.with_max, employee_info.without_max
        with_x_max += without_employee_max
        without_x_max += max(with_employee_max, without_employee_max)
    return ReturnType(with_x_max, without_x_max)


def generate_max_happy(boss: Employee):
    boss_info = process(boss)
    return max(boss_info.with_max, boss_info.without_max)


if __name__ == "__main__":
    n, root = [int(k) for k in sys.stdin.readline().split(" ")]
    id2employee = {i: Employee(0, []) for i in range(n+1)}
    for idx, happy in enumerate([int(happy) for happy in sys.stdin.readline().split(" ")]):
        id2employee[idx+1].happy = happy
    for idx, line in enumerate(sys.stdin):
        employee_id, subordinate_id = [int(k) for k in line.split()]
        id2employee[employee_id].subordinates.append(id2employee[subordinate_id])
        if idx == n-1:
            break
    print(generate_max_happy(id2employee[root]))
