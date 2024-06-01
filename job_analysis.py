import pandas as pd
df = pd.read_csv('bank_marketing.csv')
unique_job_levels = df['job'].nunique()
print("Count of unique job levels:", unique_job_levels)
management_clients = df[df['job'] == 'Management']  
num_management_clients = len(management_clients)
print("Number of clients in the management level:", num_management_clients)