import pandas as pd 

data={
    'A': [1, 2, 3, None, 5],
    'B': [None,2,3,4,5],
    'C': [1,2,None,None,5]
}

df= pd.DataFrame(data)
print("Original Dataset:\n",df)
print()

df.fillna(0, inplace=True)
print("Data after filling with zero:\n",df)