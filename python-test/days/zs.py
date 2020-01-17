#!/usr/bin/env python3
#_*_conding:utf-8_*_

import time

user,passwd = 'zs','zs123'
def auth(func):
	def wrapper(*args,**kwargs):
		username = input("username:").strip()
		password = input("password:").strip()

		if user ==username and passwd == password:
			print("\033[32;1mUser has password authentication\033[0m")
			func(*args,**kwargs)
		else:
			exit("\033[31;1mInvalid username or password\033[0m")
	return wrapper()
@auth
def index():
	print("welome to index page")

@auth
def home():
	print("welcome to home page")

@auth
def bbs():
	print("welcome to bbs page")

index()
home()
bbs()
