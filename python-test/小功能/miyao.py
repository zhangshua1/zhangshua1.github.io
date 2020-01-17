import itertools as its

words = "1234567890"
r = its.product(words,repeat=6)
dic = open("./password.txt","a")
for i in r:
	dic.write("".join(i))
	dic.write("".join("\n"))
	print(i)
dic.close()
print("密码本已生成")