#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sklearn import preprocessing
#import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

friends = [109, 1017, 1127, 418, 625, 957, 89, 950, 946, 797, 981, 125, 455, 731, 1640, 485, 1309, 472, 1132, 1773, 906, 531, 742, 621]

happiness = [.8, .6, .3, .6, .6, .4, .8, .5, .4, .3, .3, .6, .2, .8, 1, .6, .2, .7, .5, .3, .1, 0, .3, 1]

df= pd.DataFrame ({'friends':friends, 'happiness':happiness})
print("create data frame from friends and happiness: \n",df.head(),"\n")
print("do correlation between friends and happiness: \n",df.corr(),"\n")

df_scaled = pd.DataFrame(preprocessing.scale(df), columns = ['friends_scaled','happiness_scaled']) #put two arrays into one data set.

print("after data scaled: \n",df_scaled.head(),"\n")

print("do correlation between scaled data frame: \n",df_scaled.corr(),"\n")

print("anaysis the standard deviation distribution result...\n")

within_1std=df_scaled[(df_scaled['friends_scaled']<=1)&(df_scaled['friends_scaled']>=-1)].shape[0]
within_1std_percent=within_1std/float(df_scaled.shape[0])

within_2std=df_scaled[(df_scaled['friends_scaled']<=2)&(df_scaled['friends_scaled']>=-2)].shape[0]
within_2std_percent=within_2std/float(df_scaled.shape[0])

within_3std=df_scaled[(df_scaled['friends_scaled']<=3)&(df_scaled['friends_scaled']>=-3)].shape[0]
within_3std_percent=within_3std/float(df_scaled.shape[0])

print("within_1std =",within_1std,"  percent=",within_1std_percent)
print("within_2std =",within_2std,"  percent=",within_2std_percent)
print("within_3std =",within_3std,"  percent=",within_3std_percent,"\n")

print("the chat to show the scaled friends and happiness data distribution!\n")

df_scaled.plot(kind='scatter', x= 'friends_scaled', y='happiness_scaled')

plt.show()

