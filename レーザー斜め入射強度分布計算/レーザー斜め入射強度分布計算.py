# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 23:41:07 2021

@author: kanza
"""

#レーザー強度計算

import ast
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from numpy import sin
from numpy import cos
from numpy import exp
from numpy import pi

#パラメータファイル読み込み
paramfile="laser_param.txt"
with open(paramfile) as f:
    param = ast.literal_eval(f.read())
    
    P_0=param["beam_power[W]"]
    
    omega0x_0,omega0y_0=\
        param["beam_radius(x,y)[micro_m]"][0],\
        param["beam_radius(x,y)[micro_m]"][1]
    
    thetax_0,thetay_0=\
        param["theta(x,y)[degree]"][0],\
        param["theta(x,y)[degree]"][1]
    
    x0_0,y0_0=\
        param["lasor center coordinates(x0,y0)"][0],\
        param["lasor center coordinates(x0,y0)"][1]
    
    R_0=param["radius of spherical surface of light receiving(R_0)[mm]"]
    
    print("-デフォルト値-")
    print("ビームパワー[W]:",P_0)
    print("垂直入射ビーム径(x,y)[micro_m]:",omega0x_0,",",omega0y_0)
    print("レーザーの入射角(x,y)[degree]:",thetax_0,",",thetay_0)
    print("レーザーの中心座標(x0,y0)[mm]:",x0_0,",",y0_0)
    print("受光面の半径(R0)[mm]:",R_0)
    print("---")
    
    
    "レーザーの中心を(a,b)としてデフォルトは(x0,y0)"
    "レーザーのx,y方向の入射角をそれぞれ(thetax,thetay)としてデフォルトは(thetax_0,thetay_0)"
    def P(a=x0_0,b=y0_0,\
          thetax=thetax_0,thetay=thetay_0,\
              power=P_0):
        
        "mmに合わせる"
        omegax =1e-3 * omega0x_0 / cos(np.deg2rad(thetax))
        omegay =1e-3 * omega0y_0 / cos(np.deg2rad(thetay))
        
        I0 = 2*power / pi /omegax /omegay
        
        I = lambda r,theta:\
            I0*r*exp( -2*(\
            ((r*cos(theta)-a)**2 )/(omegax**2) + \
            ((r*sin(theta)-b)**2 )/(omegay**2) ) )
        
        P = integrate.dblquad(I,0,2*pi,lambda r:0,lambda r:R_0)
        return P[0]

x=np.linspace(-2*R_0,2*R_0,200)

Pplot = [P(i,0) for i in x]
print(Pplot)

fig,ax=plt.subplots()
ax.grid(True)

# P1=P(x)

ax.plot(x,Pplot)
plt.show




    
# def I(r,theta,I0,x0,y0,omega0x,omega0y):
#     return I0*exp( -2*( ( (r*cos(theta)-x0)**2 )/(omega0x**2) +\
#                        ((r*sin(theta)-y0)**2 )/(omega0y**2)) )

# def P(r0,I0,x0,y0,omega0x,omega0y):
#     return integrate.dblquad(lambda r,theta:r*I,0,2*pi,\
#                              lambda r:0,lambda r:r0)

# def I0(beamP,omega0x,omega0y):
#     return 2*beamP / (pi*omega0x*omega0y)

# beamP = 1
# x0,y0 = 0,0
# r0 = 1e-3
# omega0x,omega0y = 140.35e-6,156.45e-6
# I0 = I0(beamP,omega0x,omega0y)

# P = integrate.dblquad(lambda r,theta:\
#                       I0*exp( -2*( ( (r*cos(theta)-x0)**2 )/(omega0x**2) \
#                        + ((r*sin(theta)-y0)**2 )/(omega0y**2)) ),0,2*pi,\
#                           lambda r:0,lambda r:r0)

# print(P)