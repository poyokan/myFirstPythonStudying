# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 01:11:56 2021

@author: kanza
"""

import os

def replace_filename(old,new):
    
    "現在のディレクトリを取得"
    cwd = os.getcwd()
    
    "現在のディレクトリに存在するファイル名のリストを取得"
    curdir = os.listdir()
    
    list_old = []
    list_new = []
    
    for name_old in curdir:
    
        if name_old != "replace_filename.py" :
            "ファイル名を置換"
            name_new = name_old.replace(old,new)
            
            path_old = cwd + "\\" + name_old
            path_new = cwd + "\\" + name_new
            
            list_old.append(path_old)
            list_new.append(path_new)
            
            if os.path.exists(path_old) == True:
                
                os.rename(path_old ,path_new)

replace_filename("練習","lesson")


