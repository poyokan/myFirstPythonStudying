# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 17:14:12 2021

@author: kanza
"""

"優しいpython　Lesson5　練習問題"

print("練習1")
testlist = [74,85,69,77,81]
testmax = max(testlist)
testmin = min(testlist)
testave = sum(testlist) / len(testlist)
print("テストの点は",testlist,"です。")
print("最高点は",testmax,"です。")
print("最低点は",testmin,"です。")
print("平均点は",testave,"です。")
print("")

print("練習2")
print("テストの点は",testlist,"です。")
testlist_up = sorted(testlist)
testlist_down = sorted(testlist,reverse=True)
print("昇順は",testlist_up,"です。")
print("降順は",testlist_down,"です。")
print("")

print("練習3")
testlist_80 = [i for i in testlist if i>=80]
print("80点以上は",testlist_80,"です。")
print("80点以上の人は",len(testlist_80),"人です。")
print("")

print("練習4")
city = ["東京","名古屋","大阪","京都","福岡"]
temp_max = [32,28,27,26,27]
temp_min = [25,21,20,19,22]

citytemp = zip(city,temp_max,temp_min)

for i,j,k in citytemp:
    print(i,"の最高気温は",j,"最低気温は",k,"です。")
print()
print("終わり")