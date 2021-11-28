# -*- coding: utf-8 -*- # 
# @Time    : 2021-11-27 22:12
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :
from math import sqrt


def get_side_length(x1, y1, x2, y2):
    a_side = abs(x1 - x2)
    b_side = abs(y1 - y2)
    return sqrt(a_side * a_side + b_side * b_side)


# 海伦公式 area=sqrt(p*(p-a)*(p-b)*(p-c)) 其中p=(a+b+c)/2
def get_area(x1, y1, x2, y2, x3, y3):
    a_side = get_side_length(x1, y1, x2, y2)
    b_side = get_side_length(x1, y1, x3, y3)
    c_side = get_side_length(x2, y2, x3, y3)
    p = (a_side + b_side + c_side) / 2
    area = sqrt(p * (p - a_side) * (p - b_side) * (p - c_side))
    return area


def is_inside(x1, y1, x2, y2, x3, y3, x, y):
    area_1 = get_area(x1, y1, x2, y2, x, y)
    area_2 = get_area(x1, y1, x3, y3, x, y)
    area_3 = get_area(x2, y2, x3, y3, x, y)
    area = get_area(x1, y1, x2, y2, x3, y3)
    return area_1 + area_2 + area_3 <= area


# 两个二维向量(x1, y1) (x2, y2)的叉乘仍然为一个向量 方向在z轴 结果为x1*y2-x2*y1
# 此时认为向量的起点在原点 如果(x1, y1)叉乘(x2, y2)的结果为正 则说明(x1, y1)在(x2, y2)的右边
def cross_product(x1, y1, x2, y2):
    return x1 * y2 - x2 * y1


# 如果点在三角形内部 则应始终在三角形边的右边
def is_inside_1(x1, y1, x2, y2, x3, y3, x, y):
    one_three_x, one_three_y = x3 - x1, y3 - y1
    one_two_x, one_two_y = x2 - x1, y2 - y1
    # 如果0-2叉乘0-3的结果为正 说明2在0-3的右边 此时1-2-3的顺序为逆时针 交换2 3 使得1-2-3的顺序变为顺时针
    if cross_product(one_two_x, one_two_y, one_three_x, one_three_y) > 0:
        x3, x2 = x2, x3
        y3, y2 = y2, y3
    one_other_x, one_other_y = x - x1, y - y1
    one_two_x, one_two_y = x2 - x1, y2 - y1
    if cross_product(one_other_x, one_other_y, one_two_x, one_two_y) <= 0:
        return False
    two_other_x, two_other_y = x - x2, y - y2
    two_three_x, two_three_y = x3 - x2, y3 - y2
    if cross_product(two_other_x, two_other_y, two_three_x, two_three_y) <= 0:
        return False
    three_other_x, two_other_y = x - x3, y - y3
    three_one_x, three_one_y = x1 - x3, y1 - y3
    if cross_product(three_other_x, two_other_y, three_one_x, three_one_y) <= 0:
        return False
    return True


if __name__ == "__main__":
    a, b = map(float, input().split())
    c, d = map(float, input().split())
    e, f = map(float, input().split())
    g, h = map(float, input().split())
    print('Yes' if is_inside_1(a, b, c, d, e, f, g, h) else 'No')
