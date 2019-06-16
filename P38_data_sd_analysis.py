#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

temperature=[31,32,32,31,28,29,31,38,32,31,30,29,30,31,26]

sorted_temp=sorted(temperature)
mean_temp=np.mean(temperature)

print ('original temperature are :',temperature)

print ('sorted temperature are :',sorted_temp)

print ('mean of temperature is: ', mean_temp)

print ('median of temperature is: ', np.median(temperature))

print ('\n')

diff_squre_list=[]

num_items=len(temperature)
product=1.

print ('=======method-1 to calculate standard deviation, step by step=======')

for temp in temperature:
    diff=temp-mean_temp
    diff_squre=diff**2
    diff_squre_list.append(diff_squre)
    average_diff_squre=np.mean(diff_squre_list)
    product*=temp

standard_deviation = np.sqrt(average_diff_squre)
geometric_mean = product ** (1./num_items)

print ('Standard Deviation (bias, /n) = ',standard_deviation)

print ('Geometric Mean = ',geometric_mean)

print ('=======method-2 to calculate standard deviation, using numpy directly =======')

print ('Standard Deviation (bias, /n) = ',np.std(temperature))
