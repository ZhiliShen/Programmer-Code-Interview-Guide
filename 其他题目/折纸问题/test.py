# -*- coding: utf-8 -*- # 
# @Time    : 2021-11-28 19:33
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : test.py
# @Notice  :


# 产生第i+1次折痕 就是在第i次产生的每一条折痕的上边插入一道下折痕 下边插入一道上折痕
# 最后折痕的产生能形成一棵满二叉树 头节点为下折痕 每一个节点的左子树头节点为上折痕 右子树节点为下折痕
# 对该棵二叉树进行先右 再中 最后左的遍历即可从上到下进行打印
def print_all_folds(n: int):
    aux(0, n, True)


def aux(index: int, n: int, flag):
    if index == n:
        return
    aux(index + 1, n, True)
    if flag:
        print('down')
    else:
        print('up')
    aux(index + 1, n, False)


if __name__ == "__main__":
    print_all_folds(int(input()))
