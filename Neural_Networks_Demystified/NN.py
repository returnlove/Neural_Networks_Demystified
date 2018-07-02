# -*- coding: utf-8 -*-

import numpy as np

X = np.array(([3,5],[5,1],[10,2]), dtype = float)
y = np.array(([75],[82],[93]), dtype = float)


print(np.amax(X, axis = 0))

#scaling inputs and ouput
X = X/np.amax(X, axis = 0)
y = y/100