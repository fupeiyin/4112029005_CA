# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 21:33:34 2023

@author: USER
"""
import os
import time
os.mkdir('CS')
file=open('homework.txt','r')
content=file.read()
line=file.readline()
with open('homework.txt','w')as file:
    file.write('4112029005_傅珮茵\n')
with open('homework.txt','r')as file:
    content=file.read()
file_size=os.path.getsize('homework.txt')
print(f'文件大小:{file_size}字節')
modification_time=os.path.getmtime('homework.txt')
print(f'最後修改時間:{modification_time}')
formatted_time=time.ctime(modification_time)
print(f'最後修改時間(人類可讀格式):{formatted_time}')
if os.path.exists('homework.txt'):
    os.remove('homework.txt')




