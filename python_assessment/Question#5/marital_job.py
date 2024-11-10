import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = r'C:\Users\izulhish\Downloads\Task Assessment\Bank_Marketing\bank.csv'
data = pd.read_csv(file_path)

# Filter data where 'deposit' is 'yes'
deposit_data = data[data['deposit'] == 'yes']

# Group by 'job' and 'marital' and count occurrences
grouped = deposit_data.groupby(['job', 'marital']).size().unstack(fill_value=0)

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))

# Stacked bar chart
grouped.plot(kind='bar', stacked=True, ax=ax, colormap='Set3')

# Title and labels
ax.set_title('Job and Marital Status of Individuals with Deposit Subscription')
ax.set_xlabel('Job Type')
ax.set_ylabel('Count of Subscribers')
ax.legend(title='Marital Status', bbox_to_anchor=(1.05, 1), loc='upper left')

# Adjust x-axis labels
ax.set_xticklabels(grouped.index, rotation=45, ha='right')

plt.tight_layout()
plt.show()
