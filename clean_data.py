# import all necessary libraries

import pandas as pd

# Load dataset

data = pd.read_csv('C:\\Users\\laksh\\Downloads\\customer_personality_analysis\\customer_personality _analysis.csv', sep = '\t')
print("shape:", data.shape)
print("columns:", data.columns)
print("data types:", data.dtypes)
print(data.head())

# Standardize column names

data.columns = data.columns.str.lower().str.replace(' ', '_')
print("Columns:", data.columns.tolist())

# Check for missing values
    
missing_values = data.isnull().sum()
print("Missing values:", missing_values)

# Handle missing values

median_income = data['income'].median()
data['income'] = data['income'].fillna(median_income)
print("Missing values after filling:", data.isnull().sum())

# Remove duplicates

data = data.drop_duplicates()
print("Shape after removing duplicates:", data.shape)

# Convert Date columns to datetime format

data['dt_customer'] = pd.to_datetime(data['dt_customer'], format='%d-%m-%Y')

# Fix Data Types

data['income'] = data['income'].astype(float)
data['year_birth'] = data['year_birth'].astype(int)

# Standardize text values

print("\nMarital status :", data['marital_status'].unique())
data['marital_status'] = data['marital_status'].replace({
    'Alone': 'Single',
    'Absurd': 'Single',
    'YOLO': 'Single',
    'Together': 'Married',})

print("\nMarital status :", data['marital_status'].unique())

# Save cleaned data to a new CSV file

data.to_csv("cleaned_customer_personality_analysis.csv", index=False)




