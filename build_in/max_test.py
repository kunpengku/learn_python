

print max([1,2,3,4])

def f(x):
    if x==2: 
        return 2
    else:
        return 1
print max([1,2,3,4], key=f)
