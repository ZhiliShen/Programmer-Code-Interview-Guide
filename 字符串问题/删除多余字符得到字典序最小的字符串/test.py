# -*- coding: utf-8 -*- #
# @Time    : 2021/10/16 12:25
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :

# 有些字符只会出现在特定的区间段 一旦离开这个区间段 则没有机会再去选择这些字符了
# 所以需要去记录每个字符所出现的区间段 选择该区间段内字典序最小的字符 删除其后面的所有同种字符 重新建立每个字符所出现的区间段
def remove_duplicate_letters_1(chars: str):
    length = len(chars)
    if length <= 1:
        return chars

    count = [0 for i in range(256)]  # 可以只生成大小为26的数组 但是后续需要计算偏移量

    for char in chars:
        count[ord(char)] += 1

    result = []

    left, right = 0, 0
    # 循环结束的条件是所有字符都被选中了 也就是count数组中所有的值均为0 所以一开始我想while的判断条件写个遍历count数组的数是否都是0
    # 但是这样的处理方法更为优雅 right只有在left到right区间段中的所有字符均已被选过才会到达字符串末尾 所以循环的中止条件就变为了right<length
    while right < length:
        cur_index = ord(chars[right])
        if count[cur_index] == -1:  # 这里一开始想把两个判断条件放一块 (count[cur_index] == -1 or count[cur_index] - 1 > 0): count[cur_index] -= 1 right += 1 但是如果是因为前者进入该分支 是不能执行count[cur_index] -= 1的
            right += 1
        else:
            count[cur_index] -= 1
            if count[cur_index] == 0:
                small_char_index = -1
                for i in range(left, right + 1):  # 在挑选最小char的时候 一定要保证之前选过的字符不要再参与选择了
                    if count[ord(chars[i])] != -1 and (small_char_index == -1 or chars[i] < chars[small_char_index]):
                        small_char_index = i
                result.append(chars[small_char_index])
                count[ord(chars[small_char_index])] = -1  # 选中过后 直接赋值为-1 表明该位置已经被选中了 之前我想的是重新生成一个没有被选中字符的字符串
                for i in range(small_char_index + 1, right + 1):  # 需要重新统计区间段的count 之间在原有的基础加回来就好
                    index = ord(chars[i])
                    if count[index] != -1:
                        count[index] += 1
                left = small_char_index + 1
                right = left
            else:  # 如果当前大于0 则说明后面还有选择它的机会 直接跳过即可
                right += 1

    return ''.join(result)


# 更为优雅的解法
def remove_duplicate_letters_2(chars: str):
    length = len(chars)
    if length <= 1:
        return chars

    count = [0 for i in range(256)]  # 含义同上一解法的count
    in_res = [False for i in range(256)]  # 表明当前字符是否在最终结果中出现

    for char in chars:  # 建立词频统计
        count[ord(char)] += 1

    result = []

    for char in chars:
        count[ord(char)] -= 1
        if in_res[ord(char)]:  # 如果当前字符已经出现在结果中了 就不用再去处理了
            continue
        # 如果当前结果不为空 而且最后一个字符大于当前字符 而且后面还有机会再次选择到最后一个字符 那将其删去 就像老师会优先把奖项给毕业年级学生
        while len(result) > 0 and result[-1] > char and count[ord(result[-1])] > 0:
            in_res[ord(result[-1])] = False  # 注意先设为False 再去除
            result = result[:-1]

        result.append(char)
        in_res[ord(char)] = True  # 表明该字符已经再结果中出现了

    return ''.join(result)


if __name__ == "__main__":
    test = input()
    print(remove_duplicate_letters_2(test))
