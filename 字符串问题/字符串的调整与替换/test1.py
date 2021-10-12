# -*- coding: utf-8 -*- # 
# @Time    : 2021-10-12 21:17
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test1.py
# @Notice  :
def replace(string: str):
    length = len(string)
    if len(string) == 0:
        return

    char_num = 0

    for temp in string:
        if temp == ' ':
            char_num += 1

    new_length = length + 2 * char_num
    new_str = [''] * new_length
    index = new_length - 1
    for temp in string[::-1]:
        if temp != ' ':
            new_str[index] = temp  # str是不可变对象 不支持创建完毕后修改 所以需要使用list先创建后拼接
            index -= 1
        else:
            new_str[index - 2: index + 1] = '%20'
            index -= 3

    return ''.join(new_str)


if __name__ == "__main__":
    test = input()
    print(replace(test))
