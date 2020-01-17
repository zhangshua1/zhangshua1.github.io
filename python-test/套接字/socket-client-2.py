#!/usr/bin/env python3
#_*_coding:utf-8_*_
import socket
HOST = '127.0.0.1'
PORT = 50007
with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as s:
	s.sendto(b'Hello world ',(HOST,PORT))
	data = s.recv(1024)
	print('Received',repr(data))
