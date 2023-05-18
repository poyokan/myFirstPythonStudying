 -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 19:16:58 2021

@author: kanza
"""

list_a =[(i+1,j) for i in range(2) for j in range(i+1)]
print(list_a)
# list_b =[]

# for elem in list_a:
#     list_b.append(elem[0])

# print("list_aは",list_a)
# print("list_bは",list_b)

# set_b = set(list_b)
# for elem in set_b:
#     num =list_b.count(elem)
#     print(f"{elem}の個数:{num}")


list_b = [elem[0] for elem in list_a]
print(list_b)

list_c = [list_b.count(elem) for elem in set(list_b)]
print(list_c)