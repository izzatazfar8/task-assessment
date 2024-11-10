import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = r'C:\Users\izulhish\Downloads\Task Assessment\Bank_Marketing\bank.csv'
data = pd.read_csv(file_path)

# Group by 'education' and 'deposit' and count occurrences
education_deposit_counts = data.groupby(['education', 'deposit']).size().unstack(fill_value=0)

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))

# Stacked bar chart
bars = education_deposit_counts.plot(kind='bar', stacked=True, ax=ax, colormap='Set3')

# Title and labels
ax.set_title('Education Levels with Deposit Subscription')
ax.set_xlabel('Education Level')
ax.set_ylabel('Count')
ax.legend(title='Deposit Subscription', bbox_to_anchor=(1.05, 1), loc='upper left')

# Annotate each segment with its value
for bar in bars.patches:
    height = bar.get_height()
    width = bar.get_width()
    x_position = bar.get_x() + width / 2
    y_position = bar.get_y() + height / 2
    ax.text(x_position, y_position, f'{int(height)}', ha='center', va='center', fontsize=10)

# Adjust x-axis labels
ax.set_xticklabels(education_deposit_counts.index, rotation=45, ha='right')

plt.tight_layout()
plt.show()
