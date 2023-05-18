#                               -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 20:14:57 2021

@author: kanza
"""

#https://amorphous.tf.chiba-u.jp/lecture.files/chem_computer/11_scipy%E3%81%AE%E5%9F%BA%E6%9C%AC%E3%81%A8%E5%BF%9C%E7%94%A8/11.html

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import sph_harm
# =============================================================================
#球面調和関数：sph_harm,引数は(degree,order,theta,phi)
#degree:方位量子数m
#order:磁気量子数l
#theta,phi:極座標の偏角
# =============================================================================
from mpl_toolkits.mplot3d import Axes3D

def PlotData(Ylm, theta, phi, lm, outfile=None):
    """
    データのプロット
    """
    l, m = lm[0], lm[1]
    # |Ylm|がなぞるベクトルの先端を計算
    r = np.abs(Ylm.real)
    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)
    color = np.ones(r.shape)  # 正負の色つけのため   
    color[Ylm < 0] = -1       # 正負の色つけのため
    fig = plt.figure()#プロット領域の作成
    ax = fig.gca(projection='3d')#プロット中の軸の取得　gcaは"Get Current Axes"
    ax.plot_surface(x, y, z, facecolors=plt.cm.jet(color),#cmapはカラーマップ
                    rstride=1, cstride=1)#rstride,cstrideはそれぞれ何ステップずつプロットするか指定
    plt.title("$Y^{{m={}}}_{{l={}}}$".format(m, l), size=20)
    length = 0.5
    ax.set_xlim(-length, length)
    ax.set_ylim(-length, length)
    ax.set_zlim(-length, length)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.setp(ax.get_xticklabels(), visible=False)#setpは"set property" 第一引数で指定したオブジェクトに条件を付与。今回は値を見えなくしている。
    plt.setp(ax.get_yticklabels(), visible=False)
    plt.setp(ax.get_zticklabels(), visible=False)
    if outfile is not None:
        fig.savefig(outfile)
        print(outfile, "was created.")

def CalcYlm(lm):
    l, m = lm[0], lm[1]
    # order=m degree=lで球面調和関数を計算
    t = np.linspace(0, np.pi, 50)#0~piまでデータ点50個のデータを作る
    p = np.linspace(0, 2 * np.pi, 100)
    theta, phi = np.meshgrid(t, p)#格子状のデータ点を作る際のやつ
    if m == 0:
        Y = sph_harm(m, l, phi, theta)
    if m > 0:
        Ya = sph_harm(-m, l, phi, theta)
        Yb = sph_harm(m, l, phi, theta)
        Y = 1/np.sqrt(2) * (Ya + (-1)**m*Yb)
    if m < 0:
        Ya = sph_harm(m, l, phi, theta)
        Yb = sph_harm(-m, l, phi, theta)
        Y = 1j/np.sqrt(2) * (Ya - (-1)**m*Yb)
    return Y, theta, phi

# (l, m)の組み合わせを好きなだけ
lmset = [(1, -1), (1, 0), (1, 1),
         (2, -2), (2, -1), (2, 0), (2, 1), (2, 2),
         (3, -3), (3, -2), (3, -1), (3, 0), (3, 1), (3, 2), (3, 3)]

for lm in lmset:
    Y, theta, phi = CalcYlm(lm)
    # lとmから出力ファイル名を決める
    outfile = "l{}_m{:+d}.png".format(lm[0], lm[1])
    PlotData(Y, theta, phi, lm, outfile)
# plt.show()