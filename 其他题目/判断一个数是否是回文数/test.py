# -*- coding: utf-8 -*- # 
# @Time    : 2021-12-05 15:46
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :


def is_palindrome(num: int):
    num = abs(num)
    temp = 1
    # 先将temp的调整为10^(num的位数-1)
    while num // temp >= 10:  # 这里不选择while temp*10 <= num 是为了避免在其他语言中溢出
        temp *= 10
    while num != 0:
        if num // temp != num % 10:
            return False
        num = (num % temp) // 10
        temp //= 100  # 这里不要忘记将temp的位数始终与num保持一致
    return True


if __name__ == "__main__":
    num = int(input())
    print('Yes' if is_palindrome(num) else 'No')
