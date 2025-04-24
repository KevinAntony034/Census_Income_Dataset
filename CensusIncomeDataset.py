# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample dataset structure based on the provided example
# Load the Census Income dataset (replace with your file path)
data = pd.read_csv(r"C:\Users\OMEN\Downloads\CensusIncomeDataset\census_income_dataset.csv")

# Ensure column names are properly stripped of whitespace
data.columns = data.columns.str.strip()

# Task 1: Age Distribution of Respondents
plt.figure(figsize=(10, 6))
plt.hist(data['AGE'], bins=20, color='slateblue')
#sns.histplot(data['AGE'], bins=20, kde=True, color='blue')
plt.title("Age Distribution of Respondents", fontsize=16)
plt.xlabel("Age", fontsize=14)
plt.ylabel("Frequency", fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()

# Task 2: Frequency of Each Relationship Status as a Pie Chart
plt.figure(figsize=(8, 6))
relationship_counts = data['RELATIONSHIP'].value_counts()
plt.pie(
    relationship_counts.values, 
    labels=relationship_counts.index, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=sns.color_palette("muted", len(relationship_counts))
)
plt.title("Relationship Status Frequency", fontsize=16)
plt.show()

# Task 3: Respondents' Salary (<=50k or >50k) by Educational Level
data['SALARY_GROUP'] = data['SALARY'].apply(lambda x: 0 if x.strip() == '<=50K' else 1)  # Group salary
education_salary = data.groupby(['EDUCATION', 'SALARY_GROUP']).size().unstack(fill_value=0)

# Stacked Bar Chart
education_salary.plot(kind='bar', stacked=True, figsize=(10, 8), color=["forestgreen", "slateblue"])
plt.title("Salary Among Different Educational Levels", fontsize=10)
plt.xlabel("Education Level", fontsize=10)
plt.ylabel("Count", fontsize=10)
plt.xticks(rotation=20, fontsize=9)
plt.yticks(fontsize=10)
plt.legend(['<=50K', '>50K'], title="Salary", fontsize=12)
plt.show()