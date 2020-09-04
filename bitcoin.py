#!/usr/bin/env python3

#-*-coding: utf-8 -*-

import hashlib
import random
import base58
import ecdsa

# 定义 hash160() 函数
def hash160(data):
    h1 = hashlib.new('sha256',data)
    h2 = hashlib.new('ripemd160',h1.digest())
    return h2.digest()

# 定义 hash256() 函数
def hash256(data):
    h1 = hashlib.new('sha256',data)
    h2 = hashlib.new('sha256',h1.digest())
    return h2.digest()

# base58 转换
b58encode = base58.b58encode
b58decode = base58.b58decode

# 生成一个256位的随机整数
akb = random.getrandbits(256)
print('随机数是：',akb)

# 把随机数转换成十六进制，补齐32位
ske = hex(akb)[2:].zfill(64)
print('私钥是：',ske)

# 
nmb = b'\x80' + bytes.fromhex(ske) + b'\x01'
print('校检码哈希值为：',bytes.hex(hash256(nmb)))
print('校检码哈希值前8位为：',bytes.hex(hash256(nmb))[:8])
print('校检码哈希值前8位为：',bytes.hex(hash256(nmb)[:4]))

hkt = nmb + hash256(nmb)[:4]
print('待转换格式为：',bytes.hex(hkt))
print('WIF格式为：',b58encode(hkt).decode('utf-8'))

# 通过私钥计算公钥
private_key = bytes.fromhex(ske)
sk = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1)
vk = sk.verifying_key.to_string()
print('非压缩公钥是：',bytes.hex(vk))
print('非压缩公钥的长度是：',len(bytes.hex(vk)))
akb = bytes.hex(vk)[-1:]
print('非压缩公钥的最后一位是：',akb)
a2 = ['0','2','4','6','8','a','c','e']
for ske in a2:
    if akb == ske:
        nmb = b'\x02' + vk[:32]
        break
    else:
        nmb = b'\x03' + vk[:32]
hkt = bytes.hex(nmb)
print('压缩公钥是：',hkt)

# 先对公钥数据进行 hash160
sdn = bytes.fromhex('00') + hash160(nmb)

# 计算校检码
check_num = hash256(sdn)[:4]
print('公钥哈希为：',hash256(sdn).hex())
print('校检码为：',bytes.hex(check_num))

# 计算比特币地址
btc_add = b58encode(sdn + check_num).decode('utf-8')
print('比特币地址为：',btc_add)
