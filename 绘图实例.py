# -*- coding: utf-8 -*-
# @Time : 11/23/24 12:02 AM
# @Author : CSR
# @File : 绘图实例.py
from cProfile import label

import numpy as np
import matplotlib.pyplot as plt


# 生成数据
x = np.arange(0, 6, 0.1)
# 以0.1为单位，生成0到6的数据

y = np.sin(x)

y2 = np.cos(x)

# 绘制图形
plt.plot(x, y,label='sin')
plt.plot(x, y2,linestyle = '--',label='cos')
plt.xlabel('x')
plt.ylabel('y')
plt.title('sin & cos')
plt.legend()
plt.show()


import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('/home/caisongrui/Pictures/pexels-8moments-1183099.jpg')
plt.imshow(img)

plt.show()