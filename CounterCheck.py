# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 18:21:26 2020

@author: qtckp
"""

import Stemmer
stemmer = Stemmer.Stemmer('russian')

def stem(text):
    return stemmer.stemWord(text.lower())



with open('Counts.txt', 'r', encoding = 'utf8') as f:
    
    lines = f.readlines()


voc = {}
for line in lines:
    t = [ w.strip() for w in line.split('=')]
    voc[t[0]] =  int(t[1])



tot = {k: v for k, v in voc.items() if v >= 100 and v < 950000 and any((s.isalpha() for s in k))}


for mn in (100, 200, 300, 500, 1000, 2000):
    d = {k: v for k, v in voc.items() if v >= mn and v < 950000 and any((s.isalpha() for s in k))}
    print(f'{mn} --> {len(d)}')





stemmed = {}
for k, v in voc.items():
    k_new = stem(k)
    if k_new in stemmed:
        stemmed[k_new] += v
    else:
        stemmed[k_new] = v
    


for mn in (100, 200, 300, 500, 1000, 2000):
    d = {k: v for k, v in stemmed.items() if v >= mn and v < 950000 and any((s.isalpha() for s in k))}
    print(f'{mn} --> {len(d)}')



tot = {k: v for k, v in stemmed.items() if v >= 1000 and v < 950000 and any((s.isalpha() for s in k))}







with open('вводные слова русские.txt', 'r', encoding = 'utf8') as f:
    
    lines = [line.strip() for line in  f.readlines() if len(line)>2]



st = set()
for line in lines:
    words = set([stem(w) for w in line.split()])
    st = st.union(words)



# убираю вводные слова - это -250 слов

tot = {k: v for k, v in stemmed.items() if k not in st and v >= 1000 and v < 950000 and any((s.isalpha() for s in k))}



with open('Stemms1000.txt','w', encoding = 'utf8') as f:
    for k in tot.keys():
        f.write(f'{k}\n')











