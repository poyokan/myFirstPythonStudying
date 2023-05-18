# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 17:37:14 2021

@author: kanza
"""

class Laser :
    """
    Parameters
    ----------
    @power : beam power P[W]
    @laserR :2Dtuple, beam elliptic radius at receiving surface(x0,y0)[m]
    @theta : 2Dtuple, beam angle to incident surface (thetax,thetay) [degree]
        
    Returns
    -------
    None.

    """
    
    def __init__(self, power, laserR, theta):
        self._power = power
        self._laserR = laserR
        self._theta = theta
    
    def get_power(self):
        """Returns Laser Power"""
        return self._power
    
    def get_laserR(self):
        """"Returns Laser Radius"""
        return self._laserR
    
    def get_theta(self):
        """Returns Laser Angle"""
        return self._theta