# -*- coding: utf-8 -*- # 
# @Time    : 2021-11-27 15:25
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test2.py
# @Notice  :


# N!=1x2x3x...xN的二进制表达式中最低位的位置 -> N!=1x2x3x...xN的二进制表达式的末尾有多少0 -> 1~N中每有一个2 非0数字就会向左移动
# 1~N中有多少因子2
def right_one(num: int):
    if num < 0:
        return -1  # 这里需要返回-1
    res = 0
    while num != 0:  # 首先是算有多少个N/5 再计算有多少个N/25 再计算有多少个N/125 以此类推
        num >>= 1
        res += num
    return res


# 记N!中因子2的个数为a N的二进制表达式中1的个数为b 则a=N-b
# 即N/2+N/4+N/8+...=N-b
# 若N的二进制表达式有b个1 -> N=k1+k2+...+kb 其中ki均为2的某次方 例如 N=10110 则k1=10000 k2=100 k3=10
# 则(k1+k2+...+kb)/2+(k1+k2+...+kb)/4+(k1+k2+...+kb)/8+...=(k1/2+k1/4+k1/8+...)+(k2/2+k2/4+k2/8+...)+(kb/2+kb/4+kb/8+...)
# 利用等比数列求和公式 和=(末项*公比-首项)/(公比-1) 得(1*1/2-ki/2)/(1/2-1)=ki-1
# 则(k1/2+k1/4+k1/8+...)+(k2/2+k2/4+k2/8+...)+(kb/2+kb/4+kb/8+...)=k1-1+k2-1+...+kb-1=(k1+k2+...+kb)-b=N-b
# 故得证
def right_one_1(num: int):
    if num < 0:
        return -1
    ones = 0  # N的二进制表达式中1的个数
    cur_num = num
    while cur_num != 0:
        if cur_num & 1 != 0:
            ones += 1
        cur_num >>= 1
    return num-ones


if __name__ == "__main__":
    a = int(input())
    print(right_one(a))
