import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = r'C:\Users\izulhish\Downloads\Task Assessment\Bank_Marketing\bank.csv'
data = pd.read_csv(file_path)

# Filter data by deposit and job counts
job_deposit_counts = data[data['deposit'] == 'yes']['job'].value_counts()

# Create a bar plot with custom colors
plt.figure(figsize=(10, 6))
bars = job_deposit_counts.plot(kind='bar', color=plt.cm.Paired(range(len(job_deposit_counts))))  

# Annotate bars values
for bar in bars.patches:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height + 5,  
             f'{int(height)}', ha='center', va='bottom', fontsize=10)

# Title and labels
plt.title('Number of Jobs with Deposit Subscription')
plt.xlabel('Job Type')
plt.ylabel('Count of Subscribers')
plt.xticks(rotation=45)
plt.show()
