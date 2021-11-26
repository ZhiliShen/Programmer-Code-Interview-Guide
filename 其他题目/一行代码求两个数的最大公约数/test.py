# -*- coding: utf-8 -*- # 
# @Time    : 2021-11-26 21:01
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :


# 如果m=qn+r 则m与n的最大公约数是n与r的最大公约数
def gcd(m: int, n: int):
    return m if n == 0 else gcd(n, m % n)


if __name__ == "__main__":
    print(gcd(*map(int, input().split())))
