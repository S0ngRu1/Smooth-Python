# -*- coding: utf-8 -*-
# @Time : 2024/10/13 13:01
# @Author : CSR
# @File : 逗号代码.py
from typing import List

def process(list_data:List)->str:
    processed_data = ''
    for i in range(len(list_data)):
        if i == len(list_data)-1:
            processed_data = processed_data +'and '+ str(list_data[i])
        else:
            processed_data = processed_data + str(list_data[i]) + ', '
    return processed_data

if __name__ == '__main__':
    spam = ['apples', 'bananas', 'tofu', 'cats']
    print(process(spam))