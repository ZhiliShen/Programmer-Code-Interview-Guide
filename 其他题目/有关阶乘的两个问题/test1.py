# -*- coding: utf-8 -*- # 
# @Time    : 2021-11-27 14:41
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test1.py
# @Notice  :


# N!=1x2x3x...xN的末尾有多少0 -> 1~N中每有一组2x5最低位的非0数字就会向左移动 因为2与5是质数 所以选择2与5
# 又因为因子2的数目多余因子5的数目 -> 1~N中有多少因子5
def zero_num(num: int):
    if num < 0:
        return 0
    res = 0
    for index in range(5, num + 1, 5):
        cur = index  # 不要在循环中对循环标识符进行操作
        while cur % 5 == 0:
            res += 1
            cur //= 5
    return res


# 1~N中有N/5个数能够贡献1个5 有N/25个数能够贡献2个5 有N/125个数能够贡献3个5 以此类推
def zero_num_1(num: int):
    if num < 0:
        return 0
    res = 0
    while num != 0:  # 首先是算有多少个N/5 再计算有多少个N/25 再计算有多少个N/125 以此类推
        res += num // 5
        num //= 5
    return res


if __name__ == "__main__":
    a = int(input())
    print(zero_num_1(a))
