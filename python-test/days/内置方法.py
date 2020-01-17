#!/usr/bin/env python3
#_*_coding:utf-8_*_

print(abs(-23))
print(all([3,2,-5]))
print(any([3,2,-5]))
print([1,2,"我擦"])
a = bytes("abcde",encoding="utf-8")
print(a.capitalize(),a)
print( a[0] )
print(1/2*3)
a = lambda x:print(x)
a(3)
res = filter(lambda n:n>5,range(10))
for i in res:
	print(i)
import functools
res = functools.reduce( lambda x,y:x+y,range(10) )
print(res)
print(globals())

a = [1,2,3,4]
b = ['z','b','c','d']

for i in zip(a,b):
	print(i)

