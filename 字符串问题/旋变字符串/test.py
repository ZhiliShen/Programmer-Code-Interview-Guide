# -*- coding: utf-8 -*- # 
# @Time    : 2021-10-26 09:08
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
def is_scramble_1(a_str: str, b_str: str):
    if (a_str is None and b_str is not None) or (a_str is not None and b_str is None):
        return 'NO'
    if a_str is None and b_str is None:
        return 'YES'
    if a_str == b_str:
        return 'YES'
    if not valid(a_str, b_str):
        return 'NO'
    a_len = len(a_str)
    return 'YES' if process_1(a_str, b_str, 0, 0, a_len) else 'NO'
    # process2()这个方法是错的 因为其没有考虑到b的组成部分均是a的组成部分的旋变字符串 因此根本无法进入for循环
    # return 'YES' if process_2(a_str, b_str, False) else 'NO'


def process_1(a_str: str, b_str: str, a_start: int, b_start: int, size: int):
    if size == 1:
        if a_str[a_start] == b_str[b_start]:
            return True
        else:
            return False
    if a_str[a_start:a_start + size] == b_str[b_start: b_start + size]:
        return True
    for left_part in range(1, size):
        # a[0:i]与b[0:i]互为旋变词 a[i:]与b[i:]互为旋变词 a[0:i]与b[-i:0]互为旋变词 a[i:]与b[:-i]互为旋变词
        if (process_1(a_str, b_str, a_start, b_start, left_part) and process_1(a_str, b_str, a_start + left_part,
                                                                               b_start + left_part,
                                                                               size - left_part)) or (
                process_1(a_str, b_str, a_start, b_start + size - left_part, left_part) and process_1(a_str, b_str,
                                                                                                      a_start + left_part,
                                                                                                      b_start,
                                                                                                      size - left_part)):
            return True
    return False


def process_2(a_str: str, b_str: str, flag: bool):
    a_len = len(a_str)
    if a_str == b_str:
        return True
    for i in range(1, a_len):
        if a_str[:i] == b_str[:i]:
            flag = flag or process_2(a_str[i:], b[i:], flag)
        elif a_str[:i] == b_str[-i:]:  # b[-i:]代表从后面截取i个字符
            flag = flag or process_2(a_str[i:], b_str[:-i], flag)
    return flag


def valid(a_str: str, b_str: str):
    a_len, b_len = len(a_str), len(b_str)
    if a_len != b_len:
        return False
    str2num = [0 for _ in range(256)]
    for char in a_str:
        str2num[ord(char)] += 1
    for char in b_str:  # 不用考虑有的字符串少了 因为在长度固定的情况下有多必有少
        str2num[ord(char)] -= 1
        if str2num[ord(char)] < 0:
            return False
    return True


def is_scramble_2(a_str: str, b_str: str):
    if (a_str is None and b_str is not None) or (a_str is not None and b_str is None):
        return 'NO'
    if a_str is None and b_str is None:
        return 'YES'
    if a_str == b_str:
        return 'YES'
    if not valid(a_str, b_str):
        return 'NO'
    a_len, b_len = len(a_str), len(b_str)
    dp = [[[False for _ in range(a_len+1)] for _ in range(b_len)] for _ in range(a_len)]  # 数组越外面的索引 越要声明在里面

    # base case
    for i in range(a_len):
        for j in range(b_len):
            if a_str[i] == b_str[j]:
                dp[i][j][1] = True

    # transfer equation
    # 三维dp 但好在每个位置的值只依赖于下一层的值 与本层的值无关
    for size in range(2, a_len+1):
        for i in range(a_len-size+1):  # 这里要写a_len-size+1 而不是a_len-size
            for j in range(b_len-size+1):
                for left_part in range(1, size):
                    if (dp[i][j][left_part] and dp[i+left_part][j+left_part][size-left_part]) or (dp[i][j+size-left_part][left_part] and dp[i+left_part][j][size-left_part]):
                        dp[i][j][size] = True
                        break

    return 'YES' if dp[0][0][a_len] else 'NO'


if __name__ == "__main__":
    a = input()
    b = input()
    print(is_scramble_2(a, b))
