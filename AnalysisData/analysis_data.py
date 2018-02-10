#!/usr/bin/env python
# -*- coding: utf-8 - 

from builtins import float
import matplotlib.pyplot as plt

x = []
y = []

#数据路径用户根据自己存放位置更改
for line in open("D:/KMeans.txt"):  
    line_list = line.split()
    _x = float(line_list[0])
    _y = float(line_list[1])

    x.append(_x)
    y.append(_y)
    
plt.scatter(x, y, c = 'g')
plt.show()