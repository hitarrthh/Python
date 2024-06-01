import pandas as pd
import matplotlib.pyplot as plt
bank_data = pd.read_csv('bank_marketing1.csv')
plt.figure(figsize=(8, 6))
plt.hist(bank_data['age'], bins=20, color='skyblue', edgecolor='black')  
plt.title('Age Distribution of Individuals')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
