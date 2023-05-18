# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 18:19:22 2021

@author: kanza
"""

"やさしいpython　Lesson7　練習"

# print("練習1")

# def rpast(num):
#     print("*" * num)

# n = int(input("個数を入力してください"))
# rpast(n)
# print("")

# print("練習2")

# def rpstr(num,str="*"):
#     print(str * num)

# s = input("文字列を入力してください。")
# n = int(input("個数を入力してください。"))
# rpstr(n,s)
# print("")

print("練習3")

def makex(x):
    while True:
        yield x
        x = x+1

# start = int(input("開始値(整数)を入力してください。"))
# stop = int(input("停止値(整数)を入力してください。"))

n = makex(0)
print(next(n))
print(next(n))