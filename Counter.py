# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 22:29:15 2020

@author: qtckp
"""

with open('stopwords(used).txt','r', encoding = 'utf8') as f:
    stops = [w.rstrip().lower() for w in f.readlines() if not w.startswith('#') and len(w)>1]
    stops = set(stops)



counter = {}
kk = 0
with open('word_lines.txt','r', encoding = 'utf8') as f:
    for line in f:
        arr = line.rstrip().lower().split()
        kk+=1
        for r in arr:
                   
            if r not in stops:
            
                if r in counter:
                    counter[r] += 1
                else:
                    counter[r] = 1
            
        if kk % 10000 == 0:
            print(kk)




counter2 = {k: v for k, v in sorted(counter.items(), key=lambda item: item[1])}

with open('Counts.txt','w', encoding = 'utf8') as f:
    for k, v in counter2.items():
        f.write(f'{k}  =   {v}   \n')

