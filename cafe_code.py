import numpy as np
import pandas as pd
import os

df_raw = pd.read_csv(os.path.join('..', 'data', 'dirty_cafe_sales.csv'))
df = df_raw.copy()

def data_summary(dataframe):
    print("Data Summary:")
    print(dataframe.describe())
    print("\nMissing Values:")
    print(dataframe.isnull().sum())

print("Initial Data Summary:")
data_summary(df)

df = df.drop_duplicates()  # Remove duplicate rows

# Convert columns to appropriate data types
df[['Quantity', 'Price Per Unit', 'Total Spent']] = df[['Quantity', 'Price Per Unit', 'Total Spent']].apply(pd.to_numeric, errors='coerce')
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'], errors='coerce')

df = df[df['Item'].notna()] # Drop rows where Item is missing 

# Check if item always has a price per unit
#item_price_check = df.groupby('Item')['Price Per Unit'].nunique()

for _ in range(3):  # Iterate multiple times to ensure all missing values are imputed
    mask = df['Quantity'].isna() & df['Price Per Unit'].notna() & df['Total Spent'].notna() # missing Quantity
    df.loc[mask, 'Quantity'] = df.loc[mask, 'Total Spent'] / df.loc[mask, 'Price Per Unit']
    mask = df['Quantity'].notna() & df['Price Per Unit'].isna() & df['Total Spent'].notna() # missing Price Per Unit
    df.loc[mask, 'Price Per Unit'] = df.loc[mask, 'Total Spent'] / df.loc[mask, 'Quantity']
    mask = df['Quantity'].notna() & df['Price Per Unit'].notna() & df['Total Spent'].isna() # missing Total Spent
    df.loc[mask, 'Total Spent'] = df.loc[mask, 'Quantity'] * df.loc[mask, 'Price Per Unit']

df = df.dropna(subset=['Quantity', 'Price Per Unit', 'Total Spent']) # Drop rows where any of these are still missing


mask = df['Payment Method'].isna()
df.loc[mask, 'Payment Method'] = 'Unknown' # Impute missing Payment Method with 'Unknown'

mask = df['Location'].isna()
df.loc[mask, 'Location'] = 'Unknown' # Impute missing Location with 'Unknown'

df = df.dropna(subset=['Transaction Date']) # Drop rows where Transaction Date is missing

print("\nCleaned Data Summary:")
data_summary(df)

df.to_csv(os.path.join('..', 'data', 'clean_cafe_sales.csv'), index=False)

