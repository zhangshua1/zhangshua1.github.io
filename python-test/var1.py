#!/usr/bin/env python3
#_*_coding:utf-8_*_

name = input("name:")
age = input("age:")
job = input("job:")

info = '''
--------info of {_name} ----------
name:{_name}

age:{_age}

job:{_job}
'''.format(_name=name,
		   _age=age,
		   _job=job)

print(info)
