# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 20:22:58 2021

@author: kanza
"""

#https://amorphous.tf.chiba-u.jp/lecture.files/chem_computer/11_scipy%E3%81%AE%E5%9F%BA%E6%9C%AC%E3%81%A8%E5%BF%9C%E7%94%A8/11.html

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import lpmv

# scipy.special.lpmv(m, v, x)
# order m(磁気量子数; m), degree v(方位量子数; l)
theta = np.linspace(0, 2*np.pi, 1000)
x = np.cos(theta)
fig, ax = plt.subplots()
ax.plot(theta * 180/np.pi, lpmv(0, 1, x), label="$l=1, m=0$")
ax.plot(theta * 180/np.pi, lpmv(1, 1, x), label="$l=1, m=1$")
ax.plot(theta * 180/np.pi, lpmv(0, 2, x), label="$l=2, m=0$")
ax.plot(theta * 180/np.pi, lpmv(1, 2, x), label="$l=2, m=1$")
ax.plot(theta * 180/np.pi, lpmv(2, 2, x), label="$l=2, m=2$")
ax.legend()
ax.set_xlabel("angle/deg.")
ax.set_ylabel("$P^m_l$")
fig.savefig("legendre.png")
plt.show()
