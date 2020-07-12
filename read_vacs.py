# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 16:05:10 2020

@author: qtckp
"""




import json
import pandas as pd


def read_vacancies_part(part):
    with open(f'vacancies-{part:02}.json', 'r', encoding = 'utf8') as fp:
        return json.loads(fp.read())


v1 = read_vacancies_part(1)



