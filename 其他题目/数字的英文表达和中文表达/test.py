# -*- coding: utf-8 -*- # 
# @Time    : 2021-12-07 21:46
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :


def num1to19(num: int):
    if num < 1 or num > 19:
        return ""
    one2nineteen = ["One ", "Two ", "Three ", "Four ", "Five ", "Six ", "Seven ", "Eight ", "Nine ", "Ten ",
                    "Eleven ", "Twelve ", "Thirteen ", "Fourteen ", "Fifteen ", "Sixteen ", "Seventeen ", "Eighteen ",
                    "Nineteen "]
    return one2nineteen[num - 1]


def num1to99_english(num: int):
    if num < 1 or num > 99:
        return ""
    if num < 20:
        return num1to19(num)
    high = num // 10
    twenty2ninety = ["Twenty ", "Thirty ", "Forty ", "Fifty ", "Sixty ", "Seventy ", "Eighty ", "Ninety "]
    return twenty2ninety[high - 2] + num1to19(num % 10)


def num1to999_english(num: int):
    if num < 1 or num > 999:
        return ""
    if num < 100:
        return num1to99_english(num)
    high = num // 100
    return num1to99_english(high) + "Hundred " + num1to99_english(num % 100)


def get_num_eng_exp(num: int):
    if num == 0:
        return "Zero"
    res = ""
    if num < 0:
        res += "Negative, "
    num = abs(num)
    high = 1000000000
    high_index = 0
    billion2thousand = ["Billion", "Million", "Thousand", ""]
    while num != 0:
        cur = num // high
        num %= high
        if cur != 0:
            res += num1to999_english(cur)
            res += billion2thousand[high_index] + (" " if num == 0 else ", ")
        high //= 1000
        high_index += 1
    return res


def num1to9(num: int):
    if num < 1 or num > 9:
        return ""
    one2nine = ["一", "二", "三", "四", "五", "六", "七", "八", "九"]
    return one2nine[num - 1]


def num1to99_chinese(num: int, has_hundred: bool):
    if num < 1 or num > 99:
        return ""
    if num < 10:
        return num1to9(num)
    high = num // 10
    if high == 1 and (not has_hundred):
        return "十" + num1to9(num % 10)
    else:
        return num1to9(high) + "十" + num1to9(num % 10)


def num1to999_chinese(num: int):
    if num < 1 or num > 999:
        return ""
    if num < 100:
        return num1to99_chinese(num, False)
    res = num1to9(num // 100) + "百"
    rest = num % 100
    if rest == 0:
        return res
    elif rest >= 10:
        res += num1to99_chinese(rest, True)
    else:
        res += "零" + num1to9(rest)
    return res


def num1to9999(num: int):
    if num < 1 or num > 9999:
        return ""
    if num < 1000:
        return num1to999_chinese(num)
    res = num1to9(num // 1000) + "千"
    rest = num % 1000
    if rest == 0:
        return res
    elif rest >= 100:
        res += num1to999_chinese(rest)
    else:
        res += "零" + num1to99_chinese(rest, False)
    return res


def num1to99999999(num: int):
    if num < 1 or num > 99999999:
        return ""
    high = num // 10000
    rest = num % 10000
    if high == 0:
        return num1to9999(rest)
    res = num1to9999(high) + "万"
    if rest == 0:
        return res
    else:
        if rest < 1000:
            return res + "零" + num1to999_chinese(rest)
        else:
            return res + num1to9999(rest)


def get_num_chi_exp(num: int):
    if num == "0":
        return "零"
    res = ""
    if num < 0:
        res += "负"
    num = abs(num)
    high = num // 100000000
    rest = num % 100000000
    if high == 0:
        return res + num1to99999999(rest)
    res += num1to9999(high) + "亿"
    if rest == 0:
        return res
    else:
        if rest < 10000000:
            return res + "零" + num1to99999999(rest)
        else:
            return res + num1to99999999(rest)


if __name__ == "__main__":
    a = int(input())
    print(get_num_eng_exp(a))
    print(get_num_chi_exp(a))
