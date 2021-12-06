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
            left = mid + 1  # 这里说明mid一定在断点左侧 并且一定不是断点 因为mid已经不是最小值了 所以left取mid+1 进一步推进
        else:  # 这里出现相当则一定不是因为mid与right指向同一个数字所致 而此时mid指向的数字与right指向的数字相等
            #                  left   mid        right(break)
            # 则mid可能在断点的左侧 1     1     2     1
            #                  left        break  mid              right
            # mid也可能是断点的右侧 1     2     1     1     1     1     1
            #                  left        mid(break)  right
            # mid也可能是断点其自身 1     2     1     1     1
            if array[right - 1] <= array[right]:  # 此时right大于等于左边的数字 所以right绝对不可能是断点 因此选择收缩right 而且right不会是0 因为不用担心越界
                right -= 1
            else:   # 如果right是小于左边的数字 则说明right一定是断点
                return right
    return array[left]


if __name__ == "__main__":
    a = int(input())
    test = list(map(int, input().split()))
    print(get_min(test))
