# -*- coding: utf-8 -*- # 
# @Time    : 2021-10-21 12:30
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
def min_length(a_str, b_str):
    a_length, b_length = len(a_str), len(b_str)
    if a_length == 0 or b_length == 0 or a_length < b_length:
        return 0

    # 建立字典 表明a欠b的字母的具体数目
    b2num = [0 for i in range(256)]
    for char in b_str:
        b2num[ord(char)] += 1

    left, right = 0, 0
    match = b_length  # 表明当前str1[left, right]一共欠str2多少个字符 当其为0时 则表明该区间段满足要求
    result = float('inf')

    while right < a_length:  # 一旦right超出区间段都还不起str2的字符 说明left以后开头的字符串也都是还不起的 所以不用进一步考虑了
        b2num[ord(a_str[right])] -= 1
        if b2num[ord(a_str[right])] >= 0:  # 如果归还了之后还是>=0 说明是有效归还 需要将match-1
            match -= 1
            if match == 0:  # 如果全部归还完毕 则表明当前[left, right]是有效区间段 需要进一步收窄left 寻求更小的窗口子串
                while b2num[ord(a_str[left])] < 0:  # 如果归还之后还是不会欠 说明该left可以剔除窗口
                    b2num[ord(a_str[left])] += 1  # 先归还 后left递增 顺序不能弄错
                    left += 1
                result = min(result, right-left+1)
                # eg adabbca 在right为第一个c的情况下 left在第二个a这里跳出收窄left的循环 此时left为3 更小的窗口子串只可能在left后面出现 因为left之前的最小子串都必须以c结尾 必然大于当前的窗口子串
                match += 1  # 此时a又开始欠b相应的字符
                b2num[ord(a_str[left])] += 1  # 先记账 后left从4开始
                left += 1
                right += 1
            else:
                right += 1
        else:
            right += 1

    return result if result != float('inf') else 0  # 如果最后的结果仍然为float('inf') 则表明从来没有符合条件的窗口子串出现过


if __name__ == "__main__":
    a = input()
    b = input()
    print(min_length(a, b))
