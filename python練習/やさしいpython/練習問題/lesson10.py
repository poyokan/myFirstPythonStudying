# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 00:36:07 2021

@author: kanza
"""

import os
import datetime

def lesson9_1():
    curdir = os.listdir(".")
    
    print("名前",end="\t")
    print("サイズ")
    for name in curdir:
        size = os.path.getsize(name)
        print(name , end="\t")
        print(size,"バイト")
        
        
def lesson9_2():
    curdir = os.listdir(".")
    
    print("名前",end="/t")
    print("最終アクセス時刻")
    
    for name in curdir:
        timestamp = os.path.getatime(name)
        time = datetime.datetime.fromtimestamp(timestamp)
        print(name,end = "\t")
        print(time)

# lesson9_1()
lesson9_2()