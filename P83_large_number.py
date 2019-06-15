#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
result=[]

for num_of_toss in range(1, 10000):
    toss_value=np.random.randint(low=1,high=10,size=num_of_toss)
    mean=toss_value.mean()
    result.append(mean)

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
