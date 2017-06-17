#coding:utf8

class What_for:
    @classmethod
    def id(cls):
        print 'work with {clsa}'.format(clsa=cls)

    @staticmethod
    def uncommon():
        print 'I could be a global function'



def mydeco(func):
    def _nononmane(*argsss, **kw):
        print 'before'
        res = func(*argsss, **kw)
        print 'after'
        return res


    return _nononmane


@mydeco
def add(a,b):
    return a+b

a = What_for()

a.id()
        
a.uncommon()

ret = add(1,3)
print ret

##with 语句，改善了try finally
