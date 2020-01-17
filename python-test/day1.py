#!/usr/bin/env python3
#_*_coding:utf-8_*_

name = "jiwei"
print("Hello" , name)

name = input(“name:”)
age = input(“age:”)
job = input(“job:”)

info = '''
--------- info of s% --------
name:s%
age:s%
job:s%
''' % (name,name,age,job)

print(info)