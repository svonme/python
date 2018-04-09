# -*- coding: utf-8 -*-
#
# @Time    : 2018/4/4 17:13
# @Author  : svon.me@gmail.com
#

# 迭代，for 循环， python 中所有迭代都是通过 for in 来完成

if __name__ == '__main__':

    print("数组循环: ")
    arr = [1, 2, 3, 4, 5, 6]
    for item in arr:
        print('循环元素: %d' % item)


    print("字典项目: ")
    map = {
        'a': 1,
        'b': 1,
        'c': 1,
        'd': 1,
    }
    for key in map:
        print('循环元素: %s = %s' % (key, map.get(key)))

    # 如果需要获取数组的下标，需要使用 python 内置的 enumerate 函数，把数组变成索引-元素对
    print('enumerate 函数转换数组为索引-元素对')
    for i, value in enumerate(arr):
        print('下标: %s 元素: %s' % (i, value))