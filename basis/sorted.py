# -*- coding: utf-8 -*-
#
# @Time    : 2018/4/8 18:13
# @Author  : svon.me@gmail.com
#

# sorted 数据排序


def sort(value):
    return abs(value)


if __name__ == '__main__':
    arr = [1, 2, 3, 1, 6, 9, 10]
    # 默认排序
    arr2 = sorted(arr)
    # 数组倒序
    arr2.reverse()
    # 指定排序方式
    arr3 = sorted(arr, reverse=True)
    print(arr2)
    print(arr3)
