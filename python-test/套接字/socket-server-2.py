#!/usr/bin/env python3
#_*_coding:utf-8_*_

import socket
HOST = ''
PORT = 50007
with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as s:
	s.bind((HOST,PORT))
	while True:
		data, addr = s.recvfrom(1024)
		print('Connected by ',addr)
		if not data : break
		s.sendto(data,addr)
