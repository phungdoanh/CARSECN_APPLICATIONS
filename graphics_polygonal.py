#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 11:26:49 2022

@author: namnguyen
"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib as mpl
import copy

x=[0.1,0.3,0.3,0.1]
y=[0.1,0.1,0.3,0.3]


def polygonal_graphics(x,y):

    fig, ax = plt.subplots()
    
    
    trapezoid = patches.Polygon(xy=list(zip(x,y)), fill=False)
    ax.add_patch(copy.copy(trapezoid))
    
    t_start = ax.transData
    t = mpl.transforms.Affine2D().rotate_deg(0)
    t_end = t + t_start
    
    trapezoid.set_transform(t_end)
    ax.add_patch(trapezoid)
    
    plt.show()
    
    
polygonal_graphics(x, y)
