#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import numpy as np

user1={"Target","Banana Republic","Old Navy"}
user2={"Banana Republic","Gap","Uno Kolo"}

def jaccard (user1, user2):

    common_set= set (user1 & user2)
    full_set = set (user1 | user2)
    print("common set= ", common_set)
    print("full set  = ", full_set)
    return len(common_set)/len(full_set)

print ("user1= ", user1)
print ("user2= ", user2)

print ("\n")

Jaccard=jaccard (user1, user2)

print ("\n")
print ("Jaccard factor= ", Jaccard)


