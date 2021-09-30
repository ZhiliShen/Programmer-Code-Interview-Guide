# -*- coding: utf-8 -*- # 
# @Time    : 2021-09-30 11:05
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test1.py
# @Notice  :
steps = 0


def hanoi(num: int, source, target, auxiliary):
    if num == 1:
        move(num, source, target)
    hanoi(num - 1, source, auxiliary, target)
    move(num, source, target)
    hanoi(num - 1, auxiliary, target, source)


def move(num: int, source, target):
    print("Move {:d} from {} to {}".format(num, source, target))
    global steps
    steps += 1


def hanoi_new(num: int, source, target, auxiliary):
    if num == 1:
        move(num, source, auxiliary)
        move(num, auxiliary, target)  # 哪怕只剩一个也要按照规则来
        return  # 写递归要写return！
    hanoi_new(num - 1, source, target, auxiliary)
    move(num, source, auxiliary)
    hanoi_new(num - 1, target, source, auxiliary)
    move(num, auxiliary, target)
    hanoi_new(num - 1, source, target, auxiliary)


if __name__ == "__main__":
    n = int(input())
    hanoi_new(n, 'left', 'right', 'mid')
    print("It will move {:d} steps.".format(steps))
