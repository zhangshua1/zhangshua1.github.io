#!/usr/bin/env python3
#_*_coding:utf-8_*_
#生成从00000到999999的密码表
f = open('passdict.txt','w')
for id in range(1000000):
	password = str(id).zfill(6)+'\n'
	f.write(password)
f.close()