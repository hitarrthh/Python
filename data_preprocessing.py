import pandas as pd
df = pd.read_csv('bank_marketing.csv')
df.drop('Unnamed: 0', axis=1, inplace=True)
df.dropna(inplace=True)  
df.drop_duplicates(inplace=True)
shape_after_processing = df.shape
print("Shape of the data after dropping 'Unnamed: 0', handling missing values, and removing duplicates:", shape_after_processing)
