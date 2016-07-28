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
print (xy)

plt.plot(xy[:,0], xy[:,1], label='blood flow')

plt.xlabel('steps')
plt.ylabel('mean pressure')
plt.title('hemeLB output')
plt.legend()
plt.show()

