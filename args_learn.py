

def add(*arg, **kk):
    print arg
    print kk



def add2(a,b):
    return a+b



d = {"a":1,"b":3}
print add(1,2,3,4,5,d,a=3,b=2,)


def add3(name,age):
    print "I'm {name}, {age} years old".format(name=name, age=age)

l2=(3,4)
print add2(*l2)

l3={}
l3['name']= 'fp'
l3['age']= '27'
print add3(**l3)


