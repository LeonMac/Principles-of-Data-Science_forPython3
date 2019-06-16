#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import numpy as np
#import pandas as pd
from matplotlib import pyplot as plt

def random_dice_roll():
    return random.randint(1,6)


trials_list=[]
std_deviation_tmp=0.0

num_trials=100
for trial in range(num_trials):
    trials_list.append (random_dice_roll())

avg=sum(trials_list)/float(num_trials)

print ('the trail list is shown as below:\n',trials_list)
print ('the avergae dice roll point = ',avg)

for trial in range(num_trials):
    std_deviation_tmp+=(trials_list[trial]-avg)**2

std_deviation=(std_deviation_tmp/(num_trials-1))**0.5

print ("\nnote: you shall be careful for the stdandard deviation calculation, bias (/n) or non-bias (/n-1)!!")
print ('my calculated stdandard deviation (non-bias,/n-1) = ',std_deviation)
print ('use numpy lib to calculate standard deviation directly (non-bias,/n-1) = ', np.std(trials_list, ddof=1))


# another version, calculate standard deviation for various data list.

'''
num_trials=range(100,1000,10)
avgs_list=[]
std_dev_list=[]
std_deviation=0.0

for num_trial in num_trials:
    trials_list=[]
    for trial in range(1,num_trial):
        trials_list.append (random_dice_roll())
        print(trial)
        avg=sum(trials_list)/float(num_trial)
    avgs_list.append (avg)
    print (trials_list)

    for trial in range(1,num_trial):
        print(trial, trials_list[trial])
        std_deviation+=(trials_list[trial]-avg)**2

    std_deviation=std_deviation/(num_trial-1)
    std_dev_list.append (std_deviation)

plt.plot(num_trials, avgs)
plt.xlabel('Number of Trials')
plt.ylabel('Average')
plt.show()
'''
