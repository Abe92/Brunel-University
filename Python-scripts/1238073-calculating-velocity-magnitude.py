# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 10:58:02 2016

@author: GS70 2PE
"""
from math import pow,sqrt

x = input("vx: ")
y = input("vy: ")
z = input("vz: ")

x = float(x)
y = float(y)
z = float(z)

powxyz = pow(x,2) + pow(y,2) + pow(z,2)
velocity = sqrt(powxyz)
    
print(velocity)