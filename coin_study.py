#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import time

user_fever_explain=np.array(['comic', 'love', 'act', 'war'])
user_fever=np.array([5 ,1 , 3, 4])

movie_egen_matrix=np.random.randint(5,size=(4,100))+1

movie_recommend=np.dot(user_fever,movie_egen_matrix)

print ('user_fever_matrix shape is: ',user_fever.shape)

print ('user_fever   =      ',user_fever_explain)
print ('\n')
print ('movie set egen  =      \n',movie_egen_matrix)
print ('\n')
print ('movie_egen_matrix shape is: ',movie_egen_matrix.shape)
print ('user_fever_matrix shape is: ',user_fever.shape)
print ('\n')
print ('movie recommand list : \n',movie_recommend)


print ('\n')

for num_of_movie in (100,1000,10000,100000, 1000000,10000000):
    movie_egen_matrix=np.random.randint(5,size=(4,num_of_movie))+1
    time_start=time.time()
    np.dot(user_fever,movie_egen_matrix)
    print ('It takes ',time.time()-time_start,' seconds to do ',num_of_movie, 'correlation calculate!')
