import pandas as pd
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt_tab')
df=pd.DataFrame({
    'Text': [
        'Cat are running quickly.',
        'Dogs were barking loudly!',
        'He studies in university.',
        'They are enjoying thee holidays.'
    ]
})
print("Original DataFrame:\n", df)
stremmer=PorterStemmer()
def stem_text(text):
    tokens=word_tokenize(text.lower())
    stems=[stremmer.stem(word) for word in tokens if word.isalpha()]
    return ' '.join(stems)
df["Stemmed_Text"]=df['Text'].apply(stem_text)
print("\nAfter Stemming:\n")
print(df[['Text','Stemmed_Text']])