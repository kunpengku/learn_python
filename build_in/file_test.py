#coding:utf8

#file 用于打开文件， 可open一样， 但是推荐用open。
#file更适合用于 类型检查，如 instance(f, file)

f = open('a.txt')
print isinstance(f, file)
