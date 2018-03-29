# -*- coding: utf-8 -*-
#
# @Time    : 2018/3/29 18:12
# @Author  : svon.me@gmail.com
#

# set 和 dict 类似，是一个集合，但是元素之间不能重复, set 中的元素时乱序的

if __name__ == '__main__':

    _list = set(['a', 'b', 'c', 'd'])

    # 添加新元素
    _list.add('1')
    _list.add('2')
    _list.add('3')

    print('set 集合中的数据: ', _list)

    _list.remove('a')  # 删除某一个元素

    print('修改后的集合: ', _list)

