# -*- coding: utf-8 -*- # 
# @Time    : 2021-11-27 15:55
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
from math import sqrt


# (x1, y1)最左   (x2, y2) 最上
#
# (x3, y3)最下   (x4, y4) 最右

# 该方法用于判断点是否在边平行于坐标轴的矩形内部
def parallel_inside(x1, y1, x4, y4, x, y):
    if x <= x1:
        return False
    if x >= x4:
        return False
    if y >= y1:
        return False
    if y <= y4:
        return False
    return True


# 通过旋转坐标轴 将矩形的边变为平行于坐标轴
def is_inside(x1, y1, x2, y2, x3, y3, x4, y4, x, y):
    if y1 == y2:
        return parallel_inside(x1, y1, x4, y4, x, y)
    l, k = abs(y4 - y3), abs(x4 - x3)
    s = sqrt(l * l + k * k)
    sin, cos = l / s, k / s
    new_x1, new_y1 = cos * x1 + sin * y1, -sin * x1 + cos * y1
    new_x4, new_y4 = cos * x4 + sin * y4, -sin * y4 + cos * y4
    new_x, new_y = cos * x + sin * y, -sin * x + cos * y
    return parallel_inside(new_x1, new_y1, new_x4, new_y4, new_x, new_y)


if __name__ == "__main__":
    a, b = map(float, input().split())
    c, d = map(float, input().split())
    e, f = map(float, input().split())
    g, h = map(float, input().split())
    i, j = map(float, input().split())
    print('Yes' if is_inside(a, b, c, d, e, f, g, h, i, j) else 'No')
