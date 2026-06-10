import numpy as np
import pandas as pd
import os

# Loading the raw data
df_raw = pd.read_csv(os.path.join('data_files', 'dirty_cafe_sales.csv'))
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

# Drop rows where Item is missing or ERROR (print count of error values before dropping) - section commented out as it may be better to impute missing Item values 
# rather than drop them, depending on the analysis goals
# error_count = df[df['Item'] == 'ERROR'].shape[0]
#print(f"Number of ERROR values in Item column: {error_count}")
# df = df[df['Item'].notna()]
# df = df[df['Item'] != 'ERROR']

Item_Prices = {
    1.0: 'Cookie',
    1.5: 'Tea',
    2.0: 'Coffee',
    5.0: 'Salad',
    # 3.0 and 4.0 are ambiguous, so we omit them
}

# Check for missing or ERROR values in Item column before imputation
item_mask = (df['Item'].isna() | df['Item'].str.upper().isin(['ERROR', 'UNKNOWN']))
print(f"Number of missing or ERROR values in Item column: {item_mask.sum()}") # 969 values

# Impute mapping to fix missing Item values and then replace missing values with 'Unknown'
item_fix = item_mask & df['Price Per Unit'].isin(Item_Prices.keys())
df.loc[item_fix, 'Item'] = df.loc[item_fix, 'Price Per Unit'].map(Item_Prices)
df['Item'] = df['Item'].fillna('UNKNOWN')
df['Item'] = df['Item'].replace('ERROR', 'UNKNOWN')

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

# Impute missing Payment Method with 'Unknown' + Replace ERROR values
df['Payment Method'] = df['Payment Method'].fillna('UNKNOWN') 
df['Payment Method'] = df['Payment Method'].replace('ERROR', 'UNKNOWN')

# Impute missing Location with 'Unknown' + Replace ERROR values
df['Location'] = df['Location'].fillna('UNKNOWN')
df['Location'] = df['Location'].replace('ERROR', 'UNKNOWN')

# Drop rows where Transaction Date is missing
df = df.dropna(subset=['Transaction Date']) 

# Print cleaned data summary
print("\nCleaned Data Summary:")
data_summary(df)

# Save the cleaned data to a new CSV file
df.to_csv(os.path.join('data_files', 'clean_cafe_sales.csv'), index=False)

