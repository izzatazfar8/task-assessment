import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Load the dataset
data = pd.read_csv('C:/Users/izulhish/Downloads/Task Assessment/credit_card_complaints.csv')

# Filter out rows with missing data
data_filtered = data[['state', 'issue', 'submitted_via', 'date_received', 'company']].dropna()

# Convert date_received to datetime
data_filtered['date_received'] = pd.to_datetime(data_filtered['date_received'])

# Count complaints by state and issue
complaints_by_state_issue = data_filtered.groupby(['state', 'issue']).size().reset_index(name='count')

# Identify the most common complaint for each state
most_common_complaints = complaints_by_state_issue.loc[complaints_by_state_issue.groupby('state')['count'].idxmax()]
most_common_complaints = most_common_complaints.sort_values(by='count', ascending=True)

# Full state names
state_full_names = {
    'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas', 'CA': 'California',
    'CO': 'Colorado', 'CT': 'Connecticut', 'DE': 'Delaware', 'FL': 'Florida', 'GA': 'Georgia',
    'HI': 'Hawaii', 'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana', 'IA': 'Iowa',
    'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana', 'ME': 'Maine', 'MD': 'Maryland',
    'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota', 'MS': 'Mississippi', 'MO': 'Missouri',
    'MT': 'Montana', 'NE': 'Nebraska', 'NV': 'Nevada', 'NH': 'New Hampshire', 'NJ': 'New Jersey',
    'NM': 'New Mexico', 'NY': 'New York', 'NC': 'North Carolina', 'ND': 'North Dakota', 'OH': 'Ohio',
    'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania', 'RI': 'Rhode Island', 'SC': 'South Carolina',
    'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah', 'VT': 'Vermont',
    'VA': 'Virginia', 'WA': 'Washington', 'WV': 'West Virginia', 'WI': 'Wisconsin', 'WY': 'Wyoming'
}

# Replace state abbreviations with full names
most_common_complaints['state_full'] = most_common_complaints['state'].replace(state_full_names)

# 1st Graph: Number of Complaints by State
plt.figure(figsize=(14, 8))
sns.barplot(data=most_common_complaints, y='state_full', x='count', hue='issue', palette='Set2', dodge=False)
plt.title('No. of Complaints by State')
plt.xlabel('Number of Complaints')
plt.ylabel('State')
plt.legend(title='Complaint Type')
plt.tight_layout()
plt.show()

# 2nd Graph: Number of Complaints by Issue

total_complaints_by_issue = data_filtered['issue'].value_counts().reset_index()
total_complaints_by_issue.columns = ['issue', 'count']

# Bar plot with annotations 
plt.figure(figsize=(16, 8))  
sns.barplot(data=total_complaints_by_issue, x='issue', y='count', palette='viridis', hue='issue', dodge=False)
plt.title('No. of Complaints by Issue')
plt.xlabel('Issue')
plt.ylabel('Number of Complaints')

plt.xticks(rotation=45, ha='right')  
plt.subplots_adjust(bottom=0.2)  

for index, row in total_complaints_by_issue.iterrows():
    plt.text(x=index, y=row['count'] + 100, s=row['count'], ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.show()

# 3rd Graph: Complaints by Submission Platform (Pie chart)
submission_counts = data_filtered['submitted_via'].value_counts()
explode = [0.2 if label in ['email', 'fax'] else 0 for label in submission_counts.index]

plt.figure(figsize=(12, 8))
plt.pie(submission_counts, labels=submission_counts.index, autopct='%1.1f%%', startangle=90,
        explode=explode, labeldistance=1.15, wedgeprops={'linewidth': 0, 'edgecolor': 'black', 'linestyle': 'solid'})  # Adjust labeldistance
plt.text(0, -1.3, 'Complaints by Submission Platform', ha='center', va='center', fontsize=16, fontweight='bold')
plt.axis('equal')
plt.tight_layout()  
plt.show()

# 4th Graph: Complaints Over Year
complaints_over_time = data_filtered.resample('YE', on='date_received').size().reset_index(name='count')

plt.figure(figsize=(14, 8))
sns.lineplot(data=complaints_over_time, x='date_received', y='count', marker='o')
plt.title('Number of Complaints Over Year')
plt.xlabel('Year')
plt.ylabel('Number of Complaints')

# Annotate each point on the line
for x, y in zip(complaints_over_time['date_received'], complaints_over_time['count']):
    plt.text(x, y + 50, s=y, ha='center', va='bottom', fontsize=10, fontweight='bold')
plt.xticks(rotation=45)
plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%Y'))
plt.tight_layout()
plt.show()

# 5th Graph: Scatter Plot for Complaints by Top 20 Companies 
company_issue_counts = data_filtered.groupby(['company', 'issue']).size().reset_index(name='count')
total_complaints_by_company = company_issue_counts.groupby('company')['count'].sum().reset_index()
top_20_companies = total_complaints_by_company.nlargest(20, 'count')
top_20_company_issues = company_issue_counts[company_issue_counts['company'].isin(top_20_companies['company'])]
top_20_company_issues = top_20_company_issues.sort_values(by='count', ascending=False)

plt.figure(figsize=(14, 8))
sns.scatterplot(data=top_20_company_issues, x='company', y='count', hue='issue', style='issue', markers='o', s=100)
plt.xticks(rotation=45, ha='right')
plt.title('Complaints by Top 20 Companies with Their Issues', fontsize=16)
plt.xlabel('Company', fontsize=14)
plt.ylabel('Number of Complaints', fontsize=14)
plt.legend(title='Issue Type', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# KPI 
total_complaints = data_filtered.shape[0]
total_issues = data_filtered['issue'].nunique()
total_companies = data_filtered['company'].nunique()
most_complaints_issue = data_filtered['issue'].value_counts().idxmax()
highest_complaints_year = data_filtered['date_received'].dt.year.value_counts().idxmax()
most_complaints_company = data_filtered['company'].value_counts().idxmax()

plt.figure(figsize=(12, 8))

# Total Complaints Recorded
plt.subplot(3, 2, 1)
plt.title("Total Complaints Recorded", fontsize=14)
plt.gca().add_patch(Rectangle((0, 0), 1, 1, color='lightblue', alpha=0.5))
plt.text(0.5, 0.5, f"{total_complaints}", fontsize=30, ha='center', va='center')
plt.xticks([])
plt.yticks([])

# Total Issue Recorded
plt.subplot(3, 2, 2)
plt.title("Number of Credit Card Issues", fontsize=14)
plt.gca().add_patch(Rectangle((0, 0), 1, 1, color='lightblue', alpha=0.5))
plt.text(0.5, 0.5, f"{total_issues}", fontsize=30, ha='center', va='center')
plt.xticks([]) 
plt.yticks([])

# Total Companies Involved
plt.subplot(3, 2, 3)
plt.title("Total Companies Involved", fontsize=14)
plt.gca().add_patch(Rectangle((0, 0), 1, 1, color='lightcoral', alpha=0.5))
plt.text(0.5, 0.5, f"{total_companies}", fontsize=30, ha='center', va='center')
plt.xticks([])
plt.yticks([])

# Most Complaints 
plt.subplot(3, 2, 4)
plt.title("Most Complaints by Issue", fontsize=14)
plt.gca().add_patch(Rectangle((0, 0), 1, 1, color='lightpink', alpha=0.5))
plt.text(0.5, 0.5, most_complaints_issue, fontsize=20, ha='center', va='center')
plt.xticks([])
plt.yticks([])

# Year with Highest Complaints
plt.subplot(3, 2, 5)
plt.title("Year with Highest Complaints", fontsize=14)
plt.gca().add_patch(Rectangle((0, 0), 1, 1, color='lightyellow', alpha=0.5))
plt.text(0.5, 0.5, f"{highest_complaints_year}", fontsize=20, ha='center', va='center')
plt.xticks([])
plt.yticks([])

# Company with Most Complaints
plt.subplot(3, 2, 6)
plt.title("Company with Most Complaints", fontsize=14)
plt.gca().add_patch(Rectangle((0, 0), 1, 1, color='lightgray', alpha=0.5))
plt.text(0.5, 0.5, f"{most_complaints_company}", fontsize=20, ha='center', va='center')
plt.xticks([])
plt.yticks([])

plt.tight_layout()
plt.show()