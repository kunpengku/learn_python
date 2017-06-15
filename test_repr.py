from __future__ import unicode_literals

class Basic(object):

    def __repr__(self):
        fields = self.reprs if hasattr(self, 'reprs') else self.columns
        fields = ', '.join(['{k}={v}'.format(k=k, v=getattr(self, k)) for k in fields])
        return ('<{0} {1}>').format(self.__class__.__name__, fields)

class Bind(Basic):


    reprs = {'id', 'name', 'age'}


    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
        self.age1 = None


b = Bind(1,'fp', 30)

print b
print getattr(b, 'age')
print hasattr(b, 'age1')
