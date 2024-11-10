import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Load dataset
file_path = r'C:\Users\izulhish\Downloads\Task Assessment\Bank_Marketing\bank.csv'
data = pd.read_csv(file_path)

# Calculate KPIs
# 1. Customer Demographics
mean_age_subscribers = data[data['deposit'] == 'yes']['age'].mean()
mean_age_non_subscribers = data[data['deposit'] == 'no']['age'].mean()

# 2. Financial Standing
mean_balance_subscribers = data[data['deposit'] == 'yes']['balance'].mean()
balance_range_high_sub = data[data['deposit'] == 'yes']['balance'].describe()[['min', 'max']]
loan_effects = data.groupby('loan')['deposit'].value_counts(normalize=True).unstack().fillna(0)['yes']

# 3. Subscription by Category
job_subscription_rate = data.groupby('job')['deposit'].value_counts(normalize=True).unstack().fillna(0)['yes']
marital_subscription_rate = data.groupby('marital')['deposit'].value_counts(normalize=True).unstack().fillna(0)['yes']
education_subscription_rate = data.groupby('education')['deposit'].value_counts(normalize=True).unstack().fillna(0)['yes']

# 4. Marketing Effectiveness
contact_conversion_rate = data.groupby('contact')['deposit'].value_counts(normalize=True).unstack().fillna(0)['yes']
previous_campaign_effect = data.groupby('poutcome')['deposit'].value_counts(normalize=True).unstack().fillna(0)['yes']
day_conversion_rate = data.groupby('day')['deposit'].value_counts(normalize=True).unstack().fillna(0)['yes']

# 5. Risk Indicators
default_effects = data.groupby('default')['deposit'].value_counts(normalize=True).unstack().fillna(0)['yes']
housing_effects = data.groupby('housing')['deposit'].value_counts(normalize=True).unstack().fillna(0)['yes']

# Plotting the KPIs
fig = plt.figure(figsize=(15, 10))

# 1. Average Age of Subscribers 
plt.subplot(3, 4, 1)
plt.title("Average Age of Subscribers", fontsize=12)
plt.gca().add_patch(Rectangle((0, 0), 1, 1, color='lightblue', alpha=0.5))
plt.text(0.5, 0.5, f"{mean_age_subscribers:.2f}", fontsize=10, ha='center', va='center')
plt.xticks([])  
plt.yticks([])

# 2. Average Balance of Subscribers ($)
plt.subplot(3, 4, 2)
plt.title("Average Balance of Subscribers ($)", fontsize=12)
plt.gca().add_patch(Rectangle((0, 0), 1, 1, color='salmon', alpha=0.5))
plt.text(0.5, 0.5, f"${mean_balance_subscribers:,.2f}", fontsize=10, ha='center', va='center')
plt.xticks([])  
plt.yticks([])

# 3. Loan Effects on Subscription
plt.subplot(3, 4, 5)
plt.title("Loan Effects on Subscription", fontsize=12)
plt.gca().add_patch(Rectangle((0, 0), 1, 1, color='peachpuff', alpha=0.5))
plt.text(0.5, 0.5, loan_effects.to_string(float_format='{:.2%}'.format), fontsize=8, ha='center', va='center')
plt.xticks([])  
plt.yticks([])

# 4. Contact Conversion Rate
plt.subplot(3, 4, 10)
plt.title("Contact Conversion Rate", fontsize=12)
plt.gca().add_patch(Rectangle((0, 0), 1, 1, color='lavender', alpha=0.5))
plt.text(0.5, 0.5, contact_conversion_rate.to_string(float_format='{:.2%}'.format), fontsize=8, ha='center', va='center')
plt.xticks([])  
plt.yticks([])

# 5. Default Loan Effects on Subscription
plt.subplot(3, 4, 9)
plt.title("Default Effects on Subscription", fontsize=12)
plt.gca().add_patch(Rectangle((0, 0), 1, 1, color='lightcoral', alpha=0.5))
plt.text(0.5, 0.5, default_effects.to_string(float_format='{:.2%}'.format), fontsize=8, ha='center', va='center')
plt.xticks([])  
plt.yticks([])

# 6. Housing Loan Effects on Subscription
# Calculate subscription rate based on housing loan status
housing_effects = data.groupby('housing')['deposit'].value_counts(normalize=True).unstack().fillna(0)['yes']

# Housing Loan Effects on Subscription
plt.subplot(3, 4, 6)
plt.title("Housing Loan Effects on Subscription", fontsize=12)
plt.gca().add_patch(Rectangle((0, 0), 1, 1, color='mistyrose', alpha=0.5))
plt.text(0.5, 0.5, housing_effects.to_string(float_format='{:.2%}'.format), fontsize=8, ha='center', va='center')
plt.xticks([])  
plt.yticks([])

# layout
plt.tight_layout()
plt.show()
