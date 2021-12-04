# -*- coding: utf-8 -*- # 
# @Time    : 2021-12-04 15:34
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :


# 先从低到高看num需要使用多少位
# 再从高到低看每个位上的值最多是多少
def get_string(bases: str, num: int):
    cur = 1
    base_num = len(bases)  # 基数
    need_lens = 0  # 表示num所需要使用到的位数
    while num >= cur:
        need_lens += 1
        num -= cur
        cur *= base_num
    res = []
    index = 0
    while True:
        cur //= base_num  # 注意这里要还原
        cur_num = num // cur  # 当前位置上最多能用cur_num个cur
        res.append(bases[cur_num])
        num %= cur
        index += 1
        if index == need_lens:
            break
    return ''.join(res)


def get_num(bases: str, chars: str):
    base_num = len(bases)
    cur = 1
    res = 0
    for i in range(len(chars)-1, -1, -1):
        res += (bases.index(chars[i])+1)*cur
        cur *= base_num
    return res


if __name__ == "__main__":
    a, b = map(int, input().split())
    c = input()
    if a == 1:
        d = int(input())
        print(get_string(c, d))
    else:
        e = input()
        print(get_num(c, e))
