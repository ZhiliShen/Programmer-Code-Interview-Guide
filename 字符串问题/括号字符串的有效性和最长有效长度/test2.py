# -*- coding: utf-8 -*- # 
# @Time    : 2021-10-10 22:03
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test2.py
# @Notice  :
def max_valid_len(cur: str):
    length = len(cur)
    dp = [0 for i in range(length)]
    res = 0

    # base case
    dp[0] = 0

    # transfer equation
    for i in range(1, length):
        if cur[i] == '(':  # 如果是左括号 则以其结尾的字符串必然不合法
            dp[i] = 0
        else:  # 如果是右括号 则看其向左跨越有效字符串后的字符是否为左括号 并要考虑是否能继续延长
            pre = i - dp[i - 1] - 1
            if cur[pre] == '(':
                dp[i] = dp[i - 1] + 2 + (dp[pre - 1] if pre - 1 >= 0 else 0)
                res = max(res, dp[i])
    return res


if __name__ == "__main__":
    test = input()
    print(max_valid_len(test))
