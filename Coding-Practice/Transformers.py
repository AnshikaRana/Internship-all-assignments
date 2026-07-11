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

