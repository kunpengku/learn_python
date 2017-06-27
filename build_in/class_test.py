

class A(object):
    def f(self):
        print 'A'

class B(A):

    def f(self):
        print 'B'

    def c(self):
        super(B, self).f()

b=B()
b.f()
b.c()
