
a = [1,2,3,4,5]
print filter(None,a)

a = [-1,0,1,2,3,4,5]
print filter(None,a)


a = [1,2,3,4,5]

def choose_odd(i):
    if i % 2 == 1: 
        return True
    else:
        return False

print filter(choose_odd,a)


# filter(function, iterable) is equivalent to [item for item in iterable if function(item)]



