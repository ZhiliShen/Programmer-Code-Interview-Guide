# -*- coding: utf-8 -*- # 
# @Time    : 2021-12-04 17:02
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :

def one_appear_num(num: int):
    if num < 1:
        return 0
    count = 0
    for i in range(1, num + 1):
        count += get_one_num(i)
    return count


def get_one_num(num: int):
    res = 0
    while num != 0:
        if num % 10 == 1:
            res += 1
        num //= 10
    return res


# 114是关注14+1~114 21345是关注于1345+1~21345
# 在上述关注的区间内
# 如果最高位的数字等于1 则所有最高位上出现1的次数是除去最高位后剩下的数+1 例如114去掉1得到14 即14+1=15
# 如果最高位的数字大于1 则所有最高位上出现1的次数是10^(位数-1） 例如21345位数为5 则10000
# 在上述所关注的区间中 除去最高位 剩余的某一位固定为1 则其余为可以从0~9自由变换 而最高位则提供了可以变化的次数 例如1346~11345可以变换1次 11346~21345可以再变化一次
# 所以计算公式即（最高位的数字）x(除去最高位后剩下的位数)x（10^某一位固定的情况下可以变化的位数）
# 关注区间之外的数字可以按照上述步骤继续处理
def one_appear_num_1(num: int):
    if num < 1:
        return 0
    num_len = get_len_of_num(num)  # 如果数字为1~9 则直接返回1
    if num_len == 1:
        return 1
    cur = pow(10, num_len-1)
    highest = num // cur
    if highest == 1:
        highest_one_appear_num = num % cur + 1
    else:
        highest_one_appear_num = cur
    other_one_appear_num = highest * (num_len-1) * cur // 10
    return highest_one_appear_num + other_one_appear_num + one_appear_num_1(num % cur)


def get_len_of_num(num: int):
    num_len = 0
    while num != 0:
        num_len += 1
        num //= 10
    return num_len


if __name__ == "__main__":
    print(one_appear_num_1(11))
