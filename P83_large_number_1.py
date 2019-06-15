#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
result=[]
sum_up=0

for num_of_toss in range(1, 5000):
    toss_value=np.random.randint(low=1,high=10,size=1)
    sum_up = sum_up + toss_value
    temp= sum_up/num_of_toss
    #print (type(temp))
    mean = float (sum_up/num_of_toss)
    result.append(mean)
   # print (mean)

print ("We get ",len(result)," test data!")
print (type(result))

df=pd.DataFrame({'mean': result})
print ("The first 5 mean value are:")
print (df.head())
print ("The last 5 mean value are:")
print (df.tail())

df.plot (title=' Law of Large Numbers')
plt.xlabel ("Number of throes in sample")
plt.ylabel ("Average (mean) of samples")
plt.show()
