import pandas as pd
df = pd.read_csv('bank_marketing.csv')
subscribed_clients = df[df['deposit'] == 'no']  
contacts = subscribed_clients['contact'].count()  
campaign = subscribed_clients['campaign'].sum()  
print("Total number of contact who have subscribed not to a deposit:", contacts)
print("Total number of campaign conducted who have subscribed not to a deposit:", campaign)
