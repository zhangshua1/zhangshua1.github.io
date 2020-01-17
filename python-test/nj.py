#!/usr/bin/env python3
#_*_coding:utf-8_*_

jiwei = 27
count = 0

while count < 3:
	name = int(input("name:"))
	if name == jiwei:
		print("you win!")
		break
	elif name > jiwei:
		print("you max!")
	elif name < jiwei:
		print("you min!")
	count +=1
else:
	print("你输错次数太多！")