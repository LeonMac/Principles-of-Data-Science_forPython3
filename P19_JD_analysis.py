#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests #used for grab data from the web

from bs4 import BeautifulSoup #used to parse HTML

from sklearn.feature_extraction.text import CountVectorizer

jd_texts =[]

for index in range(0, 30, 10):     #index from 0, 10, 20,...1000?
    page ='https://www.indeed.com/jobs?q=data+scientist&start='+str(index)
    print ("grab data from web site...", index)

    web_result = requests.get(page).text    #use requests to actually vsit the url specfied by page.

    soup=BeautifulSoup(web_result, "html.parser")

    for listing in soup.findAll('span', {'class':'summary'}):
        jd_texts.append(listing.text)

print ("Finished grab data from web site, now start anaylysis...")

type(jd_texts)
vect=CountVectorizer(ngram_range=(1,2),stop_words='english')
matrix=vect.fit_transform(jd_texts)
print (len(vect.get_feature_names()))


