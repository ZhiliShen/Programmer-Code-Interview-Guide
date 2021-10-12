# -*- coding: utf-8 -*- # 
# @Time    : 2021-10-12 20:14
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test1.py
# @Notice  :
def get_count_string(string: str):
    if len(string) == 0:
        return ""
    res = string[0]
    num = 0
    for cur in string:
        if cur == res[-1]:
            num += 1
        else:
            res = res + '_' + str(num) + '_' + cur
            num = 1
    res = res + '_' + str(num)

    return res


if __name__ == "__main__":
    test = input()
    print(get_count_string(test))
