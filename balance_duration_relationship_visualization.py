import pandas as pd
import matplotlib.pyplot as plt
bank_data = pd.read_csv('bank_marketing1.csv')
plt.figure(figsize=(8, 6))
plt.scatter(bank_data['balance'], bank_data['duration'], color='skyblue', alpha=0.5)
plt.title('Relationship between Account Balance and Last Contact Duration')
plt.xlabel('Account Balance')
plt.ylabel('Last Contact Duration')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
