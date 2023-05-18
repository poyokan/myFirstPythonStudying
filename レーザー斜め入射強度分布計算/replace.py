# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 23:43:59 2021

@author: kanza
"""

import os ,sys

def replace_func(fname,replace_set):
    target,replace = replace_set
    
    with open(fname,"w") as f:
        f.replace(target,replace)

set1 = ["param","default"]
replace_func("レーザー強度分布計算.py",set1)
