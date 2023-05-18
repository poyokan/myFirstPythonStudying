# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 12:43:32 2021

@author: kanza
"""

list1 = ["ピカチュウ","マイナン","プラスル","パチリス","エモンガ","トゲデマル","モルペコ"]

set1 = [["ピカチュウ","ピカチュウ様だろ"],["デデンネ","デデカス"]]

def replace_list(list_old,list_new,replace_set):
    
    print("置換前リスト:{0}".format(list_old))
    
    target,replace = replace_set
    
    lo = list_old
    
    for item in lo:
        
        #文字列の置換
        item_mod = item.replace(target,replace)
        
        #リストに追加
        lo.append(item_mod)




for item in list1:
    
    #文字列の置換
    item_mod = item.replace("ピカチュウ","ピカチュウ様だろ")
    
    #リストに追加
    list_new.append(item_mod)



print(list1)
print(list_new)
