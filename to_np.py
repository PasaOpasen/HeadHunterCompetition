# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 20:28:47 2020

@author: qtckp
"""


import numpy as np
import gc
from numba import jit
from scipy import sparse

import Stemmer
stemmer = Stemmer.Stemmer('russian')


def stem(text):
    return stemmer.stemWord(text)



with open('Counts2.txt', 'r', encoding = 'utf8') as f:
    
    lines = f.readlines()


voc = {}
for line in lines:
    t = [ w.strip() for w in line.split('=')]
    voc[t[0]] =  int(t[1])

stops = set(voc.keys())



    

arr_ = [] #np.array([False for _ in range(len(stops))])
    
kk = 0
    
with open('word_lines.txt','r', encoding = 'utf8') as f:
        
    for line in f:
            
        kk += 1
            
        tmp = set((stem(r) for r in line.rstrip().lower().split()))
            
            #arr_.append([word in tmp for word in stops])
            #arr_ = np.vstack((arr_, ))
        arr_.append(np.array([word in tmp for word in stops]))                            
                    
        if kk % 10000 == 0:
            print(kk)
                #gc.collect()
            
            if kk % 100000 == 0:
                
                mat = sparse.csr_matrix(np.vstack(arr_))
                sparse.save_npz(f'X3955_{kk//100000}.npz', mat)
                arr_ = []
                
                # with open(f'X3955_{kk/100000}.npy', 'wb') as f:
                #     np.save(f, np.vstack(arr_))
                #     arr_ = []
                



mat = sparse.csr_matrix(np.vstack(arr_))

sparse.save_npz(f'X3955_{30}.npz', mat)








