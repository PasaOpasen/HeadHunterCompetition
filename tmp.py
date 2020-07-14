# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 15:46:39 2020

@author: qtckp
"""

words = np.array(list(stops))

sl = X[y[:,0].toarray().flatten(),:]

for i in range(50):
    print(words[sl[i,:].toarray().flatten()])
