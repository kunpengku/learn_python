#coding:utf8


# staticmethod 不会收到默认的第一个参数 cls。
# staticmethod 类似于Java中的 静态方法
# classmethod 可以说是 静态方法的一个变种，多出来的第一个参数，有时会有神奇的作用。

class A(object):

    @staticmethod
    def f(arg1, arg2):
        print arg1,arg2
# 静态方法 可以用 类名，或者 实例来调用
A.f(1,3)        


A().f(3,4)
