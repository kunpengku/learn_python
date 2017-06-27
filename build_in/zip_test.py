


x=[1,2,3]
y=[4,5,6]


zipped = zip(x,y)
print zipped



x2, y2 = zip(*zipped)

print list(x2) == x
print list(y2) == y
