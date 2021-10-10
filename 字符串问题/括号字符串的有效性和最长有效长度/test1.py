# -*- coding: utf-8 -*- # 
# @Time    : 2021-10-10 22:03
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test1.py
# @Notice  :
from collections import deque


def validate(cur: str):
    stack = deque()
    for temp in cur:
        if temp == '(':
            stack.append('(')
        elif temp == ')':
            if len(stack) == 0:
                return 'NO'
            elif stack[0] == ')':
                return 'NO'
            else:
                stack.pop()
    if len(stack) == 0:
        return 'YES'
    else:
        return 'NO'


def validate_2(cur: str):
    status = 0
    for temp in cur:
        if temp != '(' and temp != ')':
            return 'NO'
        elif temp == ')':
            status -= 1
            if status < 0:
                return 'NO'
        else:
            status += 1

    return 'YES' if status == 0 else 'NO'


if __name__ == "__main__":
    test = input()
    print(validate_2(test))
