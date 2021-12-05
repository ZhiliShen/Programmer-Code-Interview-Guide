# -*- coding: utf-8 -*- # 
# @Time    : 2021-12-05 15:59
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :

# 首先区间中right上的数字一定是小于等于断点左侧的数字 大于等于断点右侧的数字
# 所以我们只需要比较mid与断点之间的关系 来缩短区间即可
def get_min(array: list):
    left, right = 0, len(array) - 1
    while left < right:
        mid = left + (right - left) // 2
        if array[mid] < array[right]:
            right = mid  # 这里说明mid一定在断点右侧 而且很可能是断点 所以right取mid
        elif array[mid] > array[right]:
            left = mid+1  # 这里说明mid一定在断点左侧 并且一定不是断点 因为mid已经不是最小值了 所以left取mid+1 进一步推进
        else:
            right -= 1  # 这里出现相当则一定不是因为mid与right指向同一个数字所致 而此时mid指向的数字与right指向的数字一致 则mid可能在断点的左侧 也可能是断点的右侧 也可能是断点自身 但此时right绝对不可能是断点 因此选择收缩right是最为稳妥的选择
    return array[left]


if __name__ == "__main__":
    a = int(input())
    test = list(map(int, input().split()))
    print(get_min(test))
