

class A():
    name='aaa'


    def __init__(self, n):
        self.n =  n


a = A('b')


print a.name
print a.n


print getattr(a, 'name')
print getattr(a, 'n')

print getattr(A, 'name')


print hasattr(a, 'n')
print hasattr(a, 'name')
print hasattr(a, 'me')
