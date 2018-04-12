# -*- coding: utf-8 -*-
#
# @Time    : 2018/4/13 00:13
# @Author  : svon.me@gmail.com
#


# 类


class Person(object):

    # 构造函数
    def __init__(self, name, age):
        # 初始化父类属性值
        super(Person, self).__init__()

        # 赋值
        self.name = name
        self.age = age

    def introduce(self):
        print("我的名字是%s, 我今年%s岁" % (self.name, self.age))


if __name__ == '__main__':

    person = Person('张三', 22)
    person.introduce()
