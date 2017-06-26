#coding:utf8

#bin(x)  
#bin返回一个字符串， 输入参数的二进制形式。

print bin(0)
print bin(1)
print bin(3)
print bin(4)
print type(bin(5))



# 如果传入参数不是一个 数字，那么这个对象，需要实现__index__方法，
# 来返回一个数字，然后bin会返回这个数字的 二进制形式
class A():
    def __index__(self):
        return 7


a = A()

print bin(a)
