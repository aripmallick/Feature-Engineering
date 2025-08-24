import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

data={
    'Age' : [35, np.nan, 31, 67, 59],
    'Testscore' : [85, 90, np.nan, 78, 92],
    'Grade' : ['A', 'B', np.nan, 'C', 'A']
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

imputer = SimpleImputer(strategy='mean')
df_imputed = pd.DataFrame(imputer.fit_transform(df[['Age', 'Testscore']]), columns=['Age', 'Testscore'])

df['Age'] = df_imputed['Age']
df['Testscore'] = df_imputed['Testscore']
print("\nAfter Mean Imputation:")
print(df)
