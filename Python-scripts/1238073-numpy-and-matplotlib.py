# -*- coding: utf-8 -*-
"""
Author: Aldy Rasyid Abe

Source: sentdex-youtube (https://pythonprogramming.net/loading-file-data-matplotlib-tutorial/)

Improved by: Derek Groen
"""

import matplotlib.pyplot as plt
import csv
import numpy as np

xy = np.zeros([0,2])

with open ('D:/Python/In/ID-and-average-pressure/step_and_pressure.txt','r') as csvfile:
    plots = csv.reader(csvfile)
    for row in plots:
        xy = np.vstack([xy,[float(row[0]), float(row[1])]])
        #xy = np.vstack([xy,[float(row[0]), float(row[1]), float(row[2]), float(row[3]), float(row[4]), float(row[5]), float(row[6]), float(row[7])]])
print (xy)

#magnitudes = np.sqrt(xy[:,4]*xy[:,4] + xy[:,5]*xy[:,5] + xy[:,6]*xy[:,6])

plt.plot(xy[:,0], xy[:,1], label='blood flow')

plt.xlabel('steps')
plt.ylabel('mean pressure')
plt.title('hemeLB output')
plt.legend()
plt.show()

