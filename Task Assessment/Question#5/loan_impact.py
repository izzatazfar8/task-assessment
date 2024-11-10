import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = r'C:\Users\izulhish\Downloads\Task Assessment\Bank_Marketing\bank.csv'
data = pd.read_csv(file_path)

# Default, housing loan, and personal loan effects on deposit subscription in stacked format
default_counts = data.groupby(['default', 'deposit']).size().unstack()
housing_counts = data.groupby(['housing', 'deposit']).size().unstack()
loan_counts = data.groupby(['loan', 'deposit']).size().unstack()

# Plotting all three in a single figure with subplots
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

# Default loan
default_counts.plot(kind='bar', stacked=True, ax=axs[0], color=['orange', 'lightgreen'])
axs[0].set_title('Effect of Default on Deposit Subscription')
axs[0].set_xlabel('Default Status')
axs[0].set_ylabel('Count')

# Housing Loan
housing_counts.plot(kind='bar', stacked=True, ax=axs[1], color=['orange', 'lightgreen'])
axs[1].set_title('Effect of Housing Loan on Deposit Subscription')
axs[1].set_xlabel('Housing Loan Status')

# Personal Loan
loan_counts.plot(kind='bar', stacked=True, ax=axs[2], color=['orange', 'lightgreen'])
axs[2].set_title('Effect of Personal Loan on Deposit Subscription')
axs[2].set_xlabel('Personal Loan Status')

plt.tight_layout()
plt.show()
