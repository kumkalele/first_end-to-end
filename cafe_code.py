import numpy as np
import pandas as pd
import os

# Loading the raw data
df_raw = pd.read_csv(os.path.join('data', 'dirty_cafe_sales.csv'))
df = df_raw.copy()

# Initial data exploration
def data_summary(dataframe):
    print("Data Summary:")
    print(dataframe.describe())
    print("\nMissing Values:")
    print(dataframe.isnull().sum())

print("Initial Data Summary:")
data_summary(df)

# Remove duplicate rows
df = df.drop_duplicates() 

# Convert columns to appropriate data types
df[['Quantity', 'Price Per Unit', 'Total Spent']] = df[['Quantity', 'Price Per Unit', 'Total Spent']].apply(pd.to_numeric, errors='coerce')
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'], errors='coerce')

# Drop rows where Item is missing 
df = df[df['Item'].notna()]

# Calculate missing values for Quantity, Price Per Unit, and Total Spent
for i in range(3):  # Iterate three times to ensure all missing values are imputed
    mask_quantity = (
        df['Quantity'].isna() 
        & df['Price Per Unit'].notna() 
        & df['Total Spent'].notna()
    ) # missing Quantity
    
    df.loc[mask_quantity, 'Quantity'] = df.loc[mask_quantity, 'Total Spent'] / df.loc[mask_quantity, 'Price Per Unit']

    mask_price = (
        df['Quantity'].notna() 
        & df['Price Per Unit'].isna() 
        & df['Total Spent'].notna()
    ) # missing Price Per Unit

    df.loc[mask_price, 'Price Per Unit'] = df.loc[mask_price, 'Total Spent'] / df.loc[mask_price, 'Quantity']

    mask_total = (
        df['Quantity'].notna() 
        & df['Price Per Unit'].notna() 
        & df['Total Spent'].isna()
    ) # missing Total Spent

    df.loc[mask_total, 'Total Spent'] = df.loc[mask_total, 'Quantity'] * df.loc[mask_total, 'Price Per Unit']

# Drop rows where any of these are still missing
df = df.dropna(subset=['Quantity', 'Price Per Unit', 'Total Spent']) 

# Impute missing Payment Method with 'Unknown'
df['Payment Method'] = df['Payment Method'].fillna('Unknown') 

# Impute missing Location with 'Unknown'
df['Location'] = df['Location'].fillna('Unknown')

# Drop rows where Transaction Date is missing
df = df.dropna(subset=['Transaction Date']) 

# Print cleaned data summary
print("\nCleaned Data Summary:")
data_summary(df)

# Save the cleaned data to a new CSV file
df.to_csv(os.path.join('data', 'clean_cafe_sales.csv'), index=False)

