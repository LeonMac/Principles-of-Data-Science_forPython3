#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import random
import numpy as np
#import pandas as pd
from matplotlib import pyplot as plt

def normal_pdf(x, mu=0, sigma=1):
    return (1./np.sqrt(2*3.14159*sigma**2) )* 2.718**( -(x-mu)**2/(2*sigma**2) )


x_values = np.linspace(-5,5,100)
y_values = [normal_pdf(x) for x in x_values]

plt.plot(x_values, y_values)
plt.show()
'''

from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt


def normal_pdf(x, mean, sigma):
    return (1./np.sqrt(2*3.14159*sigma**2) )* 2.718**( -(x-mean)**2/(2*sigma**2) )

x=np.arange(-5,5,0.01)
mean=0
sigma=1
y=normal_pdf(x, mean, sigma)

#y=norm.pdf(x,mean,sigma)
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
'''
