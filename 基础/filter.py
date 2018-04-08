# -*- coding: utf-8 -*-
#
# @Time    : 2018/4/8 17:27
# @Author  : svon.me@gmail.com
#

# filter 数据筛选


def is_odd(n):
    # 判断是否是基数
    return n % 2 == 1

if __name__ == '__main__':

    arr = filter(is_odd, range(5, 50))

    print("筛选后的数据: ", list(arr))
