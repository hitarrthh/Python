import pandas as pd
df = pd.read_csv('bank_marketing.csv')
subscribed_clients = df[df['deposit'] == 'yes']  
average_age_subscribed = subscribed_clients['age'].mean()  
print("Average age of clients who have subscribed to a deposit:", average_age_subscribed)
