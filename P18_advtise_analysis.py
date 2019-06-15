#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import seaborn as sns


# %matplotlib inline
data = pd.read_csv('http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv', index_col=0)
head=data.head()

print (head)

print (data)

sns.set(style="ticks", color_codes=True)
g=sns.pairplot (data, x_vars=["TV","radio","newspaper"], y_vars="sales") #, height=4.5, aspect=0.7)

import matplotlib.pyplot as plt
plt.show()
