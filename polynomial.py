import pandas as pd
from sklearn.preprocessing import PolynomialFeatures

#sample datset with two columns
data=pd.DataFrame({
    'X1':[2,4,6,3,5],
    'X2':[3,5,7,8,10]
})
print("Original Data:")
print(data)
#create polynomial+interaction features
poly = PolynomialFeatures(degree=2, include_bias=False)
poly_features = poly.fit_transform(data)
#get feature names
feature_names=poly.get_feature_names_out(['X1','X2'])
poly_df=pd.DataFrame(poly_features, columns=feature_names)
print("\nPolynomial and Interaction Features:") 
print(poly_df)