import pandas as pd


#Return a new Data Frame with no empty cells:
df = pd.read_csv('data.csv')
new_df = df.dropna()
print(new_df.to_string())


#Remove all rows with NULL values
df = pd.read_csv('data.csv')
df.dropna(inplace = True)
print(df.to_string())