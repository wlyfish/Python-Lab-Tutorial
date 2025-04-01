#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @Time    : 2025/4/1 22:55
 @Author  : wly
 @File    : 字符串填充压缩.py
 @Description: 
"""
str1 = "abcd"
print(str1.ljust(10, 'x'))
print(str1.ljust(4, 'x'))

str2 = "\n ads df oj   opij i p "
print('|' + str2.lstrip() + '|')
print('|' + str2.strip() + '|')
print('|' + str2 + '|')
