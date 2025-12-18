import pandas as pd
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('omw-1.4')
df=pd.DataFrame({
    'Text': [
        'Cat are running quickly.',
        'Dogs were barking loudly!',
        'He studies in university.',
        'They are enjoying thee holidays.'
    ]
})
print("Original DataFrame:\n", df)
lemmatizer=WordNetLemmatizer()
def lemmatize_text(text):
    tokens=word_tokenize(text.lower())
    lemmas=[lemmatizer.lemmatize(word) for word in tokens if word.isalpha()]
    return ' '.join(lemmas)
df["Lemmatized_Text"]=df['Text'].apply(lemmatize_text)
print("\nAfter Lemmatization:\n")
print(df[['Text','Lemmatized_Text']])