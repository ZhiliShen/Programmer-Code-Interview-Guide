# -*- coding: utf-8 -*- # 
# @Time    : 2021-10-25 20:39
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
from typing import List
from functools import cmp_to_key


# a.b->a拼接b
# 如果a.b < b.a 则a在b前 根据这个标准对字符串数组进行升序排列 最后拼接得到的字符串即是结果
# 但是实现比较函数的时候需要注意以下三点
# 自反性 a=a 反对称性 a<b->b>a 传递性 a<=b b<=c -> a <= c
# 而这样的比较函数需要证明其满足传递性 书中则是将字母看作26进制 将其视作数字进行证明 所以书上的证明视为了表明该比较函数是合法的
# 而python2.x原来是支持传入比较函数 但是在python3.x中可能考虑到传入的cmp函数的不合法 进而转变为key接口 保证接受的本身即是一个可比较的值
# 所以我们需要依赖functools.cmp_to_key来将cmp进行转换
def lowest_string(str_list: List[str]):
    str_list_len = len(str_list)
    if str_list_len == 0:
        return ''
    str_list.sort(key=cmp_to_key(cmp))
    return ''.join(str_list)


def cmp(a: str, b: str):
    if a + b > b + a:
        return 1
    else:
        return -1


if __name__ == "__main__":
    n = int(input())
    test = []
    for _ in range(n):
        test.append(input())
    print(lowest_string(test))
