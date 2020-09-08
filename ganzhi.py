#!/usr/bin/env python3

# -*- coding: utf-8 -*-

a = '甲乙丙丁戊己庚辛壬癸'

s = '子丑寅卯辰巳午未申酉戌亥'

def akb(x):
    v = x % 10 - 1
    b = x % 12 - 1
    return a[v] + s[b]

ske = [akb(x)  for x in range(1,61)]
print(ske)

# 还可以生成不存在的干支组合
def nmb(x):
    v = x % 10 - 1
    b = x % 12
    return a[v] + s[b]

hkt = [nmb(x)  for x in range(1,61)]
print(hkt)
