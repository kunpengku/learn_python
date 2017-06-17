#coding:utf-8

import multitask

def coroutine_1():
    for i in range(3):
        print 'c1'
        yield i



def coroutine_2():
    for i in range(3):
        print 'c2'
        yield i

multitask.add(coroutine_1())
multitask.add(coroutine_2())


multitask.run()

#生成器很像 迭代器 ，在for i in rangexx 这样的用法用 ，生成器和迭代器的表现是一样的。


