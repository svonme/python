# -*- coding: utf-8 -*-
#
# @Time    : 2018/4/5 23:11
# @Author  : svon.me@gmail.com
#

# range 列表生成

if __name__ == '__main__':

    arr = list(range(10))  # 快速生成一个数组, 元素默认从 0 开始

    print("生成 10 个元素: ", arr)

    arr2 = list(range(10, 30))  # 生成 20 个元素，元素从 10 开始

    # 高级用法, 元素为每一次循环的平方
    arr3 = [x * x for x in range(1, 11)]

    print(arr3)