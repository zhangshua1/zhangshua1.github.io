#!/usr/bin/env python3
#_*_coding:utf-8_*_

import socket
HOST = '192.168.107.106'  # 远程主机
PORT = 50007  # 服务端使用的端口

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
	s.connect((HOST,PORT))
	s.sendall(b'Hello world')  # 发送数据
	data = s.recv(1024)  # 接受数据
print('Received',repr(data))
