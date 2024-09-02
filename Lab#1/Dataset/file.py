import pandas as pd

df = pd.read_csv('RealEstateDataset.csv', sep=';', on_bad_lines='skip')
df.head()