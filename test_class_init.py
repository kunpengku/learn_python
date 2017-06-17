# 类似单例模式 
# 将实例化一些类，然后放在 类变量中，以后用的时候，直接用类名获取就可以。

class Toy():

    storage = {}

    def __init__(self, age, name):
        self.age = age
        self.name= name
        self.storage[age] = self
    def __repr__(self):
        return '{}--{}'.format(self.age,self.name)


T1 = Toy(1,'ff')
T2 = Toy(3,'dd')


print T1
print T2

print Toy.storage.get(1) == T1
