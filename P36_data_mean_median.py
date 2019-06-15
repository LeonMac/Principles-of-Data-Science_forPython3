#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy

original_data=[5,4,3,4,5,3,2,5,3,2,1,4,5,3,4,4,5,4,2,1,4,5,4,3,2,4,4,5,4,3,2,1]

sorted_data=sorted(original_data)

print ('original data are :',original_data)

print ('sorted data are :',sorted_data)

print ('mean of data is: ', numpy.mean(original_data))

print ('median of data is: ', numpy.median(original_data))
