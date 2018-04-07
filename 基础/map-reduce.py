# -*- coding: utf-8 -*-
#
# @Time    : 2018/4/6 08:03
# @Author  : svon.me@gmail.com
#

from functools import reduce


if __name__ == '__main__':

    def func(x):
        return x * x

    print(list(map(func, range(10))))

    # 把数组中所有的元素转换为字符串类型
    # str 是系统内置函数，接收一个参数，返回字符串类型结果
    print(list(map(str, range(20, 50))))

    def fn(x, y):
        arr = []
        # 判断第一个元素是否是数组
        if not isinstance(x, list):
            arr.append(x * x)
        else:
            arr = x
        pass
        arr.append(y * y)
        return arr

    print("将数组中的每一个元素平方根", reduce(fn, [1, 3, 5, 7, 9]))