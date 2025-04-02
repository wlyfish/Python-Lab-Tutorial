#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @Time    : 2025/4/2 10:00
 @Author  : wly
 @File    : 字符串判定.py
 @Description: 
"""
str1 = 'aE'
print(str1.isalpha())

str2 = '34 '
print(str2.isdigit())

str3 = 'sdf23'
print(str3.isalnum())

str4 = " \r"
print(str4.isspace())

print('wo' in 'di wo n.')
