import os
import pandas as pd
import numpy as np
import glob
file_path="C:/Orange_Buick_2022-12-1"

files = os.path.join("C:/Orange_Buick_2022-12-1", "Orange_Buick_GLChartOfAccountsTable_202*.csv")
files = glob.glob(files)
df = pd.concat(map(pd.read_csv, files), ignore_index=True)
#print(df)
fa_df = df.drop_duplicates(subset = 'GLAccount', keep= 'last')
fa_df = fa_df[['GLAccount','AccountNumber','AccountDescription','AccountType','Department']].reset_index()
fa_df['Drill1'] = 'Income'
fa_df['AccountType'].unique()
fa_df.loc[fa_df['AccountType'] == 1, 'Drill1'] = 'Assets'
fa_df.loc[fa_df['AccountType'] == 2, 'Drill1'] = 'Liabilities'
fa_df[fa_df['AccountType'] == 1]
fa_df['Alloc'] = 1
list_of_columns = ['Drill2', 'Drill3', 'Drill4', 'Drill5', 'Business', 'Sales-COS', 'Type', 'Negative', 'Dormant', 'Sort_Order']
for i in list_of_columns:
    fa_df[i] = np.nan
fa_df['Dormant'] = 'N'
fa_df['Negative'] = 1
fa_df = fa_df.drop(['AccountType'], axis=1)
fa_df = fa_df.rename(columns ={'AccountNumber':'GLAccount_input','AccountDescription':'Description'})
fa_df = fa_df[['GLAccount', 'GLAccount_input', 'Description', 'Drill1',
           'Drill2', 'Drill3', 'Drill4', 'Drill5', 'Alloc', 'Business', 'Department',
           'Sales-COS', 'Type', 'Negative', 'Dormant', 'Sort_Order']]
fa_df = fa_df.sort_values(by=['Drill1', 'GLAccount_input'])
print(fa_df)
