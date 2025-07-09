import pandas as pd
df = pd.read_csv('example_sales.csv',encoding = 'utf-8')
print(df.head())
df = df.dropna()
df = df.drop_duplicates()
df.to_csv('clean_sales.csv',index=False,encoding='utf-8')
print(df)
