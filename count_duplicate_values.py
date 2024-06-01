import pandas as pd
dd = pd.read_csv('bank_marketing.csv')
duplicate = dd.duplicated().sum()
print("TOTAL NUMBER OF DUPLICATE VALUES ARE: ",duplicate)