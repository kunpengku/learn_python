#coding:utf8

#classmethod  这是一个build-in的函数， 如果类中的方法上面有classmethod修饰，这个方法就变成了 类方法。 类方法的第一个参数是 这个类， 一般取参数名cls。 

class A(object):


    @classmethod
    def f(cls, arg1, arg2):
        print cls
        print arg1,arg2


#调用方法，直接用类名调用 ,或者用 实例都可以调用。
A.f(1,2)

#用实例调用
a = A()
a.f(3,4)


#如果是这个类的子类 调用该方法，那么第一个参数传递过来的就是 子类的 class

class B(A):
    pass


B.f(1,2)


# classmethod不同于 Java中的 静态方法， 因为 还有一个build-in 方法就是  staticmethod
