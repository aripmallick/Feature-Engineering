import pandas as pd 

data={
    'A': [1, 2, 3, None, 5],
    'B': [None,2,3,4,5],
    'C': [1,2,None,None,5]
}

df= pd.DataFrame(data)
print("Original Dataset:\n",df)
print()

df_cleaned=df.dropna()

print("Cleaned Dasta:\n",df_cleaned)