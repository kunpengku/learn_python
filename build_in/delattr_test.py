#coding:utf8


#delattr
# delattr 可以删除 实例属性，但不能删除 类属性。

class A():
    name='fp'

    def __init__(self):
        self.n = 'wi'


a = A()


print a
print a.name
print a.n

print dir(a)

delattr(a, 'n')
# is equivalent to del a.n

print a
print a.name
print a.n
