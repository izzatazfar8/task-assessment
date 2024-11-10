import squarify
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = r'C:\Users\izulhish\Downloads\Task Assessment\Bank_Marketing\bank.csv'
data = pd.read_csv(file_path)

# Calculate counts of each job type
job_counts = data['job'].value_counts()

# Prepare labels
labels = [f'{job}\n{count}' for job, count in zip(job_counts.index, job_counts.values)]

# Create the squarify plot
plt.figure(figsize=(12, 8))
squarify.plot(sizes=job_counts.values, label=labels, alpha=0.8)
plt.title('Number of Jobs')
plt.axis('off')
plt.show()
