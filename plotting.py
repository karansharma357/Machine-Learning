# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 21:47:31 2018

@author: Karan Sharma
"""
import numpy as np
import matplotlib.pyplot as plt
# plotting a line
x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))

# scatter-plot points
x = np.random.normal(size=500)
y = np.random.normal(size=500)
plt.scatter(x, y)

# showing images
x = np.linspace(1, 12, 100)
y = x[:, np.newaxis]

im = y * np.sin(x) * np.cos(y)
print(im.shape)
# imshow - note that origin is at the top-left by default!
plt.imshow(im)
# Contour plot - note that origin here is at the bottom-left by default!
plt.contour(im)

