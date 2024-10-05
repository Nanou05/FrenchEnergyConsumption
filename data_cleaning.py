# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 20:36:25 2024

@author: Nanou05
"""
import pandas as pd

# load the data 

data = pd.read_csv("consommation-regionale-gnc.csv", delimiter=';')

def data_cleaning(data):
   
    data['date'] = pd.to_datetime(data['annee'], format='%Y')
    
    data['consommation_gwh_pcs'] = pd.to_numeric(data['consommation_gwh_pcs'].replace(',','.'))
    
    data = data.dropna()
    
    return data

data = data_cleaning(data)


data.to_csv('consommation-regionale-cleaned.csv')