# Task Assessment - Python Analytics

This repository contains analytical scripts to explore and visualize datasets related to bank and credit card complaints, as well as bank marketing data. The goal is to derive insights through various analytic techniques and present visual summaries.

## Datasets

### Question 4: Bank and Credit Card Complaints
- **Scripts**: `Q4_1_bank_complaint_analytic.py` and `Q4_2_credit_card_complaint_analytic.py`
- **Source**: [Bank and Credit Card Complaints on Kaggle](https://www.kaggle.com/datasets/mexwell/bank-and-credit-card-complaints)

### Question 5: Bank Marketing Dataset
- **Script**: `Question#5_bank_marketing_analytic.py`
- **Source**: [Bank Marketing Dataset on Kaggle](https://www.kaggle.com/datasets/janiobachmann/bank-marketing-dataset)

## Dependencies

Make sure to install the following dependencies:
```bash
pip install pandas matplotlib seaborn


===== Usage =====
Clone the repository:
git clone https://github.com/izzatazfar8/task-assessment.git
Edit CSV Paths
Update the file paths in each script to match the location of your dataset files:

Edit path for the dataset:
data = pd.read_csv("path/to/your_dataset.csv")

Run the script :
python Q4_1_bank_complaint_analytic.py
python Q4_2_credit_card_complaint_analytic.py

For Question5, run each of the python script :
Example : python kpi.py
