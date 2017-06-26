
a=['apple', 'orange', 'NNN']
a_e = enumerate(a)
print enumerate(a)
print list( enumerate(a) )
print list( enumerate(a,2) )

#print a_e.'apple'

for i in a_e:
    print i
