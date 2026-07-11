from transformers import pipeline

classifier = pipeline("sentiment-analysis")

result = classifier("The class was very boring.")
print(result)