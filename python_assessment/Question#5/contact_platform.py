import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt

# Load the dataset
file_path = r'C:\Users\izulhish\Downloads\Task Assessment\Bank_Marketing\bank.csv'
data = pd.read_csv(file_path)

# Count occurrences of each contact type
contact_counts = data['contact'].value_counts()

# function to format the labels
def func(pct, allvals):
    absolute = int(pct / 100.*np.sum(allvals))
    return f"{absolute} ({pct:.1f}%)"

# Plotting
plt.figure(figsize=(8, 6))
plt.pie(contact_counts, labels=contact_counts.index, autopct=lambda pct: func(pct, contact_counts), startangle=140)
plt.title('Contact Platform Distribution')
plt.show()
