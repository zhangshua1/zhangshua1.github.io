'''for i in range(0,10):
	if i < 5:
		print("loop",i)
'''
'''
for i in range(10):
	print("--------",i)
	for j in range(10):
		print(j)
		if j>5:
			break
'''
'''
import sys
print(sys.argv) #打印环境变量
'''
import nj
import os
#cmd_res = os.system("dir")#执行命令不保存结果
cmd_res = os.popen("dir").read()
print(cmd_res,"----->")
os.mkdir("new_dir")

