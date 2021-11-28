# -*- coding: utf-8 -*- # 
# @Time    : 2021-11-28 20:05
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :


# 若希望得到完美矩形 需要满足 最后拼成的大矩形的面积需要与等于小矩形之和 除了最后拼成的大矩形的四个顶点只出现1次外 其他任何小矩形的顶点都必须出现偶数次
def is_rectangle_cover(rectangles: list):
    if len(rectangles) == 0:
        return False
    left_most, up_most, right_most, bottom_most = float("inf"), -float("inf"), -float("inf"), float("inf")
    rectangle2count = set()
    area = 0
    for rectangle in rectangles:
        left_most = min(left_most, rectangle[0])
        up_most = max(up_most, rectangle[3])
        right_most = max(right_most, rectangle[2])
        bottom_most = min(bottom_most, rectangle[1])
        area += (rectangle[2] - rectangle[0]) * (rectangle[3] - rectangle[1])
        if (rectangle[0], rectangle[1]) in rectangle2count:
            rectangle2count.remove((rectangle[0], rectangle[1]))
        else:
            rectangle2count.add((rectangle[0], rectangle[1]))
        if (rectangle[2], rectangle[3]) in rectangle2count:
            rectangle2count.remove((rectangle[2], rectangle[3]))
        else:
            rectangle2count.add((rectangle[2], rectangle[3]))
        if (rectangle[0], rectangle[3]) in rectangle2count:
            rectangle2count.remove((rectangle[0], rectangle[3]))
        else:
            rectangle2count.add((rectangle[0], rectangle[3]))
        if (rectangle[2], rectangle[1]) in rectangle2count:
            rectangle2count.remove((rectangle[2], rectangle[1]))
        else:
            rectangle2count.add((rectangle[2], rectangle[1]))
    if (left_most, up_most) not in rectangle2count or (left_most, bottom_most) not in rectangle2count or (
    right_most, bottom_most) not in rectangle2count or (right_most, up_most) not in rectangle2count or len(
            rectangle2count) != 4:
        return False
    return area == (right_most - left_most) * (up_most - bottom_most)


if __name__ == "__main__":
    a = int(input())
    test = []
    for _ in range(a):
        b, c, d, e = map(int, input().split())  # 前者是左下角点的坐标 后者是右上角点的坐标
        test.append((b, c, d, e))
    print('Yes' if is_rectangle_cover(test) else 'No')
