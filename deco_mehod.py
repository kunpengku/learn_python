#coding:utf8

#   无参数装饰器 – 包装无参数函数
def decorator(func):
    print 'hello in deco'

    return func

@decorator
def foo():
    print 'foo'
    pass


#foo()



# 无参数装饰器 – 包装带参数函数


def decorator_func_args(func):
    def handle_args(*args, **kwargs):
        print 'start'

        func(*args, **kwargs)
        print 'end'


    return handle_args

@decorator_func_args
def foo2(a, b=2):
    print a, b


#foo2(3)


# 带参数装饰器 – 包装无参数函数


def decorator_with_params(arg_of_decorator):
    print arg_of_decorator

    def newDecorator(func):
        
        print func
        return func


    return newDecorator

@decorator_with_params("deco_args")
def foo3():
    print 'foo3'
    pass

#foo3()



# 带参数装饰器– 包装带参数函数

def decorator_with_param_and_func_args(arg_of_deco):
    print arg_of_deco
    def decorator(func):

        def wapper(*args, **kwargs):
            print 'start'
            func(*args, **kwargs)
            print 'end'

        return wapper

    return decorator


@decorator_with_param_and_func_args("last")
def foo4(a, b=2):
    print a, b

foo4(3)


