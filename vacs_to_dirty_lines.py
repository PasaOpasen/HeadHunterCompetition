# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 18:32:37 2020

@author: qtckp
"""



import json
import pandas as pd


def read_vacancies_part(part):
    with open(f'vacancies-{part:02}.json', 'r', encoding = 'utf8') as fp:
        return json.loads(fp.read())


#v1 = read_vacancies_part(1)



def it_or_space(char):
    if char.isalnum():
        return char
    return ' '



with open('dirty_lines.txt','w', encoding = 'utf8') as f:
    for i in range(1,11):
        print(f'i = {i}')
        dic = read_vacancies_part(i)
        print('dic is ready')
        for k, d in enumerate(dic.values()):
            line = d['description'] + ' ' + ' '.join(d['key_skills']) + ' ' + d['name']
            #line = str([it_or_space(c) for c in line])
            #line = ' '.join(line.split())
            f.write(line+'\n')
            
            if k % 10000 == 0:
                print(k)







with open('word_lines.txt','w', encoding = 'utf8') as f:
    with open('dirty_lines.txt','r', encoding = 'utf8') as f0:
        for  k, line in enumerate(f0.readlines()):
            ln = ''.join([it_or_space(c) for c in line.strip()])
            ln = ' '.join(ln.split())
            f.write(ln+'\n')
            
            if k % 100000 == 0:
                print(k)






























