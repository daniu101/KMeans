#!/usr/bin/env python
# -*- coding: utf-8 -

from numpy import *
import numpy as np

#随机生成初始k个质心
def create_cent(dataSet, k):
    n = shape(dataSet)[1] # 矩阵列长度
    centroids = mat(zeros((k,n))) #生成给定形状和类型的用0填充的矩阵
    #随机生成k个质心
    for j in range(n):
        minJ = min(dataSet[:,j])
        rangeJ = float(max(array(dataSet)[:,j]) - minJ)
        centroids[:,j] = minJ + rangeJ * random.rand(k,1)
    return centroids

#计算欧几里得距离
def dist_euclidean(vector_a, vector_b):
    return sqrt(sum(power(vector_a - vector_b, 2)))
    
def kMeans(dataSet, k, distMeas=dist_euclidean, create_cent=create_cent):
    m = shape(dataSet)[0] # 矩阵行长度
    clusterAssment = mat(zeros((m,2))) #生成给定形状和类型的用0填充的矩阵
    centroids = create_cent(dataSet, k) #随机生成初始k个质心
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m): #循环每个点，以分配到最近的质心
            minDist = inf
            minIndex = -1
            for j in range(k): #循环每质心，找到距离i最近的那一个
                distJI = distMeas(centroids[j,:],dataSet[i,:])
                if distJI < minDist:
                    minDist = distJI; 
                    minIndex = j
            if clusterAssment[i,0] != minIndex: 
                clusterChanged = True
            clusterAssment[i,:] = minIndex,minDist**2
        for cent in range(k):#重新计算质心
            ptsInClust = dataSet[nonzero(clusterAssment[:,0].A==cent)[0]] #重新给每个质心分派点
            centroids[cent,:] = mean(ptsInClust, axis=0) 
    return centroids, clusterAssment