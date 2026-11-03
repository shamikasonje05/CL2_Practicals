import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
'''
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')'''

text = """ Natural Language Processing is a field of Artificial Intelligence.It helps computers understand and process human language."""

print("Original Text:")
print(text)

words = word_tokenize(text)

words = [word.lower() for word in words]

words = [word for word in words if word.isalnum()]

stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word not in stop_words]

print("\nAfter Stop Word Removal:")
print(filtered_words)

stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in filtered_words]

print("\nAfter Stemming:")
print(stemmed_words)