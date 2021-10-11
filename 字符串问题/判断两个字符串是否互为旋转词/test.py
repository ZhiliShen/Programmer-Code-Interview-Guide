# -*- coding: utf-8 -*- #
# @Time    : 2021-10-10 22:06
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
def kmp(a_str: str, target: str):
    if len(a_str) == 0 or len(target) == 0 or len(a_str) < len(target):
        return -1

    next_array = get_next_array(target)
    a_str_index = 0
    target_index = 0

    while a_str_index < len(a_str) and target_index < len(target):
        if a_str[a_str_index] == target[target_index]:  # 正常匹配就往下走
            a_str_index += 1
            target_index += 1
        else:
            if target_index == 0:
                a_str_index += 1
            else:
                target_index = next_array[target_index]

    return a_str_index - target_index if target_index == len(target) else -1  # target到头说明字符串匹配完毕


def get_next_array(target: str):
    if len(target) == 1:
        return [-1]

    next_array = [0 for i in range(len(target))]
    next_array[0] = -1
    next_array[1] = 0

    index = 2
    pre_index = 0

    while index < len(target):
        if target[index - 1] == target[pre_index]:
            next_array[index] = pre_index + 1
            pre_index += 1  # 注意这里不要写成pre_index = index pre_index并不是上一个index的含义 而是指上一个index的可以滑动到的位置 所以直接在原来的基础上+1即可
            index += 1
        else:
            if pre_index == 0:
                next_array[index] = 0
                index += 1  # 写while循环一定要对标识变量进行变化
            else:
                pre_index = next_array[pre_index]

    return next_array


def is_rotation(a_str: str, b_str: str):
    if len(a_str) != len(b_str):
        return 'NO'
    c_str = b_str + b_str
    if kmp(c_str, a_str) != -1:
        return 'YES'
    else:
        return 'NO'


if __name__ == "__main__":
    num_a, num_b = map(int, input().split())  # 注意命名空间不要被污染
    str1 = input()
    str2 = input()
    print(is_rotation(str1, str2))
