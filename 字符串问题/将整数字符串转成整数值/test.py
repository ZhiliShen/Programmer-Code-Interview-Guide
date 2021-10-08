# -*- coding: utf-8 -*- #
# @Time    : 2021-10-08 20:06
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
def validate_str(cur: str):
    if cur[0] != '-' and (cur[0] < '0' or cur[0] > '9'):  # 将多种情况转换为范围问题
        return False
    if cur[0] == '-' and (cur[1] == '0' or len(cur) == 1):
        return False
    if cur[0] == '0' and len(cur) > 1:
        return False
    for temp in cur[1:]:  # 首位已经被检查过了 所以无需再次检查
        if temp < '0' or temp > '9':
            return False

    return True


def str2num(cur: str):
    if not validate_str(cur):
        return 0
    min_q = -(pow(2, 31) // 10)
    min_r = -(pow(2, 31) % 10)  # 负号写在括号外面
    res = 0
    if cur[0] == '-':
        positive = False
        cur = cur[1:]
    else:
        positive = True
    for temp in cur:
        cur_num = ord('0') - ord(temp)
        if res < min_q or (res == min_q and cur_num < min_r):
            return 0
        res = res * 10 + cur_num
    if positive and res == -pow(2, 31):
        return 0
    else:
        return res if not positive else -res


if __name__ == "__main__":
    test = input()
    print(str2num(test))
