# -*- coding: utf-8 -*- # 
# @Time    : 2021-12-03 10:51
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :


# 输入数组代表每个城市所指向的城市 其中指向自己的城市是首都 输出数组代表与首都距离为某一值的城市的数量有多少个
# 先计算每个城市与首都之间的距离 使用负数表示距离能够帮助区分当前数值代表的是已经计算过的与首都的距离 还是下一跳的城市
def paths2distances(paths: list):
    capital = 0
    for index, num in enumerate(paths):
        if paths[index] == index:  # 如果当前城市的下一跳城市指向的是自身 则该城市是首都
            capital = index
        elif num > -1:  # 如果当前数值为自然数
            start_city = index  # 当前城市设置为起始城市
            cur_city = paths[start_city]   # 获取下一跳城市
            pre_city = start_city
            paths[start_city] = -1  # 注意最后才能将起始城市设置为-1 这样方便在回跳的时候终止
            while paths[cur_city] != cur_city:  # 跳出循环的条件是当前城市是否为首都 所以在遍历的时候 不能改变首都的值
                if paths[cur_city] > -1:  # 如果当前数值是自然数 则表明其仍然代表下一跳城市
                    target_city = paths[cur_city]
                    paths[cur_city] = pre_city  # 将当前城市的数值变为上一跳城市 方便回跳
                    pre_city = cur_city
                    cur_city = target_city
                else:  # 如果当前数值代表距离 则可以开始回调过程 并计算遍历过的城市与首都之间的距离
                    break
            if paths[cur_city] == cur_city:  # 如果跳出循环是因为找到了首都 则distance从0开始计算
                distance = 0
            else:   # 否则以已经计算过与首都距离的城市的距离开始计算
                distance = paths[cur_city]
            cur_city = pre_city  # pre_city就是回跳过程开始的第一个城市
            while paths[cur_city] != -1:  # 跳出循环的条件是回到起始城市
                distance -= 1
                pre_city = paths[cur_city]
                paths[cur_city] = distance
                cur_city = pre_city
            distance -= 1
            paths[cur_city] = distance   # 最后设置起始城市
    paths[capital] = 0


# 通过距离数组转换为统计数组
def distances2nums(distances: list):
    for i in range(len(distances)):
        index = distances[i]
        if index < 0:   # 如果当前的数值为负数 则代表与首都之间的距离
            distances[i] = 0  # 注意要把当前数值恢复为0 表示其开始代表记录与首都距离为某该索引值的城市的数量有多少个
            while True:
                index = -index  # 将负数转换为正数 以代表距离
                if distances[index] > -1:  # 如果负责记录该距离有多少个城市的位置已经不是记录距离的含义 则自增后跳出当前循环
                    distances[index] += 1
                    break
                else:
                    next_index = distances[index]  # 如果负责记录该距离有多少个城市的位置仍然是记录距离的含义 则改变其含义 并更新下一跳
                    distances[index] = 1
                    index = next_index
    distances[0] = 1  # 更新首都位置上的值


def paths2nums(paths: list):
    if len(paths) == 0:
        return
    paths2distances(paths)
    distances2nums(paths)


if __name__ == "__main__":
    a = int(input())
    test = list(map(int, input().split()))
    paths2nums(test)
    print(*test)
