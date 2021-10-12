# -*- coding: utf-8 -*- # 
# @Time    : 2021-10-12 20:27
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test2.py
# @Notice  :
def get_char_at(string: str, target_index):
    if len(string) == 0:
        return 0
    stage = True
    num = 0
    cur_index = 0
    prev_char = None
    for temp in string:
        if temp == '_':
            stage = not stage
        else:
            if stage:
                cur_index += num
                if target_index < cur_index:  # 要始终把cur_index理解为上一个char出现的最后一个位置的后一个位置 也就是新的char出现的第一个位置
                    return prev_char
                prev_char = temp
                num = 0
            else:
                num = num * 10 + (ord(temp) - ord('0'))

    return prev_char if target_index < cur_index + num else 0  # 最后一个字符在循环中并没有被累加 所以需要额外的判断


if __name__ == "__main__":
    print(get_char_at('a_1_b_2_c_4', 2))
