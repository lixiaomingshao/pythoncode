#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import hashlib

# 定义md5函数
def md5hash(data):
    akb = hashlib.new('md5',data)
    return akb.hexdigest()

# 定义sha1函数
def sha1hash(data):
    ske = hashlib.new('sha1',data)
    return ske.hexdigest()

# 输入文件的路径
filename = input('请输入文件的路径：')
# 计算时用with语句来分开调用，不然会计算到不同的结果
with open(filename,'rb') as f:
    print(md5hash(f.read()))
with open(filename,'rb') as f:
    print(sha1hash(f.read()))
