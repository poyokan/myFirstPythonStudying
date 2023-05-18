# -*- coding: utf-8 -*-

"latest 2021-9-13"
"Kazuma Matsunaga"


#calculation and plotting of incident laser intensity at circular face



import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from numpy import sin
from numpy import cos
from numpy import exp
from numpy import pi
import ast
import tkinter as tk
import tkinter.filedialog as fd

def main(paramfile):
    
    with open(paramfile) as f:
        
        param = ast.literal_eval(f.read())
        
        P0 = param["beam_power[W]"]
        
        omega0x,omega0y=\
            param["beam_radius(x,y)[m]"][0],\
            param["beam_radius(x,y)[m]"][1]
        
        thetax,thetay=\
            param["theta(x,y)[degree]"][0],\
            param["theta(x,y)[degree]"][1]
        
        x0,y0=\
            param["lasor center coordinates(x0,y0)[m]"][0],\
            param["lasor center coordinates(x0,y0)[m]"][1]
        
        R0 = param["radius of spherical surface for laser receiving(R_0)[m]"]
        
        print("-parameter-")
        print("beam power[W]:",P0)
        print("radius of vertical incident laser at light receiving face(x,y)[m]:",omega0x,",",omega0y)
        print("angle of incident laser(x,y)[degree]:",thetax,",",thetay)
        print("laser center cooridantes(x0,y0)[m]:",x0,",",y0)
        print("radius of circular light receving face(R0)[m]:",R0)
        print("---")
        
    Anser = input("plot graph？(y/n):")
        
    if Anser == "y":
        print("now plotting")
        Plot_P(param)
        print("end")
    
    else:
        print("end")

def calc_omega(param):
    
    omega0x,omega0y=\
    param["beam_radius(x,y)[m]"][0],\
    param["beam_radius(x,y)[m]"][1]
    
    thetax,thetay=\
    param["theta(x,y)[degree]"][0],\
    param["theta(x,y)[degree]"][1]
    
    omegax =omega0x / cos(np.deg2rad(thetax))
    omegay =omega0y / cos(np.deg2rad(thetay))
    
    omega = [omegax,omegay]
    
    return omega

def calc_I0(param):
    
    P0=param["beam_power[W]"]
    
    omega = calc_omega(param)
    omegax,omegay = omega[0],omega[1]
    
    I0 = 2*P0 / pi /omegax /omegay
    
    return I0

def calc_I(param,x0,y0):
    
    I0 = calc_I0(param)
    
    omega = calc_omega(param)
    omegax,omegay = omega[0],omega[1]
    
    I = lambda r,theta:\
    I0*r*exp( -2*(\
        ((r*cos(theta)-x0)**2 )/(omegax**2) + \
        ((r*sin(theta)-y0)**2 )/(omegay**2) ) )
        
    return I

def calc_P(param,x0,y0):
    
    R0 = param["radius of spherical surface for laser receiving(R_0)[m]"]
    
    I = calc_I(param,x0,y0)
    
    P = integrate.dblquad(I,0,2*pi,lambda r:0,lambda r:R0)
    
    return P[0]

def Plot_P(param):
    
    R0 = param["radius of spherical surface for laser receiving(R_0)[m]"]
    
    y0 = param["lasor center coordinates(x0,y0)[m]"][1]
    
    x=np.linspace(-2*R0,2*R0,100)
    
    plotlist = [calc_P(param,i,y0) for i in x]
    
    fig,ax=plt.subplots()
    ax.set_xlabel("Beam position x0 [m]")
    ax.set_ylabel("Beam Power[W]")
    ax.grid(True)
    
    ax.plot(x,plotlist,label=f"y0={y0}[m]")
    plt.legend()
    
    Anser = input("save?(y/n):")
    
    if Anser == "y":
        
        root = tk.Tk()
        root.withdraw()
        
        savePath = fd.asksaveasfilename(
            defaultextension = ".png",
            title = "Choose a file",
            filetypes = [("PNG",".png"),("JPEG",".jpg"),("Tiff",".tif")],
            initialdir = "./")
        
        if savePath:
            plt.savefig(savePath)

def calc_loss(param,x0,y0):
    
    P0=param["beam_power[W]"]
    
    loss = calc_P(param,x0,y0) / P0
    
    return loss



def getNearestValue(list, num):
    """
    概要: リストからある値に最も近い値を返却する関数
    @param list: データ配列
    @param num: 対象値
    @return 対象値に最も近い値
    """

    # リスト要素と対象値の差分を計算し最小値のインデックスを取得
    idx = np.abs(np.asarray(list) - num).argmin()
    return [idx,list[idx]]

def calc_loss_x(param,percent):
    
    R0 = param["radius of spherical surface for laser receiving(R_0)[m]"]
    
    y0 = param["lasor center coordinates(x0,y0)[m]"][1]
    
    x=np.linspace(-2*R0,2*R0,100)
    
    plotlist = [calc_loss(param,i,y0) for i in x]
    
    list1 = getNearestValue(plotlist, 1 - percent/100)
    
    targetx = x[list1[0]]
    return np.abs(targetx)

def Plot_loss(param):
    
    R0 = param["radius of spherical surface for laser receiving(R_0)[m]"]
    
    y0 = param["lasor center coordinates(x0,y0)[m]"][1]
    
    x=np.linspace(-2*R0,2*R0,100)
    
    plotlist = [calc_loss(param,i,y0) for i in x]
    
    fig,ax=plt.subplots()
    ax.set_xlabel("Beam position x0 [m]")
    ax.set_ylabel("Power loss ratio")
    ax.grid(True)
    
    ax.plot(x,plotlist,label=f"y0={y0}[m]")
    
    ax.axvline(calc_loss_x(param,0.1) , ls = "--" , color ="magenta")
    ax.axvline(- calc_loss_x(param,0.1) , ls ="--" , color = "magenta")
    
    ax.axvline(calc_loss_x(param,1) , ls = "--" , color = "navy")
    ax.axvline(- calc_loss_x(param,1) , ls = "--" , color = "navy")
    
    ax.axvline(calc_loss_x(param,5) , ls = "--" , color = "green")
    ax.axvline(- calc_loss_x(param,5) , ls = "--" , color = "green")
    
    plt.xscale("log")
    
    plt.legend()
    
    Anser = input("save?(y/n):")
    
    if Anser == "y":
        
        root = tk.Tk()
        root.withdraw()
        
        savePath = fd.asksaveasfilename(
            defaultextension = ".png",
            title = "Choose a file",
            filetypes = [("PNG",".png"),("JPEG",".jpg"),("Tiff",".tif")],
            initialdir = "./")
        
        if savePath:
            plt.savefig(savePath)
    
    
    
    print("end")

# if __name__=="__main__":
#     targetfile = "laser_param_2.txt"
    
    # main(targetfile)

targetfile = "laser_param_2.txt"

with open("laser_param_2.txt") as f:
        
        param = ast.literal_eval(f.read())
        
        Plot_loss(param)
        
        # x4 = calc_loss_x(param,5)
        # print("+/-",x4,"m")


#The following is a sample of parameter file in txt format
#please use it in the same directory as this program.

#-template-
# =============================================================================
# # 2021-9-13
# {
# 
# # you can use "e" instead of multiplying by powers of 10
# # ex)1.0*10^(-3) -> 1.0e-3
# 
# "beam_power[W]":1,
# 
# # radius of vertical incident laser at light receiving face
# "beam_radius(x,y)[m]":(5e-3,5e-3),
# 
# # theta is angle of incident laser
# "theta(x,y)[degree]":(0,0),
# 
# # y0 is the height of the optical axis, which is required parameter for plotting.
# # x0 is not required for plotting, but if you wanna calculate 
# #the intensity of the laser at a specific position, you can use it.
# "lasor center coordinates(x0,y0)[m]":(0,0),
# 
# "radius of spherical surface for laser receiving(R_0)[m]":3.81e-2
# 
# }
# =============================================================================

#2021-9-13
# changed all the text, etc. to English.
# changed the units of all length parameter to meter
# Added to save plotted images by specifying the directory and file name.
