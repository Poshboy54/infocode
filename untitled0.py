# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 10:33:07 2019

@author: Anton Bree
"""
# Package imports
import time
start=time.time()
import numpy as np

import astropy.io.fits as imp

#----------------------------------------------------------------
# Data reader function

def column(X,cn):
    Y=np.empty(len(X))
    for i in range(0,len(X)):
        Z=X[i]
        Y[i]=Z[cn]
    return Y

def columnlist(X,cn):
    Y=['empty']*len(X)
    for i in range(0,len(X)):
        Z=X[i]
        Y[i]=Z[cn]
    return Y
#----------------------------------------------------------------



# Import Data File
total=imp.open('G3CMockGalv06.fits')

W=(total['TilingCat'].data)

cols = total[1].columns

cols.names