# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 18:23:52 2021

@author: kanza
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import assoc_laguerre #ラゲール陪関数
from scipy.special import factorial #階乗
from numpy import sqrt
from numpy import exp



#(n,l)=(1,0) #n,lはそれぞれ主量子数、方位量子数

#nlset=[(1,0),(2,0),(2,1)]
#n,l = nl[0],nl[1]


nlset = [ [(1,0)],\
         [(2,0),(2,1)],\
         [(3,0),(3,1),(3,2)] ]

k0set = len(nlset)
k1set = [0,1,2]
"後で直す"


print("(主量子数n,方位量子数l)は",nlset)



#a0 = 5.292e-11 #ボーア半径[m]



#n,l = nl[0],nl[1]

x=np.linspace(0,20,100)

def Plotdata(n,l,k0,k1,filename):
    "データのプロット"
    
    "動径分布関数R"
    # x=r/a0 動径方向の変位/ボーア半径
    #R:a0**(3/2)*R
    R = (2/n**2) * sqrt( factorial(n-l-1,False) / factorial(n+l,False)) \
    * exp(-x/n) * assoc_laguerre(2*x/n,n-l-1,2*l+1)
    
    
    fig,ax= plt.subplots()
    ax.grid(True)
    ax.axhline(0,color="gray")
    ax.axvline(0,color="gray")
    
    
    n,l =nlset[k0][k1][0],nlset[k0][k1][1]
        
    for k0 in range(k0set):
        if nlset[k0]
        for k1 in k1set:
        
            plt.title(r"$a_0\sqrt{a_0}\times R_{nl}$",fontsize=20)
            ax.plot(x,R,label=f"n={n},l={l}")
            plt.legend(fontsize=15)
        
        #plt.savefig(filename)
        plt.show()
    
    
    nlset = [(1,0),(2,0),(2,1),(3,0),(3,1),(3,2)]
    countn = [1,2,2,3,3,3]
    
    

def Plotl() :
    fig,ax= plt.subplots()
    ax.grid(True)
    ax.axhline(0,color="gray")
    ax.axvline(0,color="gray")
    
    nlset = [(2,0),(2,1)]
    
    n = nlset[0]
    
    
    "動径分布関数R"
    # x=r/a0 動径方向の変位/ボーア半径
    #R:a0**(3/2)*R
    R = (2/n**2) * sqrt( factorial(n-l-1,False) / factorial(n+l,False)) \
    * exp(-x/n) * assoc_laguerre(2*x/n,n-l-1,2*l+1)
    
    plt.title(r"$a_0\sqrt{a_0}\times R_{nl}$",fontsize=20)
    ax.plot(x,R,label=f"n={n},l={l}")
    plt.legend(fontsize=15)




