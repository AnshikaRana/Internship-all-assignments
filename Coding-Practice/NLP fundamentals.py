#NLP Fundamentals

#Text Cleaning

#1 Text Lowercasing
text = "I Love Machine Learning and NLP"
print (text.lower())

#2 Removing Punctuation
import string
text1 = "Hello!! How have you been?"
text1 = text1.translate(str.maketrans('', '', string.punctuation))
print(text1)

#3 Removing Numbers
import re #regular expression library
text2 = "NLP 101 is very easy at 1st"
text2 = re.sub(r'\d+', '', text2)
print(text2)

#4 Text Tokenization
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
nltk.download("punkt_tab") #download tokenizer model

text3 = "NLP is amazing and easy to learn"
print(word_tokenize(text3))

#5 Stopwords Removal
from nltk.corpus import stopwords
nltk.download("stopwords")

stop_words = set(stopwords.words("english"))
#print(stop_words) 
tokens1 = word_tokenize("Nlp is easy for beginners")
print(tokens1) 
print([w for w in tokens1 if w not in stop_words])

#6 Stemming
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
print(stemmer.stem("running"))
print(stemmer.stem("studies"))
print(stemmer.stem("gaming"))

words = ['playing', 'played', 'plays']
print([stemmer.stem(w) for w in words])

#7 Lemmatization
from nltk.stem import WordNetLemmatizer
nltk.download("wordnet")
lemmatizer = WordNetLemmatizer()
words1 = ['playing', 'studies', 'jumps']
print([lemmatizer.lemmatize(w) for w in words1])

#Word level One-Hot Encoding
import numpy as np
vocab = ["ai", "data", "learning", "nlp"]

def one_hot(word, vocab):
    vector = np.zeros(len(vocab))
    
    if word in vocab:
        vector[vocab.index(word)] = 1

    return vector

for word in vocab:
    print(word, "-", one_hot(word, vocab))

#Document Level One-Hot Encoding
from sklearn.feature_extraction.text import CountVectorizer
sentences = ['I Love NLP', 'I love AI']

vectorizer = CountVectorizer(binary=True) 

x = vectorizer.fit_transform(sentences)
print(vectorizer.get_feature_names_out())
print(x.toarray())

#Bag of Words
vectorizer = CountVectorizer()
sentence = ['I love love NLP. I also love pizza', 'I love AI. AI is also easy']
X = vectorizer.fit_transform(sentence)

print(vectorizer.get_feature_names_out())
print(X.toarray())