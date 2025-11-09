import pandas as pd 

data={
    'A': [1, 2, 2, 3, 3, 4,],
    'B': [5, 6, 6, 7, 8, 8],
}

df= pd.DataFrame(data)
print("Original DataFrame:\n",df.to_string(index=False))
print("\nDuplicates Rows:\n",df[df.duplicated()].to_string(index=False))

df.drop_duplicates(subset=['A'],keep='first',inplace=True)

print("\nDataFrame after removing duplicates based on column 'A':\n",df.drop_duplicates().to_string(index=False))