# -*- coding: utf-8 -*- # 
# @Time    : 2021-12-13 15:43
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :

# 在python中优先级的顺序为取反 加减 位移 按位与 按位异或 按位或
# 加法的概念即a+b=a^b+(a&b)<<1
# python中的位移运算符和java是不一样的
# 因为python中的整数是不存在位数限制的 所以无论是左移运算符还是右移运算符都是保留符号位的
# 例如01000000000000000000000000000000(共32位)在python和java中都是1073741824
# 但是当左移一位时 python会保留符号位 变为010000000000000000000000000000000(共33位) 此时符号位没有发生变化 仍然是正数2147483648
# 而java则发生了溢出现象 变为10000000000000000000000000000000(共32位) 此时符号位发生了变化 变为负数-2147483648
# 所以在add函数中b_num中的1会永远陪着它 永远无法因为溢出而消失 永远无法变为0
def add(a_num: int, b_num: int):
    res = a_num
    while b_num != 0:  # 当不发生进位的时候 则是加法完成的时候
        res = a_num ^ b_num  # 异或运算本身记录的就是不含进位的加法
        b_num = ((a_num & b_num) << 1)  # 且运算向左移动1位 则记录了相应的发生进位的位置
        a_num = res
    return res


def neg(num: int):
    return add(~num, 1)  # 获取num的负数则是取反+1


def minus(a_num: int, b_num: int):
    if a_num < b_num:
        return add(a_num, neg(b_num))
    elif a_num > b_num:
        return neg(add(b_num, neg(a_num)))
    else:
        return 0


# axb=ax(2^0)xb0+ax(2^1)xb1+...+ax(2^31)xb31 所以每一轮我们只需要关注b当前最右边的位数是1还是0 -1073741744 1073741824
def multi(a_num: int, b_num: int):
    flag = True if a_num ^ b_num < 0 else False
    a_num = neg(a_num) if is_neg(a_num) else a_num
    b_num = neg(b_num) if is_neg(b_num) else b_num
    res = 0
    while b_num != 0:
        if b_num & 1 == 1:
            res = add(res, a_num)
        a_num <<= 1  # 获得a_num x (2^n)
        b_num >>= 1  # 获得b_num第n位上的数字
    return res if not flag else neg(res)


def is_neg(num: int):
    return num < 0


def div(a_num: int, b_num: int):
    if a_num == 0 and b_num != 0:
        return 0
    flag = True if a_num ^ b_num < 0 else False
    a_num = neg(a_num) if is_neg(a_num) else a_num
    b_num = neg(b_num) if is_neg(b_num) else b_num
    if a_num < b_num != 0:
        return 0
    res = 0
    while a_num >= b_num:
        temp = b_num
        count = 1
        while 0 < temp << 1 <= a_num:
            count <<= 1
            temp <<= 1
        res = add(res, count)
        a_num = minus(a_num, temp)
    return res if not flag else neg(res)


if __name__ == "__main__":
    a, b, c = input().split()
    if b == "+":
        if is_neg(int(a)) and not is_neg(int(c)):
            print(minus(int(c), neg(int(a))))
        elif not is_neg(int(a)) and is_neg(int(c)):
            print(minus(int(a), neg(int(c))))
        else:
            print(add(int(a), int(c)))
    if b == "-":
        print(minus(int(a), int(c)))
    if b == "*":
        print(multi(int(a), int(c)))
    if b == "\\":
        print(div(int(a), int(c)))
