#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @Time    : 2025/4/1 21:11
 @Author  : wly
 @File    : 字符串切片.py
 @Description: 
"""
str1 = "aretqwerqewdafgdgthikytuadsgrtuijtyrqtexvbxvcmnyjhstg"
print(str1[3], str1)
print(str1[-1])
print(str1[::])
print(str1[0:len(str1):1])
print(str1[::2])
print(str1[0:len(str1):-1], len(str1[0:len(str1):-1]))
print(str1[4::-1], len(str1[-1::-1]))
print(str1[::-1])
