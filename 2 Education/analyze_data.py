import pandas as pd
import numpy as np

# Read the CSV file
df = pd.read_csv('General_Education_School.csv')

# Remove the first row which contains column descriptions
df = df.iloc[1:].reset_index(drop=True)

# Convert percentage columns to numeric values
percentage_columns = ['Parent Response Rate', 'Teacher Response Rate', 'Student Response Rate']
for col in percentage_columns:
    df[col] = df[col].str.rstrip('%').astype('float') / 100

# Convert score columns to numeric
score_columns = ['Total Safety and Respect Score', 'Total Communication Score', 
                'Total Engagement Score', 'Total Academic Expectations Score']
for col in score_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

print("\nData Types of Each Column:")
print("-" * 50)
print(df.dtypes)

print("\nChecking for Duplicate Rows:")
print("-" * 50)
duplicates = df.duplicated()
num_duplicates = duplicates.sum()
print(f"Number of duplicate rows: {num_duplicates}")

if num_duplicates > 0:
    print("\nDuplicate Rows:")
    print(df[duplicates]) 