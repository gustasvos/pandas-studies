import os
import pandas as pd
import numpy as np

# fileNames is a list with the names of the csv files contained in the 'dataset' path

filenames = []

for f in os.listdir('data'):
    if f.endswith('.csv'):
        filenames.append(f)

# reads the file from the filenames list and turns into a df

def createDf(fname):
    path = 'data/' + fname
    df = pd.read_csv(path, sep=';')
    return df

df = [createDf(file) for file in filenames]
dfTotal = pd.concat(df, ignore_index=True)

print (dfTotal.head())
print (dfTotal.tail())
