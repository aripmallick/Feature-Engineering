import pandas as pd
from sklearn.preprocessing import OneHotEncoder
data={
    'Fruit':['Apple','Orange','Apple'],
    'Color':['Red','Orange','Green']
}

df=pd.DataFrame(data)
print("Original DataFrame:")            
print(df)
one_hot_encoder=OneHotEncoder(sparse_output=False)
one_hot_encoded=one_hot_encoder.fit_transform(df[['Fruit','Color']])
features_names=one_hot_encoder.get_feature_names_out(['Fruit','Color'])
df_one_hot=pd.DataFrame(one_hot_encoded,columns=features_names)

df_encoded=pd.concat([df.drop(['Fruit','Color'],axis=1),df_one_hot],axis=1)
print("After One Hot Encoding:")
print(df_encoded)