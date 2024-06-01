import pandas as pd
import matplotlib.pyplot as plt
bank_data = pd.read_csv('bank_marketing1.csv')

job_counts = bank_data['job'].value_counts()

plt.figure(figsize=(10, 6))
job_counts.plot(kind='bar', color='skyblue')
plt.title('Distribution of Job Roles in Bank Marketing Dataset')
plt.xlabel('Job Roles')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
