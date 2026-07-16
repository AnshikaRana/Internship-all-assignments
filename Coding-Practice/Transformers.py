from transformers import pipeline

classifier = pipeline("sentiment-analysis")

result1 = classifier("The class was very boring.")
print("\nResult 1:", result1)

result2 = classifier("The class is very interesting.")
print("\nResult 2:",result2)

classifier = pipeline(task="sentiment-analysis", model="SamLowe/roberta-base-go_emotions", top_k=None)
result3 = classifier("The class is very boring.")
print("\nResult 3:",result3)

sentence_list = ["Hello, how are you?",
                 "I am happy but also sad.",
                 "Are you still here?"]

result4 = classifier(sentence_list)
print("\nResult 4:",result4)

#TEXT GENERATION PIPELINE

text_generator = pipeline("text-generation", model = "distilbert/distilgpt2")
generated_text = text_generator("Today is a rainy day in Delhi.", truncation= True, num_return_sequences=2)
print("\nGenerated Text: ", generated_text[0]["generated_text"])

#NAMED ENTITY RECOGNITION
ner = pipeline("ner")
result5 = ner ("Google is hiring interns in America, India, Taj Mahal, Food, Apple")
print(result5)

#TOKENIZE
from transformers import AutoTokenizer, DistilBertTokenizer
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')

text = "Hello, How are you?"
tokens = tokenizer.tokenize(text)
token_ids = tokenizer.convert_tokens_to_ids(tokens)

print("Tokens:", tokens, "(Using DistilBert Tokenizer)")
print("Token IDs:", token_ids, "(Using DistilBert Tokenizer)")

from transformers import RobertaTokenizer
tokenizer2 = RobertaTokenizer.from_pretrained('roberta-base')

text = "Hello, How are you?"
tokens1 = tokenizer2.tokenize(text)
token_ids1 = tokenizer2.convert_tokens_to_ids(tokens1)

print("Tokens:", tokens1, "(Using Roberta Tokenizer)")
print("Token IDs:", token_ids1, "(Using Roberta Tokenizer)")

from transformers import GPT2Tokenizer
tokenizer3 = GPT2Tokenizer.from_pretrained('gpt2')

text = "Hello, How are you?"
tokens2 = tokenizer3.tokenize(text)
token_ids2 = tokenizer3.convert_tokens_to_ids(tokens2)

print("Tokens:", tokens2, "(Using GPT2 Tokenizer)")
print("Token IDs:", token_ids2, "(Using GPT2 Tokenizer)")

tokenizer4 = AutoTokenizer.from_pretrained('bert-base-uncased')

text = "Hello, How are you?"
tokens3 = tokenizer4.tokenize(text)
token_ids3 = tokenizer4.convert_tokens_to_ids(tokens2)

print("Tokens:", tokens3, "(Using Bert Base Tokenizer)")
print("Token IDs:", token_ids3, "(Using Bert Base Tokenizer)")