# -*- coding: utf-8 -*- # 
# @Time    : 2021-09-29 17:47
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
mod_num = 1000000007


def validate(string: str):
    if len(string) & 1 == 0:
        return False
    for temp in string[::2]:
        if temp not in ('1', '0'):
            return False
    for temp in string[1::2]:
        if temp not in ('&', '|', '^'):
            return False

    return True


def recur(string: str, left: int, right: int, desired: bool):
    if left == right:
        if bool(string[left]) == desired:
            return 1
        else:
            return 0
    results = 0
    for index in range(left+1, right, 2):
        if string[index] == '&':
            if desired:
                results += recur(string, left, index - 1, True) * recur(string, index + 1, right, True)
            else:
                results += recur(string, left, index - 1, False) * recur(string, index + 1, right, False)
                results += recur(string, left, index - 1, False) * recur(string, index + 1, right, True)
                results += recur(string, left, index - 1, True) * recur(string, index + 1, right, False)
        if string[index] == '|':
            if not desired:
                results += recur(string, left, index - 1, False) * recur(string, index + 1, right, False)
            else:
                results += recur(string, left, index - 1, True) * recur(string, index + 1, right, True)
                results += recur(string, left, index - 1, False) * recur(string, index + 1, right, True)
                results += recur(string, left, index - 1, True) * recur(string, index + 1, right, False)
        if string[index] == '^':
            if not desired:
                results += recur(string, left, index - 1, False) * recur(string, index + 1, right, False)
                results += recur(string, left, index - 1, True) * recur(string, index + 1, right, True)
            else:
                results += recur(string, left, index - 1, False) * recur(string, index + 1, right, True)
                results += recur(string, left, index - 1, True) * recur(string, index + 1, right, False)

    return results


def recur_top(string: str, desired: bool):
    length = len(string)
    if length == 0 or not validate(string):
        return 0
    return recur(string, 0, length - 1, desired)


def dynamic_programming(string: str, desired: bool):
    length = len(string)
    if length == 0 or not validate(string):
        return 0

    t = [[0 for j in range(length)] for i in range(length)]
    f = [[0 for j in range(length)] for i in range(length)]

    # base case
    for i in range(0, length, 2):
        if string[i] != '0':  # bool('0')等于1！！！
            t[i][i], f[i][i] = 1, 0
        else:
            t[i][i], f[i][i] = 0, 1

    # transfer equation
    for i in range(length-1, -1, -2):
        for j in range(i+2, length, 2):
            for k in range(i+1, j, 2):  # 记得写range!
                if string[k] == '&':
                    t[i][j] += t[i][k-1]*t[k+1][j] % mod_num
                    f[i][j] += (f[i][k-1]*f[k+1][j] + t[i][k-1]*f[k+1][j] + f[i][k-1]*t[k+1][j]) % mod_num
                elif string[k] == '|':
                    t[i][j] += (t[i][k-1]*t[k+1][j] + t[i][k-1]*f[k+1][j] + f[i][k-1]*t[k+1][j]) % mod_num
                    f[i][j] += f[i][k-1]*f[k+1][j]
                elif string[k] == '^':
                    t[i][j] += (t[i][k-1]*f[k+1][j] + f[i][k-1]*t[k+1][j]) % mod_num
                    f[i][j] += (t[i][k-1]*t[k+1][j] + f[i][k-1]*f[k+1][j]) % mod_num
                t[i][j] %= mod_num  # 因为累加后的值可能超过阈值
                f[i][j] %= mod_num
    return t[0][length-1] if desired else f[0][length-1]


if __name__ == "__main__":
    test = input()
    if input() == 'false':
        target = False
    else:
        target = True
    print(dynamic_programming(test, target))
