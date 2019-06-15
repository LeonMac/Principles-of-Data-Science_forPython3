#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import CountVectorizer

# grab postings from the web
texts = []

for i in range(0,100,10): # cycle through 100 pages of indeed job resources

    soup = BeautifulSoup(requests.get('http://www.indeed.com/jobs?q=data+scientist&start='+str(i)).text,'html.parser')
    print ("Reading the web messge, range index=", i)
    #print(soup.prettify())
    texts += [a.text for a in soup.findAll('span', {'class':'summary'})]
    #print(texts)

#print (type(texts))

print(texts)
#print (texts[10])   # first job description

#<type 'list'>

vect = CountVectorizer(ngram_range=(1,2), stop_words='english')
# make a count vectorizer to get basic counts

matrix = vect.fit_transform(texts)
# fit and learn to the vocabulary in the corpus

print (len(vect.get_feature_names()))  # how many features are there

freqs = [(word, matrix.getcol(idx).sum()) for word, idx in vect.vocabulary_.items()]
#sort from largest to smallest

for phrase, times in sorted (freqs, key = lambda x: -x[1])[:25]:
    print (phrase, times)
