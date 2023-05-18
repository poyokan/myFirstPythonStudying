# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 16:42:08 2021

@author: kanza
"""

"初めてのpython"

"練習1"
print("練習1")
print("1から10までの偶数を表示します。")

for i in range(10):
    if (i+1) % 2 == 0:
        print(i+1)
print("")

"練習2"
print("練習2")
print("1から10までの偶数を表示します。")

for i in range(5):
    print((i+1)* 2)
print("")

"練習3"
print("練習3")
print("九九の表")

for i in range(1,10):
    for j in range(1,10):
        print(i*j,"\t",end="")
    print("")

"練習4"
print("練習4")
i = 1
while i <= 5:
    print("*" * i)
    i = i+1
