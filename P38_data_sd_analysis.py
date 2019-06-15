#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy

temperature=[31,32,32,31,28,29,31,38,32,31,30,29,30,31,26]

sorted_temp=sorted(temperature)
mean_temp=numpy.mean(temperature)

print ('original temperature are :',temperature)

print ('sorted temperature are :',sorted_temp)

print ('mean of temperature is: ', mean_temp)

print ('median of temperature is: ', numpy.median(temperature))

print ('\n')

sqrt_diff_list=[]

num_items=len(temperature)
product=1.


for temp in temperature:
    diff=temp-mean_temp
    sqrt_diff=diff**2
    sqrt_diff_list.append(sqrt_diff)
    average_sqrt_diff=numpy.mean(sqrt_diff_list)
    product*=temp

standard_deviation = numpy.sqrt(average_sqrt_diff)
geometric_mean = product ** (1./num_items)

print ('Standard Deviation = ',standard_deviation)
print ('\n')
print ('Geometric Mean = ',geometric_mean)

