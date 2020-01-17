#!/usr/bin/env python3
#_*_coding:utf-8_*_

shangpin = [[1,"Iphone",6000],[2,"mac",12000],[3,"ipod",3000],"q"]
shopping = []
money = int(input("请输入你的金额："))
print(shangpin)
shop =int(input("请输入你要购买的商品编号："))
if shop == 1:
	if money > int(shangpin[0][2]):
		shopping.append(shangpin[0])
		print("商品已加入购物车！")
		print(shopping)
	else:
		print("你的金钱不够支付！")
elif shop == 2:
	if money > int(shangpin[1][2]):
		shopping.append(shangpin[1])
		print("商品已加入购物车！")
		print(shopping)
	else:
		print("你的金钱不够支付！")
		
elif shop == 3:
	if money > int(shangpin[2][2]):
		shopping.append(shangpin[2])
		print("商品已加入购物车！")
		print(shopping)
	else:
		print("你的金钱不够支付！")
		

