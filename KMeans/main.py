#!/usr/bin/env python
# -*- coding: utf-8 -

from numpy import *
from KMeans.load_dataset import load_dataset
from KMeans.k_means_model import kMeans
from KMeans.matplotlib_show import show

FILE_DIR = "D:/KMeans.txt"
k = 4

dataMat = mat(load_dataset(FILE_DIR))
myCentroids, clustAssing= kMeans(dataMat,k)
show(dataMat, k, myCentroids, clustAssing)  
