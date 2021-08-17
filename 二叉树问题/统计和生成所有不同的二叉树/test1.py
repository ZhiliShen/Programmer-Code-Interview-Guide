# -*- coding: utf-8 -*- #
# @Time    : 2021/8/8 16:56
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test1.py
# @Notice  :
import sys


def num_trees_with_recur(n: int):
    if n <= 1:
        return 1
    n_num_trees = 0
    for i in range(n):
        n_num_trees += (num_trees_with_recur(i) * num_trees_with_recur(n - i - 1))
    return n_num_trees


def num_trees_with_dp(n: int):
    if n <= 1:
        return 1
    num = [0 for i in range(n + 1)]
    num[0] = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            num[i] += (num[j - 1] * num[i - j])
    return num[n]


def num_trees_with_catalan(n: int):
    if n <= 1:
        return 1
    n_num_trees = 1
    inverse_element = [1 for i in range(n + 2)]
    # f(n)=f(n-1)*(4n-2)/(n+1) f(n)%mod=f(n-1)*(4n-2)/(n+1)%mod=(f(n-1)%mod*(4n-2)*inverse_element(n+1)%mod)%mod
    # f(n)=f(n-1)*((4n-2)*inverse_element(n+1)%mod)%mod
    for i in range(2, len(inverse_element)):
        inverse_element[i] = (mod - mod // i) * inverse_element[mod % i] % mod
    for i in range(2, n + 1):
        n_num_trees = n_num_trees * ((4 * i - 2) * inverse_element[i + 1] % mod) % mod
    return n_num_trees


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    mod = 1000000007
    print(num_trees_with_catalan(n))
