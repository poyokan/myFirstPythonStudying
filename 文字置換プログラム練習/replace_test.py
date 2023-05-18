# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 16:52:55 2021

@author: kanza
"""

import shutil

def replace_text(target_text,before,after):
    text_after = target_text.replace(before,after)
    return text_after

def replace_list(target_list,before,after):
    
    list_after=[]
    
    for item in target_list:
        item_after = item.replace(before,after)
        list_after.append(item_after)
    
    return(list_after)

def replace_file(target_file,before,after):
    
    back_name = target_file + ".bak"
    shutil.copy(target_file,back_name)
    
    with open(target_file,encoding="utf-8") as reader:
        list_before = reader.readlines()
    
    with open(target_file,"w",encoding="utf-8") as writer:
        for line in list_before :
            line = line.replace(before,after)
            writer.write(line)

replace_file("sample.txt", "デデンネ", "デデカス")