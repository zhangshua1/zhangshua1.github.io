#!/usr/bin/env python3
#_*_coding:utf-8_*_

import socket
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-H", "--hostname",help="hostname or ip", required=True)
args = parser.parse_args()

def portScanner(host,port):
	with socket.socket()as s:
		s.settimeout(0.1)
		if s.connect_ex((args.hostname,port)) == 0:
			print("%d open"%port)

if __name__ == '__main__':
	for p in range(1,65535):
		portScanner(args.hostname,p)
	