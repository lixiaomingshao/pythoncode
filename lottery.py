#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

# 彩票函数,代表从1到a（a > 1）中取v（v >= 1）个数字
def lottery(a,v):
    akb = set([])
    while len(akb) < v:
        ske = random.randint(1,a)
        akb.add(ske)
    return sorted(list(akb))

print('今期的大乐透号码为：')
print('前区号码：',lottery(35,5))
print('后区号码：',lottery(12,2),)
print('***')
print('今期的双色球号码为：')
print('红球：',lottery(33,6))
print('蓝球：',lottery(16,1))
    
