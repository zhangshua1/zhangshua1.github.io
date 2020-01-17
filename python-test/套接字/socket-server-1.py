#!/usr/bin/env python3
#_*_coding:utf-8_*_

import socket
HOST = ''  #为空代表所有可用的网卡
PORT = 50007  # 任意非特权端口
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
	s.bind((HOST,PORT))
	s.listen(1)  # 最大连接数
	conn, addr = s.accept()  # 返回客户端地址
	with conn:
		print('Connected by', addr)
		while True:
			data = conn.recv(1024)  # 每次最大接收客户端发来数据 1024 字节
			if not data:break  # 当没有数据就退出死循环
			conn.sendall(data)  # 把接收的数据再发给客户端
