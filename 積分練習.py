# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 21:10:45 2021

@author: kanza
"""

from scipy import integrate
from numpy import sin
from scipy import pi

I1 = integrate.quad(lambda x:sin(x),0,pi)

print(I1)

R=5

I2 = integrate.dblquad(lambda r,theta:(r**4)*sin(theta),0,pi\
                       ,lambda r:0,lambda r:R)

print(I2)



