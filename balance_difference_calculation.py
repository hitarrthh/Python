import pandas as pd
df = pd.read_csv('bank_marketing.csv')
subscribed_clients_no = df[df['deposit'] == 'no']  
subscribed_clients_yes = df[df['deposit'] == 'yes']  
sum_no = subscribed_clients_no['balance'].sum()  
sum_yes = subscribed_clients_yes['balance'].sum()  
result = sum_yes - sum_no
print("Balance in EUROS for people who have Subscribed to deposit: ",sum_yes)
print("Balance in EUROS for people who have not Subscribed to deposit: ",sum_no)
print("Difference in Balance(in EUROS):", result)
