#!/usr/bin/env python3
#_*_coding:utf-8_*_

import os,sys
import paramiko
base_dir = os.path.dirname(os.path.abspath(__file__))
host_file = "%s/host.info" %bash_dir
collect_file = "%s/collect.py" %bash_dir

import csv , codecs

with codecs.open('result.csv', 'w', 'gbk') as f1:
	csv_file = csv.writer(f1)
	csv_file.writerow(['IP地址','主机名','操作系统','内存','CPU','硬盘','网络连接状态','监听端口','网卡流量'])

	with open(host_file) as f:
		# 遍历主机列表
		while f:
			line = f.readline()
			if not line: break
			line = line.split()
			hostname = line[0]
			port = int(line[1])
			username = line[2]
			password = line[3]
			if not os.path.isfile(collect_file):
				print(collect_file + "文件不存在！")
				sys.exit(1)

			try:
				s = paramiko.Transport((hostname,port))
				s.connect(username=username,password=password)
			except Exception as e:
				print(e)
				continue
			# 上传收集程序到目标主机
			remote_file = "/tmp/collect.py"
			sftp = paramiko.SFTPClient.from_transport(s)
			sftp.put(collect_file,remote_file)
			try:
				sftp.file(remote_file)
				# 在目标主机执行收集程序
				client = paramiko.SSHClient()
				client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
				client.connect(hostname,port,username,password)
				stdin,stdout,stderr = client.exec_command('python3 %s' %remote_file)
				stdout = stdout.read()
				error = stderr.read()

				if not error:
					# 处理从主机收集的数据
					result = eval(stdout.decode('utf-8'))
					ip = result["ip"]
					os_info = result["os"]
					memory = result["memory"]
					cpu = result["cpu"]
					disk = result["disk"]
					network = result["network"]
					# 系统信息
					host_name = os_info["host_name"]
					os_version = "os_version: %s" % os_info["os_version"] + "\n" \
								  + "kernel: %s" %os_info["kernel"] + "\n" \
								  + "start_time: %s" %os_info["start_time"] + "\n" \
								  + "current_time: %s" %os_info["current_time"]
					# 内存
					m = ''
					for k,v in memory.items():
						m +="%s: %sM" %(k,v) + "\n"
					# CPU
					c = ''
					for k,v in cpu.items():
						c +="%s: %s" %(k,v) + "\n"
					# 硬盘
					d = ''
					for k,v in disk.items():
						fs = k
						mount = v["mount"]
						total =v["total"]
						avail = v["free"]
						used = v["used"]
						d +="%s -> %s.total: %s,avail: %s,used: %s" %(fs,mount,total,avail,used) + "\n"
					# 连接状态统计
					status_count = ''
					for k,v in network["tcp_status_count"].items():
						status_count +="%s: %s" %(k, v) + "\n"
					status_count     +     "\n"     +     "%s:udp_status_count" %(network["udp_status_count"])
					# 监听端口
					listen = ''

					for k,v in network["listen"].items():
						v = list(set(v))
						listen +="%s: %s" %(k,v) + "\n"
					# 网卡流量
					traffic = ''
					for k, v in network["traffic"].items():
						traffic +="%s: %sKB" %(k,v) + "\n"
					# 写入csv
					with codecs.open('result.csv', 'a', 'gbk') as f2:
						csv_file = csv.writer(f2)
						data = [
							(ip, host_name, os_version, m, c, d, status_count, listen, traffic)
						]
						csv_file.writerow(data)
					else:
						print(error)
					#删除上传到目标主机的收集程序
					#client.exec_command('rm -f %s' %remote_file)
					#client.close()
				except Exception as e:
					print(e)
					continue
				finally:
					s.close()
				

