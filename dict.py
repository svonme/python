# -*- coding: utf-8 -*-
#
# @Time    : 2018/3/29 17:52
# @Author  : svon.me@gmail.com
#

# dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度

if __name__ == '__main__':

    # 假设一个班级学院的分数
    score = {
        'adam': 80,
        'benson': 82,
        'colin': 90,
        'david': 75
    }
    print('班级成绩: ', score)

    score['Evan'] = 95   # 后面动态添加元素
    pass

    # 获取某一个键值的value， 使用 get 方法 （可以避免因为 key 不存在而引发的异常）
    print('adam 同学的成绩为 %s' % score.get('adam'))

    score.pop('david')  # 删除某一个键值对元素

    print('修改后的 dict : ', score)