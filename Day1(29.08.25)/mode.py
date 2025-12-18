import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

data={
    'Name' : ['Ram', 'Shyam', 'Mohan', 'Sohan', 'Ramesh', 'Suresh', 'Raju', 'Vijay'],
    'Age' : [64, 26, 39, np.nan, 38, 42, np.nan, 42],
    'Height' : [192, np.nan, 135, 142, np.nan, 197, 161, 146],
    'Weight' : [68, np.nan, 75, 70, 82, 57, 43, np.nan],
    'Grade' : ['A', 'B', np.nan, 'D', 'C', 'A', np.nan, 'B']
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

imputer = SimpleImputer(strategy='most_frequent')
df_imputed = pd.DataFrame(imputer.fit_transform(df[['Name', 'Age', 'Height', 'Weight', 'Grade']]), columns=['Name', 'Age', 'Height', 'Weight', 'Grade'])

df['Name'] = df_imputed['Name']
df['Age'] = df_imputed['Age']
df['Height'] = df_imputed['Height']
df['Weight'] = df_imputed['Weight']
df['Grade'] = df_imputed['Grade']
print("\nAfter Mode Imputation:")
print(df)
