#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/5/31 13:19
# @Author  : quasdo
# @Site    : 
# @File    : json_analysis.py
# @Software: PyCharm

import json

with open('a.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

print(data)