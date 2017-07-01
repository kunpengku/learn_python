from functools import wraps


def dry_run(method):
    @wraps(method)
    def wrapper(*args, **kwargs):
        print method.__name__
        return method(*args, **kwargs)

    return wrapper

@dry_run
def f():
    print '123'



print f.__name__
print f.__doc__
