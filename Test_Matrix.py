#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

x=np.array([3,6,8])

y=np.array([4,7,0])

multi=x*y
add =x+y
sub =x-y

dot =x.dot(y)
dot_1=y.dot(x)
cross=np.cross(x,y)
cross_1=np.cross(y,x)

print ('x   =      ',x)
print ('y   =      ',y)
print ('\n')
print ('x+y =      ',add)
print ('x-y =      ',sub)
print ('x*y =      ',multi)
print ('\n')
print ('x.y =      ',dot)
print ('y.x =      ',dot_1)
print ('xXy =      ',cross)
print ('yXx =      ',cross_1)
