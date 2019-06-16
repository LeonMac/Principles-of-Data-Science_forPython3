#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import random
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

friends = [109, 1017, 1127, 418, 625, 957, 89, 950, 946, 797, 981, 125, 455, 731, 1640, 485, 1309, 472, 1132, 1773, 906, 531, 742, 621]

happiness = [.8, .6, .3, .6, .6, .4, .8, .5, .4, .3, .3, .6, .2, .8, 1, .6, .2, .7, .5, .3, .1, 0, .3, 1]


mean                   =np.mean(friends)
median                 =np.median(friends)
max                    =np.max(friends)
min                    =np.min(friends)
range_fr               =np.max(friends)-np.min(friends)
standard_deviation_bias=np.std(friends)
standard_deviation_nonbias=np.std(friends, ddof=1)
variance               =np.var(friends)
covariance             =np.cov(friends)

item_number=len(friends)

#------------------------------#

print ("use the numpy for data processing...\n")
print ("total ",item_number," items.\n")
print ("the mean of the friends = ",mean ,"\n")

print ("the median of the friends = ",median ,"\n")

print ("the max of the friends = ",max,"\n")

print ("the min of the friends = ",min,"\n")

print ("the range of the friends = ",range_fr,"\n")

print ("the standard deviation of the friends (bias) = ",standard_deviation_bias,"\n")

print ("the standard deviation of the friends (non-bias) = ",standard_deviation_nonbias,"\n")

print ("the variance of the friends = ",variance,"\n")

print ("calculate the sqrt of variance =", variance**0.5, "\n")

print ("the covariance of the friends = ",covariance,"\n")

print ("calculate the sqrt of covariance =", covariance**0.5, "\n")

y_pos=range(len(friends))

z_scores_list=[]
for friend in friends:
    z_temp=(friend-mean)/standard_deviation_bias
    z_scores_list.append(z_temp)

#------------------------------#
print ("the plot to show the mean and standard deviation","\n")

print ("the plot to show the Z-Score result","\n")

plt.figure()
plt.subplot(2, 1, 1)    # (#of row, #of col, index)

plt.bar (y_pos, friends)
plt.xlabel ("Sample Index")
plt.ylabel ("Friends number")
plt.title  ("the chat to show the friends statisic result")
plt.grid(True)

plt.plot ((0,item_number), (mean,mean), 'b-',label= "mean")          #mean
plt.plot ((0,item_number), (mean+standard_deviation_nonbias,mean+standard_deviation_nonbias), 'g-', label="mean+std_dev")  #mean+std_dev
plt.plot ((0,item_number), (mean-standard_deviation_nonbias,mean-standard_deviation_nonbias), 'r-', label="mean-std_dev" )  #mean-std_dev

plt.legend()

plt.subplot(2, 1, 2)
plt.bar (y_pos, z_scores_list)
plt.xlabel ("Sample Index")
plt.ylabel ("Z-Score result")
plt.title  ("the chat to show the Z-Score")
plt.grid(True)

plt.plot ((0,item_number), (0,0), 'b-',label= "mean")          #mean
plt.plot ((0,item_number), (1,1), 'g-', label="mean+1*sigma")  #mean+std_dev
plt.plot ((0,item_number), (-1, -1), 'r-', label="mean-1*sigma" )  #mean-std_dev

plt.legend()    # this is neccesary for lebel of each line to show.

plt.show()
