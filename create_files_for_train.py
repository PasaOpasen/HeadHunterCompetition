# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 13:37:29 2020

@author: qtckp
"""


import json
import numpy as np
from scipy import sparse

mats = [sparse.load_npz(f'X3955_{i}.npz') for i in range(1,31)]


X = sparse.vstack(mats)




with open('test_begin.json','r',encoding = 'utf8') as f:
    test = json.load(f)

with open('train_labels.json','r',encoding = 'utf8') as f:
    train = json.load(f)





train_labs = [int(k)-1 for k in train.keys()]
test_labs = [int(k)-1 for k in test.keys()]




X_train = X[train_labs,:]
X_test = X[test_labs, :]


sparse.save_npz(f'X3955_train.npz', X_train)
sparse.save_npz(f'X3955_test.npz', X_test)







st = set()
for v in train.values():
    st = st.union(set(v))


Y = sparse.vstack(
    [sparse.csr_matrix(np.array([w in set(v) for w in st])) for v in train.values()]
    )



















