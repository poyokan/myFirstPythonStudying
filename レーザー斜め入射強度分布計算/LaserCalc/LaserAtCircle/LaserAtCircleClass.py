# -*- coding: utf-8 -*-

"""
2021-09-16
Kazuma Matsunaga

Python3

"""

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
import os
import json

def getNearestValue(list, num):
    """
    to return the value closest to a value from a list
    
    Parameters
    ---------
    @list: data array (int,float)
    @num: target value (int,float)
    
    Returns
    ---------
    the value closest to target
    """
    
    """
    Calculate the difference between the list element and the target value, 
    and get the index of the minimum value.
    """
    idx = np.abs(np.asarray(list) - num).argmin()
    return [idx,list[idx]]


class LaserAtCircle(Laser):
    """
    Parameters
    ----------
    @power : beam power P[W]
    @laserR : 2Dtuple, beam elliptic radius at receiving surface (omega0x,omega0y)[m]
    @theta : 2Dtuple, beam angle to incident surface (thetax,thetay) [degree]
    @center : 2Dtuple, beam center coordinates at receiving surface (x0,y0)[m]
    @surfaceR : Radius of circular photosensitive surface R0[m]

    Returns
    -------
    None.

    """
    def __init__(self, power, laserR, theta, surfaceR):
        super().__init__(power,laserR,theta)
        
        #self._center = center
        self._surfaceR = surfaceR
    
    # def get_center(self):
        # return self._center
    
    def get_surfaceR(self):
        """Returns radius of receiving surface"""
        return self._surfaceR

    def calc_omega(self):
        """Returns omega/theta [list]"""
        
        omega0x,omega0y=\
        self._laserR[0],\
        self._laserR[1]
        
        thetax,thetay=\
        self._theta[0],\
        self._theta[1]
        
        omegax =omega0x / cos(np.deg2rad(thetax))
        omegay =omega0y / cos(np.deg2rad(thetay))
        
        omega = (omegax,omegay)
        
        return omega

    def calc_I0(self):
        """"Returns I0 [float]"""
        
        P0 = self._power
        
        omega = self.calc_omega()
        omegax,omegay = omega[0],omega[1]
        
        I0 = 2*P0 / pi /omegax /omegay
        
        return I0
    
    def calc_I(self,center):
        """
        @param center : laser center coordinates (x0,y0)[m]
        @Return : I for calculating P
        """
        
        I0 = self.calc_I0()
        
        omega = self.calc_omega()
        omegax,omegay = omega[0],omega[1]
        
        x0,y0 = center[0], center[1]
        
        I = lambda r,theta:\
        I0*r*exp( -2*(\
            ((r*cos(theta)-x0)**2 )/(omegax**2) + \
            ((r*sin(theta)-y0)**2 )/(omegay**2) ) )
            
        return I
    
    def calc_P(self,center):
        """
        @param center : laser center coordinates (x0,y0)[m]
        @Return : receiving power P
        """
    
        R0 = self._surfaceR
        
        I = self.calc_I(center)
        
        P = integrate.dblquad(I,0,2*pi,lambda r:0,lambda r:R0)
        
        return P[0]
    
    def param(self):
        """Return : dict of LaserAtCircle parameter"""
        
        dict = {
                "Beam Power[W]": self._power,
                "Beam radius(omega0x,omega0y)[m]": self._laserR,
                "Beam angle(thetax,thetay)[degree]": self._theta,
                "Radius of circular receiving surface[m]": self._surfaceR
                }
        return dict
        
    def show_param(self):
        
        dict = self.param()
        
        print("-Parameter-")
        
        for key, value in dict.items():
            print(key, ":", value)
        
        print("-----------")
        
    def save(self):
        root = tk.Tk()
        root.attributes("-topmost", True)
        root.withdraw()
        root.lift()
        root.focus_force()
            
        savePath = fd.asksaveasfilename(
            defaultextension = ".txt",
            title = "save file",
            filetypes = [("TXT",".txt")],
            initialdir = "./")
            
        if savePath:
        
            with open(savePath, mode = "w", encoding = "utf-8") as f:
                dict = self.param()
                str = json.dumps(dict)
                f.write(str)
        
        else:
            pass
    
    @classmethod
    def load(cls):
        root = tk.Tk()
        root.attributes("-topmost", True)
        root.withdraw()
        root.lift()
        root.focus_force()
            
        loadPath = fd.askopenfilename(
        filetypes = [("TXT","*.txt")],
        title = "open file",
        initialdir = "./")
        
        if loadPath:
            
            with open(loadPath, mode = "r", encoding = "utf-8") as f:
                str = f.read()
                dict = json.loads(str)
                
                data = LaserAtCircle(
                dict["Beam Power[W]"],
                dict["Beam radius(omega0x,omega0y)[m]"],
                dict["Beam angle(thetax,thetay)[degree]"],
                dict["Radius of circular receiving surface[m]"]
                )
            return data
            
        else :
            pass
    
    # def Plot_P(self,y0):
    #     """
    #     Plot the power by moving the x-coordinate[m] of the center of the laser
    #     --------
    #     @param y0 [m] : y-coordinate of the laser center
    #     """
        
    #     print("now plotting")
        
    #     R0 = self._surfaceR
        
    #     x=np.linspace(-2*R0,2*R0,100)
        
    #     plotlist = [self.calc_P( (i, y0) ) for i in x]
        
    #     fig,ax=plt.subplots()
    #     ax.set_xlabel("Beam position x0 [m]")
    #     ax.set_ylabel("Beam Power [W]")
    #     ax.grid(True)
        
    #     ax.plot(x,plotlist,label=f"y0={y0} [m]")
    #     plt.legend()
        
    #     Anser = input("save?(y/n):")
        
    #     if Anser == "y":
            
    #         root = tk.Tk()
    #         root.attributes('-topmost', True)
    #         root.withdraw()
            
    #         savePath = fd.asksaveasfilename(
    #             defaultextension = ".png",
    #             title = "save file",
    #             filetypes = [("PNG",".png"),("JPEG",".jpg"),("Tiff",".tif")],
    #             initialdir = "./")
            
    #         if savePath:
    #             plt.savefig(savePath)
    
    def calc_LossRatio(self,center):
        """
        @param center : laser center coordinates (x0,y0)[m]
        -------
        @return : Power loss ratio when the laser center is at (x0, y0)[m]
        """
    
        P0 = self._power
        
        loss = self.calc_P(center) / P0
        
        return loss

    def calc_LossRatio_x(self, y0, percent):
        """
        find the x0(absolute value) where the power loss is in {percent}[%]
        by moving the x-coordinate [m] of the laser center
        
        @param y0 [m] : y-coordinate of the laser center
        @param percent : power loss ratio [%]
        --------
        @return : absolute x-coordinate[m] where loss ratio is {percent}
        """
        
        R0 = self._power
        
        x=np.linspace(-2*R0,2*R0,100)
        
        plotlist = [self.calc_loss( (i, y0) ) for i in x]
        
        list1 = getNearestValue(plotlist, 1 - percent/100)
        
        targetx = x[list1[0]]
        
        return np.abs(targetx)
    
    # def plot_P(self, y0, ax):
        
    #     R0 = self._surfaceR
        
    #     x=np.linspace(-2*R0,2*R0,100)
        
    #     plotlist = [self.calc_P( (i, y0) ) for i in x]
        
    #     if ax.__class__.__name__ == "AxesSubplot":
    #         ax.plot(x,plotlist,label=f"y0:{y0} [m]")
        
    #     else:
    #         print("error : ax isn't AxesSubplot")

    # def plot_Ploss(self, y0, percent, ax, minus = False):
        
    #     x0 = self.calc_loss_x(y0, percent)
        
    #     if ax.__class__.__name__ == "AxesSubplot":
            
    #         ax.axvline(x0, ls = "--", label = f"loss:{percent}[%]")
            
    #         if minus is False :
    #             pass
            
    #         elif minus is True :
    #             ax.axvline(-x0, ls = "--")
            
    #         else :
    #             print("error : minus must be True or False")
        
    #     else:
    #         print("errot : ax isn't AxesSubplot")


#param1 = LaserAtCircle(1, (5e-3,5e-3), (0,0), 3.81e-2)

#param1.save()

# print(param1.calc_omega())
# print(param1.calc_I0())
# print(param1.calc_I((0,0)))
# print(param1.calc_P((0,0)))

# param1.Plot_P(0)


# if __name__ is "__main__":
