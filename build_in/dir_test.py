#coding:utf8

# 无参数，返回local的变量
print dir()
print __package__

class A():
    def __dir__(self):
        return [1]



a = A()

print dir(a)

# 如果对象定义了 __dir__方法， dir函数 会调用这个方法。


