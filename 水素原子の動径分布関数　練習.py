# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 02:35:57 2021

@author: kanza
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import assoc_laguerre #ラゲール陪関数
from scipy.special import factorial #階乗
from numpy import sqrt
from numpy import exp
import os

x=np.linspace(0,20,100)

"データのプロット"
#n,lはそれぞれ主量子数、方位量子数

irange = 5 #主量子数の範囲
for i in range(irange):
    
    fig,ax= plt.subplots()
    ax.grid(True)
    ax.axhline(0,color="gray")
    ax.axvline(0,color="gray")
    
    n = i+1
    for l in range(i+1):
        
        "動径分布関数R"
        #a0 = 5.292e-11 #ボーア半径[m]
        # x=r/a0 動径方向の変位/ボーア半径
        #R:a0**(3/2)*R
        R = (2/n**2) * sqrt( factorial(n-l-1,False) / factorial(n+l,False)) \
        * exp(-x/n) * assoc_laguerre(2*x/n,n-l-1,2*l+1)
        
        plt.title(r"$a_0\sqrt{a_0}\times R_{nl}$ " + f": n={n}",fontsize=20)
        ax.plot(x,R,label=f"n={n},l={l}")
        ax.set_xlabel(r"$r/a_{0}$",fontsize=15)
        plt.legend(fontsize=15)
        
    filename = f"水素原子の動径分布関数_n={n}.png"
    os.chdir(r"C:\Users\kanza\OneDrive\picture\univ\水素原子の動径分布関数")
    plt.savefig(filename)
    plt.show()
    print(f"主量子数n={n}の描写・保存が終わったよ")
    
    if i == irange -1:
        print("全部終わったよ")

