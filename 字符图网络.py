# -*- coding: utf-8 -*-
# @Time : 2024/10/13 13:07
# @Author : CSR
# @File : 字符图网络.py

grid = [['|',' ',' ',' '],
        ['+','-','-','-','-','-','-'],
        ['|',' ',' ',' '],
        ['+','-','-','-','-','-','-']]
new_grid = []
max_len = len(max(grid, key=len))
for row in range(max_len):
        new_row = []
        for col in range(len(grid)):
                try:
                        new_row.append(grid[col][row])
                except IndexError:
                        new_row.append(' ')
        new_grid.append(new_row)

for row in new_grid:
        print(''.join(row))