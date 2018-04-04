# -*- coding: utf-8 -*-
#
# @Time    : 2018/4/4 16:10
# @Author  : svon.me@gmail.com
#

# 切片，第一个参数为元素开始位置，第二个为结束位置
# [start:end]
# python 切片中支持传入负数

if __name__ == '__main__':
    arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

    # 切片
    print('取前三个元素: ', arr[0:3])


    print('省略第一个参数，默认为 0: ', arr[:5])

    print('省略最后一个参数，默认为被切片对象的长度: ', arr[2:])

    print('使用负数，直接获取切片对象最后两个元素: ', arr[-2:])

    print('python 支持切片的对象有 数组，元组，字符串')

    str = "abcdefg"

    print('字符串 "%s" 取前五个字符 = %s' % (str, str[:5]))





