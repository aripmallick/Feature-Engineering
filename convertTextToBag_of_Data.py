import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
df=pd.DataFrame({
    'Text': [
        'Cat are running quickly.',
        'Dogs were barking loudly!',
        'He studies in university.',
        'They are running to reach the target.'
    ]
})
print("Original DataFrame:\n", df)
vectorizer=CountVectorizer()
X=vectorizer.fit_transform(df['Text'])
bow_df=pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())
print("\nBag-of-Words Representation:\n")
print(bow_df)