# -*- coding: utf-8 -*-
#
# @Time    : 2018/4/14 22:48
# @Author  : svon.me@gmail.com
#

# __slots__ 限制类中的属性


class Student(object):
    # 限制本类只允许添加 name 与 age 两个属性
    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        # 初始化父类属性值
        super(Student, self).__init__()

        # 赋值
        self.name = name
        self.age = age
        pass


if __name__ == '__main__':

    print(Student('a', 20))