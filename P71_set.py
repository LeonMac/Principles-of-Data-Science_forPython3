#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import numpy as np

list = ([1, 2, 2, 3, 5, 2,3,1,4,6])

s=set(list)
length_s=len(s)

print ("set list is: ", s)
print ("length of set : ",length_s)

print ("\n")

dict = {"dog":"human's best friend", "cat": "wonderer of the world"}

print ("Check dict, the dgog is:",end=" "), print (dict["dog"])

print ("length of cat is:",end=" "), print (len(dict["cat"]))
