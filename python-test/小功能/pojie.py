#!/usr/bin/env python3
#_*_coding:utf-8_*_
import zipfile

def extractFile(zipFile,password):
	try:
		zipFile.extractall(pwd=(password),)
		print("压缩包密码是：" + password)
	except:
		pass

def main():
	zipFile = zipfile.ZipFile('我擦.zip')
	PwdLists = open('passdict.txt')
	for line in PwdLists.readlines():
		Pwd = line.strip('\n')
		guess = extractFile(zipFile, Pwd)

if __name__ == '__main__':
	main()