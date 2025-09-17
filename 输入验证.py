# -*- coding: utf-8 -*-
# @Time : 2024/10/12 21:23
# @Author : CSR
# @File : 输入验证.py

print("请输入一个整数：")
while True:
    try:
        num = int(input())
        break
    except ValueError:
        print("输入有误，请重新输入：")