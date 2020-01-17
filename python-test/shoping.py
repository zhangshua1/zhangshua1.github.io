#!/usr/bin/env python3
#_*_coding:utf-8_*_

shangpin = [["iphone",6000],["mac",12000],["ipad",3000],["sanhua",5]]
shop = []
money = input("请输入你的金额：")
if money.isdigit():
	money = int(money)
	while True:
		for index,i in enumerate(shangpin):
			print(index,i)
		num = input("输入你要购买的编号：")
		if num.isdigit():
			num = int(num)
			if num < len(shangpin) and num >=0:
				p_i = shangpin[num]
				if p_i[1] <= money:
					shop.append(p_i)
					money -= p_i[1]
					print("购物车里有%s ,你还有%s元" %(p_i,money))
				else:
					print("\033[41;1m你剩余的钱不够支付了！\033[0m")
		elif num =='q':
			print("---------shoping---------")
			for j in shop:
				print(j)
			print("你还有%s元"%money)
			exit()
		else:
			print("请输入正确的数字！") 
