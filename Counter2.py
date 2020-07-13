# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 19:07:15 2020

@author: qtckp
"""

import Stemmer
stemmer = Stemmer.Stemmer('russian')

def stem(text):
    return stemmer.stemWord(text.lower())



with open('Stemms1000.txt','r', encoding = 'utf8') as f:
    stops = [word.rstrip() for word in f.readlines()]
    stops = set(stops) # in по множеству где-то в 200+ раз быстрее



counter = {k: 0 for k in stops}
kk = 0
with open('word_lines.txt','r', encoding = 'utf8') as f:
    
    for line in f:
        
        arr = line.rstrip().lower().split()
        
        kk += 1
        
        new = {}
        
        for r in arr:
            
            rr = stem(r)
            
            if rr in stops:
                            
                counter[rr] += 1
                
                if rr in new:
                    new[rr] +=1
                else:
                    new[rr] = 1
        
        for k, v in new.items():
            if v>5:
                del counter[k]
                stops.discard(k)
                
            
        if kk % 10000 == 0:
            print(kk)




counter2 = {k: v for k, v in sorted(counter.items(), key=lambda item: item[1])}

print(f'lenght = {len(stops)}')

with open('Counts2.txt','w', encoding = 'utf8') as f:
    for k, v in counter2.items():
        f.write(f'{k}  =   {v}   \n')




