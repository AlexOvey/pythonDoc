import pylab 
from numpy import cos,linspace, pi, sin, random
from scipy.interpolate import splprep, splev
import numpy as np

# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 21:13:40 2018

@author: alex
"""
t = linspace(0, 1.75*2*pi, 100)

x = sin(t)
y = cos(t)
z = t

#add noise
x += random.normal(scale=0.1, size =x.shape)
y += random.normal(scale=0.1, size=y.shape)
z += random.normal(scale=0.1, size=z.shape)

smoothness = 3.0 #smoothness parameter
k_param = 2 #splince order
nests = -1 #estimate of number of knot needed(-1 =maximal)
# find the knot points
knot_points, u =splprep([x, y, z], s=smoothness, k=k_param, nests=-1)
# evaluate spline, including interpolated points
xnew, ynew, znew = splev(linspace(0, 1, 400), knot_points)

# plot result

pylab.subplot(2,2,1)
data, = pylab.plot(x, y, 'bo-', label='Data with X-Y Cross section')
fit, = pylab.plot(xnew, ynew, 'r-', labels='Fit with X-Y Cross Section')
pylab.legend()
pylab.xlabel('X')
pylab.ylabel('Y')

pylab.subplot(2, 2, 1)
data, =pylab.plot(x,z, 'bo-', label ='Data with X-Z Cross Section')
fit, = pylab.plot(xnew, znew, 'r-', labels='Fit with X-Z Cross Section')
pylab.legend()
pylab.xlabel('X')