#!/usr/bin/env python
# -*- coding: utf-8 -

#导入数据
xy = []
def load_dataset(file_path):
    xy = []
    for line in open(file_path):  
        line_tmp = line.split()
        x = float(line_tmp[0])
        y = float(line_tmp[1])
        point = [x,y]
        xy.append(point) 
    return xy
