# -*- coding: utf-8 -*- #
# @Time    : 2021-11-11 19:02
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :


def product_1(array: list, mod: int):
    array_len = len(array)
    if array_len == 0 or array_len == 1:
        return None

    zero_count = 0  # 需要额外考虑0的事情 如果0出现了 则这种方法会出现除数是0的不合法情况
    product = 1
    for num in array:
        if num == 0:
            zero_count += 1
        else:
            product *= num

    res = [0 for _ in range(array_len)]
    if zero_count == 1:
        for index, num in enumerate(array):
            if num == 0:
                res[index] = product % mod
                return res
    elif zero_count == 0:
        for index, num in enumerate(array):
            res[index] = (product // num) % mod
        return res
    else:
        return res


def product_2(array: list, mod: int):
    array_len = len(array)
    if array_len == 0 or array_len == 1:
        return None
    res = [0 for _ in range(array_len)]
    res[0] = array[0]
    for index in range(1, array_len-1):   # 现在res[i]代表的就是第i元素以左的乘积
        res[index] = res[index-1] * array[index] % mod

    temp = 1
    for index in range(array_len-1, 0, -1):
        res[index] = res[index-1] * temp % mod  # 现在temp是当前元素右边的乘积(不包含当前元素)
        temp = (temp * array[index]) % mod
    res[0] = temp

    return res


if __name__ == "__main__":
    a, b = map(int, input().split())
    test = list(map(int, input().split()))
    print(*product_2(test, b))
