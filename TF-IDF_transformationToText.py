import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
df=pd.DataFrame({
    'Text': [
        'Cat are running quickly.',
        'Dogs were barking loudly!',
        'He studies in university.',
        'They are enjoying the holidays.'
    ]
})
print("Original DataFrame:\n", df)
tfidf=TfidfVectorizer()
X=tfidf.fit_transform(df['Text'])
tfidf_df=pd.DataFrame(X.toarray(), columns=tfidf.get_feature_names_out())
print("\nBag-of-Words Representation:\n")
print(tfidf_df)