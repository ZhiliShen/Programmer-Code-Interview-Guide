# -*- coding: utf-8 -*- # 
# @Time    : 2021-10-19 16:13
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
from collections import deque


def get_value(chars: str):
    return value(chars, 0)[0]


def value(chars: str, index: int):
    num = 0
    queue = deque()
    while index < len(chars) and chars[index] != ')':
        cur = chars[index]
        if '0' <= cur <= '9':
            num = num * 10 + (ord(cur) - ord('0'))
            index += 1  # while循环一定要对标志量进行变动
        elif cur != '(':
            add_num(queue, num)  # 如果上一个压栈的是乘法或者除法运算符 则需要取出上一个运算数重新计算后 将数字压栈
            queue.append(cur)  # 将运算符压栈
            index += 1
            num = 0
        else:  # 如果遇到左括号则开始进行新一轮子运算
            num, index = value(chars, index + 1)
    add_num(queue, num)  # 循环结束后一定是一个数结尾的 不要忘记将这个数压栈
    result = get_num(queue)  # 最后得到相应的结果返回
    return result, index + 1


def add_num(queue: deque, num: int):
    if len(queue) != 0:
        cur = queue.pop()
        if cur == '+' or cur == '-':
            queue.append(cur)
        else:
            pre_num = queue.pop()
            # num = (num * pre_num if cur == '*' else pre_num // num)  # 这里是我一开始的选择 除法选择进行地板除 进而保证队列中的都是整数
            pre_num = int(pre_num)  # 这里则是先转为整型
            num = (num * pre_num if cur == '*' else pre_num / num)  # 队列里面可能会有小数 地板除返回不大于结果的一个最大整数 而int是截取数字的整数部分 所以int(-1/3)与-1//3的结果分别为0和-1
    queue.append(num)  # 如果一开始栈中没有任何元素 需要直接压栈 这点上次忘写了


def get_num(queue: deque):  # 此时栈中只有加减法 因此直接从左向右计算即可
    result = 0
    add = True
    while len(queue) != 0:
        cur = queue.popleft()
        if cur == '+':
            add = True
        elif cur == '-':
            add = False
        else:
            # result += (cur if add else -cur)
            result += (int(cur) if add else int(-cur))

    return result


if __name__ == "__main__":
    test = input()
    print(get_value(test))
