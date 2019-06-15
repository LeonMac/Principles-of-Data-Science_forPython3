#!/usr/bin/env python
# -*- coding: utf-8 -*-

tweet_msg="RT @robdv: $TWTR now top holding for Andor, unseating $AAPL"

words_in_tweet= tweet_msg.split(' ') # split tweet messge to word
for word in words_in_tweet:            #for loop
    if "$" in word:
       print ("This Tweet is about", word)

