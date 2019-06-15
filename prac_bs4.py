#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests import get
from pattern.web import plaintext
url = 'http://sethgodin.typepad.com/seths_blog/2016/11/the-yeasayer.html'
htmlString = get(url).text
webText = plaintext(htmlString)
length=len(webText)
print(length)
