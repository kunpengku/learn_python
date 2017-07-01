import json

class A():

    pass

    def __repr__(self):
        all_attr = dir(A)
        s=''
        for attr in all_attr:
           s += '{0}'.format(attr) 
        return s

        


a = A()


print a


a.ddds = 1



print a
print dir(a)
print a.ddds
print a
