import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = r'C:\Users\izulhish\Downloads\Task Assessment\Bank_Marketing\bank.csv'
data = pd.read_csv(file_path)

# Define the bin edges for balancee ranges
bins = [-float('inf'), 0, 1000, 5000, 10000, 20000, float('inf')]
labels = ['<0', '0-1K', '1K-5K', '5K-10K', '10K-20K', '>20K']

# Create a new column 'balance_range' to categorize the balances
data['balance_range'] = pd.cut(data['balance'], bins=bins, labels=labels)

# Count the number of occurrences in each balance range
balance_counts = data['balance_range'].value_counts().sort_index()

# Plotting with colors
plt.figure(figsize=(10, 6))
colors = ['#f2c4c4', '#f08a8a', '#e85454', '#d62222', '#b70e0e', '#900000']  
balance_counts.plot(kind='bar', color=colors, edgecolor='black')
plt.title('Distribution of Account Balances')
plt.xlabel('Balance Range')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.show()
