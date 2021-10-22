# -*- coding: utf-8 -*- # 
# @Time    : 2021-10-22 15:03
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
def is_match(a_str: str, b_str: str):
    result = False
    if a_str is None or b_str is None:
        return result
    if is_valid(a_str, b_str):
        result = process(a_str, b_str, 0, 0)

    return 'YES' if result else 'NO'


def process(a_str: str, b_str: str, a_index: int, b_index: int):
    if b_index == len(b_str):  # 如果exp没有字符了 除非str也没有字符 否则返回False 因为空无法匹配有
        if a_index == len(a_str):
            return True
        else:
            return False
    # 如果exp只剩一个字符了 或者 exp的下一个字符不是* 就需要老老实实匹配
    if b_index == len(b_str) - 1 or b_str[b_index + 1] != '*':
        # 在使用index访问数组的时候 需要确保index是属于合法范围内的 eg: abc acd 的前两个a相匹配 因此整体是否匹配还需要看后面的也就是[a_str+1, a_len]与[b_str+1, b_len]
        return a_index < len(a_str) and (b_str[b_index] == a_str[a_index] or b_str[b_index] == '.') and process(a_str,
                                                                                                                b_str,
                                                                                                                a_index+1,
                                                                                                                b_index+1)
    else:
        # *是允许其前面的字符不存在的 所以bXXX a*YYY 虽然a与b不匹配 但由于*的存在 如果bXXX与YYY相匹配也是可以的
        # 而*允许多个字符的存在也为字符串相匹配提供了很多可能性
        # aaaXXX a*YYY 其中YYY只要与aaaXXX aaXXX aXXX XXX其中一个匹配即可
        # 而我们可以将两者的流程结合起来形成下面的代码
        while a_index < len(a_str) and (b_str[b_index] == a_str[a_index] or b_str[b_index] == '.'):
            if process(a_str, b_str, a_index, b_index+2):
                return True
            a_index += 1

        return process(a_str, b_str, a_index, b_index+2)


def is_valid(a_str: str, b_str: str):
    for char in a_str:
        if char == '.' or char == '*':
            return False

    for index, char in enumerate(b_str):
        if char == '*' and (index == 0 or b_str[index - 1] == '*'):  # 挺巧妙的处理 检查上一个字符 而非下一个字符
            return False

    return True


def is_match_map_dp(a_str, b_str):
    result = False
    if a_str is None or b_str is None:
        return result
    a_len, b_len = len(a_str), len(b_str)
    dp = [[False for j in range(b_len+1)] for i in range(a_len+1)]

    # base case
    dp[a_len][b_len] = True  # 空字符串是能匹配空的字符串的 所以设置为真
    # 很好玩的是a*b*c* 是能匹配空字符串的 但是一定要严格按照X*的模式进行重复 所以可以从右向左依次检验 一旦不符合则左边的全部为假 所以初始化为假的好处在于后续不用再继续处理
    for i in range(b_len-2, 0, -2):
        if b_str[i] != '*' and b_str[i+1] == '*':
            dp[a_len][i] = True
        else:
            break

    if a_len > 0 and b_len > 0:
        # dp的倒数第二列是str的以最后一个字符结尾的子串是否和exp的最后一个字符是否匹配 唯一一个需要考虑的是str的最后一个字符 因为只有这个才可能匹配
        if b_str[b_len-1] == '.' or a_str[a_len-1] == b_str[b_len-1]:
            dp[a_len-1][b_len-1] = True

    # transfer equation
    # 动态规划一定需要先考虑转移方程 而转移方程中的依赖决定了遍历方向 进而决定我们需要对哪些位置进行初始化
    for i in range(a_len-1, -1, -1):
        for j in range(b_len-2, -1, -1):
            if b_str[j+1] != '*':
                dp[i][j] = (a_str[i] == b_str[j] or b_str[j] == '.') and dp[i+1][j+1]
            else:
                index = i
                while index < a_len and (a_str[index] == b_str[j] or b_str[j] == '.'):  # 在使用index访问数组的时候 需要确保index是属于合法范围内的
                    if dp[index][j+2]:
                        dp[i][j] = True
                        break
                    index += 1
                if not dp[i][j]:
                    dp[i][j] = dp[index][j+2]

    return 'YES' if dp[0][0] else 'NO'


if __name__ == "__main__":
    a = input()
    b = input()
    print(is_match_map_dp(a, b))
