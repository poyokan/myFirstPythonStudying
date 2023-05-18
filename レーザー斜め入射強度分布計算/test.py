# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 03:42:27 2021

@author: kanza
"""

# from LaserCalcModule import LaserAtCircle
# import matplotlib.pyplot as plt

# def plotP_load():
#     param = LaserAtCircle.load()
    
#     fig, ax = plt.subplots()
    

import numpy as np

def a(float,tuple):

    print(float,tuple)

    return 0

# a(1,(2,3))

vec_a = np.vectorize(a)
vec_a([1,2],[(3,4)])

