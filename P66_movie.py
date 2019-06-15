#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

user_fever_explain=np.array(['comic', 'love', 'act', 'war'])
user_fever=np.array([5 ,1 , 3, 4])

movie1_egen=np.array([3, 2, 3,1])
movie2_egen=np.array([5, 5, 1,3])

relevant_1 = user_fever.dot(movie1_egen)
relevant_2 = user_fever.dot(movie2_egen)

print ('user_fever   =      ',user_fever_explain)
print ('\n')
print ('movie1_egen  =      ',movie1_egen)
print ('movie1 relevant score = ',relevant_1)
print ('movie2_egen  =      ',movie2_egen)
print ('movie2 relevant score = ',relevant_2)
print ('\n')


if relevant_1>relevant_2 :
    print ("movie1 is the better choice!")
elif relevant_1<relevant_2 :
    print ("movie2 is the better choice!")
elif relevant_1==relevant_2 :
    print ("either movie1 or movie2 is good for you!")
