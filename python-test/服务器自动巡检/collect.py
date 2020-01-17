#!/usr/bin/env python3
#_*_coding:utf-8_*_
# Only support OS CentOS or Ubuntu

from datetime import datetime, date
import os, sys, time, re, math, socket
import subprocess

###########获取本地外网IP###########
def extranet_ip():
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.connect(('10.255.255.255',0))
	ip = s.getsockname()[0]
	return ip
############# 操作系统版本/主机名/内核版本################
def os_info():
	with open("/etc/issue") as f:
		f = f.read()
		if "\S" in f or "CentOS" in f:
			with open("/etc/redhat-release") as f:
				os_version = f.read().replace('\n', '')
		else:
			os_version = f.split("\n")[0]
	host_name, kernel = os.uname()[1:3]
	os_info = {'os_version': os_version, 'host_name': host_name, 'kernel': kernel}
	return os_info

####################运行时间#####################
def start_time():
	p = subprocess.Popen("date -d \"$(awk -F. '{print $1}' /proc/uptime) second ago\" +'%F %T'", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	outs, errs = p.communicate()
	# bytes to str
	outs = outs.decode('utf-8').replace('\n','')
	# 当前时间
	date_time = date.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
	time = {'start_time': outs, 'current_time': date_time}
	return time

################# CPU核心数量 /CPU占用时间百分比 ###################
#form multiprocessing import cpu_count
#print(cpu_count())
def cpu_count():
	cpu_count = {}
	with open("/proc/cpuinfo") as f:
		for i in f.readlines():
			if "processor" in i:
				cpu_count["cpu_count"] = cpu_count.get("cpu_count", 0) + 1

	return cpu_count

# user nice system idle iowait irq softirq steal guest (从系统启动开始累计到当前)
def cpu_use_time_percent():
	with open('/proc/stat') as f:
		cpu = [int(n) for n in f.readline().split()[1:]]
		total_old = sum(cpu)
		user_old = cpu[0] + cpu[1]
		system_old = cpu[2]
		idle_old = cpu[3]
		iowait_old = cpu[4]

	time.sleep(2)
	with open('/proc/stat') as f:
		cpu = [int(n) for n in f.readline().split[1:]]
		total_new = sum(cpu)
		user_new = cpu[0] + cpu[1]
		system_new = cpu[2]
		idle_new = cpu[3]
		iowait_new = cpu[4]
	cpu_total = float(total_new - total_old)
	cpu_user = float(user_new = user_old)
	cpu_system = float(system_new - system_old)
	cpu_iowait = float(iowait_new - iowait_old)
	# used = float("%.1f" %((1-cpu_idle /cpu_total) * 100))
	user = round(cpu_user / cpu_total * 100, 1)
	system = round(cpu_system / cpu_total * 100, 1)
	iowait =round(cpu_iowait / cpu_total * 100, 1)
	cpu_time = {'user': user, 'system': system, 'iowait': iowait}
	return cpu_time
##############内存利用率#################
def memory():
	memory = {}
	with open("/proc/meminfo") as f:
		for n in range(5):
			mem = f.readline().split()
			memory[mem[0]] = int(mem[1])
	total = memory["MemTotal:"] //1024
	free = (memory['MemFree:'] + memory['Buffers:'] + memory['Cached:']) //1024
	used = total -free
	memory = {'total':total, 'used': used, 'free': free}
	return memory

############# 硬盘分区利用率#################

def disk_partitions():
	part = {}
	with open("/etc/mtab") as f:
		for p in f.readlines():
			if p.startswith("/dev"):
				p = p.split()
				fs = p[0]
				mount = p[1]
				fs_info = os.statvfs(mount)
				# 如果数除不尽则为0，所以要用float取结果浮点数，单位G
				# total = "%.1f" %(float(fs_info.f_bsize * fs_info.f_blocks / 1024 / 1024) /float(1024))
				total = round(float(fs_info.f_bsize * fs_info.f_blocks / 1024 /1024) float(1024), 1)
				# bsize * block = bytes
				used = round(total - used, 1)
				free = round(float(fs_info.f_bsize * fs_info.f_bavail / 1024 / 1024) / float(1024), 1) # bavail: 非超级用户可用块
				part[fs] = part.get(fs, {'mount':mount, 'total': total, 'used': used, 'free': free}) # 如果键存在就返回对应的值，否则新增（以读取的第一个文件系统为 准）
		return part

################# 网卡流量###################

# 通过 IP 获取网卡名
ip = extranet_ip()
def nic_traffic():
	p = subprocess.Popen("ifconfig |awk -F'[: ]' '/^em|^eth|^br|^p3p1|^en/{nic=$1}/%s/{print nic}'" %ip, stdout=subprocess.PIPE, shell=True)
	outs, errs = p.communicate()
	nic = outs.decode("utf-8").replace("\n","")
	with open("/proc/net/dev") as f:
		for s in f.readlines():
			if s.strip().startswith(nic):
				s = s.replace(":"," ")
				in_old = s.split()[1]
				out_old = s.split()[9]
	time.sleep(1)
	with open("/proc/net/dev") as f:
		for s in f.readlines():
			if s.strip().startswith(nic):
				s = s.replace(":"," ")
				in_new = s.split()[1]
				out_new = s.split()[9]
	# // 整除去尾
	traffic_in = (int(in_new) - int(in_old)) // 1024 
	traffic_out = (int(out_new) - int(out_old)) // 1024 
	traffic = {'traffic': {'in': traffic_in, 'out': traffic_out}} 
	return traffic

################ 网络连接#################

def network_status():
	tcp_status = {
		'01':'ESTABLISHED',
		'02':'SYN_SENT',
		'03':'SYN_RECV',
		'04':'FIN_WAIT1',
		'05':'FIN_WAIT2',
		'06':'TIME_WAIT',
		'07':'CLOSE',
		'08':'CLOSE_WAIT',
		'09':'LAST_ACK',
		'0A':'LISTEN',
		'0B':'CLOSING'
	}
	tcp_status_count = {}
	udp_status_count = 0
	listen = {"tcp":[], "tcp6":[], "udp":[], "udp6":[]}
	for t in listen.keys():
		if os.path.exists('/proc/net/%s' %t):
			with open('/proc/net/%s' %t) as f:
				while f:
					line = f.readline()
					if not line: break
					status_line = line.split()
					status = status_line[3]
					if status == "st": continue
					# 统计监听端口
					# TCP
					if status == "0A" and t.startswith("tcp"):
					# 16 to 10
						listen_port = int(status_line[1].split(':')[1], 16)
						listen[t] = listen.get(t, []) + [listen_port]
					# UDP
					elif status == "07" and t.startswith("udp"):
						listen_port = int(status_line[1].split(':')[1], 16)
						listen[t] = listen.get(t, []) + [listen_port]
					# 统计 TCP 连接状态
					status_name = tcp_status[status]
					if t.startswith("tcp"):
						tcp_status_count[status_name] = tcp_status_count.get(status_name, 0) + 1
					else:
						udp_status_count += 1
	network_status = {'listen': listen, 'tcp_status_count': tcp_status_count, 'udp_status_count': udp_status_count}
	return network_status

if __name__ == '__main__':
	result = {}
	os_info = os_info()
	os_info.update(start_time())
	cpu_count = cpu_count()
	cpu_count.update(cpu_use_time_percent())
	network_status = network_status()
	network_status.update(nic_traffic())

	result["ip"] = extranet_ip()
	result["os"] = os_info
	result["memory"] = memory()
	result["cpu"] = cpu_count
	result["disk"] = disk_partitions()
	result["network"] = network_status
	print(result)






