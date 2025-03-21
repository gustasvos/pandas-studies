import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# apenas estudos

# reads the csv and creates 2 dataframes
filename = 'data/dataset/EXP_2024_MUN.csv'
df = pd.read_csv(filename, sep=';')
df2 = df.tail()
df = df.head()

print(df, '\n')
print(df2, '\n')

# concatenates and reset the index so it keeps counting
frames = [df, df2]
result = pd.concat(frames, ignore_index=True)
print(result)

frames = []