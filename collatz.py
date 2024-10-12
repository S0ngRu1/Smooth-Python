# -*- coding: utf-8 -*-
# @Time : 2024/10/12 21:20
# @Author : CSR
# @File : collatz.py

def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1

if __name__ == '__main__':
    while True:
        print('Enter number:')
        number = int(input())
        while number != 1:
            number = collatz(number)