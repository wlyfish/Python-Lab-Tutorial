#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @Time    : 2025/4/1 19:54
 @Author  : wly
 @File    : 字符串1.py
 @Description: 
"""
str1 = "he\\nll\to \"w\'o\nr\
ld"
print(str1, type(str1))

str2 = r'hell\no python'
print(str2, type(str2))

str3 = ("hello"
        "Python")
print(str3, type(str3))

str4 = """hello
 python"""
print(str4, type(str4))
