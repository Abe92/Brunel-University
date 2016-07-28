# -*- coding: utf-8 -*-
"""
Calculating velocity vector (_magnitude_)
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
