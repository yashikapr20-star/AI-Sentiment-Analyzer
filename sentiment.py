from textblob import TextBlob

print("===== AI Sentiment Analyzer =====")

text = input("Enter a sentence: ")

analysis = TextBlob(text)
polarity = analysis.sentiment.polarity

print("\nPolarity Score:", polarity)

if polarity > 0:
    print("Sentiment: Positive 😊")
elif polarity < 0:
    print("Sentiment: Negative 😞")
else:
    print("Sentiment: Neutral 😐")