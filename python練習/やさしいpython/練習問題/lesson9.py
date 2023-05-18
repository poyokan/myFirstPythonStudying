# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 19:21:42 2021

@author: kanza
"""

"やさしいpython"
"lesson9"

import re

"問題1"

def check_extension(filelist):
    print("ファイルのリストは以下です。")
    
    for i in filelist:
        print(i)
    
    check = input("拡張子を入力してください。")
    
    print("該当するファイルは以下です。")
    
    checkfile = []
    
    for f in filelist:
        if f.endswith(check) is True:
            checkfile.append(f)
            
            
    if not checkfile:
        print("該当するファイルはありません。")
    
    else:
        for i in checkfile:
            print(i)

filelist1 =["Sample.csv","Sample.exe","Sample1.py","Sample2.py","Sample.txt",\
            "index.html"]

# print("--問題1--")
# check_extension(filelist1)
# print("")

"問題2"


def check_match(list,pattern):
    
    list1 = []
    
    for str in list:
        
        ptr = re.compile(pattern)
        res = ptr.search(str)
        
        if res is not None:
            m = "○"
            list1.append(m)
        
        else:
            m = "×"
            list1.append(m)
    
    print("パターン:"+pattern)
    
    for d in zip(list,list1):
        print(d)
    
    print("-----")

# print("--問題2--")

# list1 = ["113","010"]
# list2 = ["xA","xX1"]
# list3 = ["product","12A_"]
# list4 = ["3330000","106-0001"]

# check_match(list1,"[012]{3}")
# check_match(list2,"x[0-9A-Fa-f]{2,4}")
# check_match(list3,"^[a-zA-Z_][a-zA-Z0-9_]*")
# check_match(list4,"[0-9]{3}-[0-9]{4}")
