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