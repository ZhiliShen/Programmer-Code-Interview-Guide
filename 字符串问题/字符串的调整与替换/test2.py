# -*- coding: utf-8 -*- # 
# @Time    : 2021-10-12 21:29
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test2.py
# @Notice  :
def modify(string: str):
    if len(string) == 0:
        return

    new_str = [''] * len(string)
    index = len(string) - 1

    for temp in string[::-1]:
        if temp != '*':
            new_str[index] = temp
            index -= 1

    new_str[:index + 1] = ['*'] * (index + 1)

    return ''.join(new_str)


if __name__ == "__main__":
    test = input()
    print(modify(test))
