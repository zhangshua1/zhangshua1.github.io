#!/usr/bin/env python3
#_*_coding:utf-8_*_
import getpass
user1 = "zhangshuai"
password1 = 123456

count = 0
while count < 3:
	user = input("请输入账号：")
	password = int(input("请输入密码："))
	if password != password1:
		print("请重新输入！")
	else:
		print("welcome to zhangshuai is home!")
		break
	count += 1
	