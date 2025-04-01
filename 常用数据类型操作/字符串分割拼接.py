#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @Time    : 2025/4/1 23:08
 @Author  : wly
 @File    : 字符串分割拼接.py
 @Description: 
"""
str1 = "wo \n shi \r sz"
result = str1.splitlines(True)
print(result)
print(str1)

items = ["1", "2", "3"]
result2 = "-".join(items)
print(result2)
