import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = r'C:\Users\izulhish\Downloads\Task Assessment\Bank_Marketing\bank.csv'
data = pd.read_csv(file_path)

# Calculate percentage of deposit subscription
deposit_counts = data['deposit'].value_counts()
plt.figure(figsize=(8, 6))
plt.pie(deposit_counts, labels=deposit_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Percentage of Deposit Subscription (Yes and No)')
plt.show()
