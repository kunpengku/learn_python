
#compile

code="for i in range(5): print i"

cmpcode = compile(code, '', 'exec')

exec(cmpcode)
