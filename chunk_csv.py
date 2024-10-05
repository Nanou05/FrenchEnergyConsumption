# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 20:14:45 2024

@author: Nanou05
"""

import pandas as pd


def chunk_csv(file_path, chunk_size, delimiter=';'):
    chunk_n = 1
    for chunk in pd.read_csv(file_path, chunksize=chunk_size, delimiter=delimiter):
        chunk.to_csv(f'file_chunk{chunk_n}.csv', index=False)
        chunk_n += 1

chunk_csv("consommation-regionale-gnc.csv", 5)
    

