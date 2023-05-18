# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 00:18:34 2021

@author: kanza
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import assoc_laguerre #ラゲール陪関数　日本のwikiと定義が違うので注意
from scipy.special import factorial #階乗
import os 


ylength = 4

def Plotdata(k):
    fig,ax= plt.subplots()
    ax.grid(True)
    ax.axhline(0,color="gray")
    ax.axvline(0,color="gray")
    #ax.set_aspect("equal")
    
    for n in range(5):
        x=np.linspace(0,10,100)
        L=assoc_laguerre(x,n-k,k)#Lはn!で割ってある k,nは日本のラゲール多項式の上付き添え字、下付添え字
        plt.title("$L^{}_n(x)/n!$".format(k))
        ax.plot(x,L,label="n={}".format(n))
        ax.set_xlabel("x")
        ax.set_ylim(-ylength,ylength)
        ax.set_xlim(0,10)

for k in range(2):
    Plotdata(k)
    plt.legend()
    os.chdir(r"C:\Users\kanza\OneDrive\picture\univ")
    filename="ラゲール陪多項式 k={}.png".format(k)
    plt.savefig(filename)
    plt.show
    print("k={}の描画と保存が終わったよ".format(k))

