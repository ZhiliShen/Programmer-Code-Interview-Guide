# -*- coding: utf-8 -*- # 
# @Time    : 2021-05-20 14:58
# @Email   : zhilishen@smail.nju.edu.cn
# @Author  : Zhili Shen
# @File    : temp.py
# @Notice  :
a, b, c = [1, 2, 3]
print(a)
def get_edge_nodes(head: Node):
    temp = []
    left_edge_nodes, right_edge_nodes = [], []
    stack_a, stack_b = deque(), deque()
    if head is not None:
        stack_a.append(head)
        while stack_a:
            while stack_a:
                stack_b.append(stack_a.pop())
            while stack_b:
                cur = stack_b.pop()
                if cur.left is not None:
                    stack_a.append(cur.left)
                if cur.right is not None:
                    stack_a.append(cur.right)
                temp.append(cur)
            left_edge_nodes.append(temp[0].value)
            right_edge_nodes.append(temp[-1].value)
            temp.clear()
    return left_edge_nodes, right_edge_nodes


def get_leaf_nodes(head: Node):
    leaf_nodes, right_nodes = [], []
    if head is not None:
        pre_order(head.left, leaf_nodes)
        pre_order(head.right, right_nodes)
    return leaf_nodes, right_nodes


def pre_order(head: Node, res: List[int]):
    if head is None:
        return
    if head.right is None and head.left is None:
        res.append(head.value)
    pre_order(head.left, res)
    pre_order(head.right, res)


def pre_traversal(head: Node, res: List[int]):
    if head is None:
        return

    res.append(head.value)
    pre_traversal(head.left, res)
    pre_traversal(head.right, res)


def post_traversal(head: Node, res: List[int]):
    if head is None:
        return

    post_traversal(head.left, res)
    post_traversal(head.right, res)
    res.append(head.value)


def print_edge_1(head: Node):
    res = []
    if head is not None:
        left_edge_nodes, right_edge_nodes = get_edge_nodes(head)
        left_leaf_nodes, right_leaf_nodes = get_leaf_nodes(head)
        pre_orders, post_orders = [], []
        pre_traversal(head.left, pre_orders)
        post_traversal(head.right, post_orders)
        for i in [head.value] + pre_orders + post_orders:
            if i in left_edge_nodes + right_edge_nodes + left_leaf_nodes + right_leaf_nodes:
                res.append(i)
        return res


def get_others_node(head: Node, res):
    if head is None:
        return
    res.append(head.value)
    if not (head.left is not None and head.right is not None):
        get_others_node(head.left if head.left is not None else head.right, res)


def print_edge_2(head: Node):
    res = []
    if head is not None:
        left_leaf_nodes, right_leaf_nodes = get_leaf_nodes(head)
        left_others_nodes, right_others_nodes = [], []
        get_others_node(head.left, left_others_nodes)
        get_others_node(head.right, left_others_nodes)
        pre_orders, post_orders = [], []
        pre_traversal(head.left, pre_orders)
        post_traversal(head.right, post_orders)
        for i in [head.value] + pre_orders + post_orders:
            if i in left_leaf_nodes + right_leaf_nodes + left_others_nodes + right_others_nodes + [head.value]:
                res.append(i)
        return res