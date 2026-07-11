from transformers import pipeline

classifier = pipeline("sentiment-analysis")

result = classifier("The class was very boring.")
print(result)

result1 = classifier("The class is very interesting.")
print(result1)

classifier = pipeline(task="sentiment-analysis", model="SamLowe/roberta-base-go_emotions", top_k=None)
result2 = classifier("The class is very boring.")
print(result2)

sentence_list = ["Hello, how are you?",
                 "I am happy but also sad.",
                 "Are you still here?"]

result3 = classifier(sentence_list)
print(result3)

#TEXT GENERATION PIPELINE