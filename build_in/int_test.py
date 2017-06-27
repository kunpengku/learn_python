#coding:utf8

# '37'是一个八进制数， 转化成十进制
print int('370000000000000000000000000000',8)
print type(int('370000000000000000000000000000',8))

a = list()
b = dict()

b['a'] = 3

print b


print locals()

def xxx():
    a=3
    print locals()
    print globals()


xxx()

