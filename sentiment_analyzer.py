Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import nltk
... from sklearn.feature_extraction.text import TfidfVectorizer
... from sklearn.linear_model import LogisticRegression
... 
... # Sample dataset
... texts = [
...     "I love this product! It's amazing.",  # positive
...     "Terrible experience. Will not buy again.",  # negative
...     "It's okay, nothing special.",  # neutral
...     "Best purchase ever! Highly recommended.",  # positive
...     "Worst quality. Totally disappointed.",  # negative
... ]
... labels = [1, 0, 2, 1, 0]  # 1=positive, 0=negative, 2=neutral
... 
... # Text processing
... vectorizer = TfidfVectorizer()
... X = vectorizer.fit_transform(texts)
... 
... # Model
... model = LogisticRegression()
... model.fit(X, labels)
... 
... def predict_sentiment(review):
...     review_vec = vectorizer.transform([review])
...     pred = model.predict(review_vec)[0]
...     sentiment = {0: "Negative", 1: "Positive", 2: "Neutral"}
...     return sentiment[pred]
... 
... if __name__ == "__main__":
...     review = input("Enter a product review: ")
...     print("Predicted Sentiment:", predict_sentiment(review))
