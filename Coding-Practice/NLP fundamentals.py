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


#STEMMING