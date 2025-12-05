import re
import string

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')
nltk.download('stopwords')
data = [
    ("I really loved this movie! It was fantastic and very engaging.", "positive"),
    ("What a waste of time. The plot was boring and too predictable.", "negative"),
    ("An amazing performance by the lead actor. Great story.", "positive"),
    ("I did not enjoy the movie. It was too long and not entertaining.", "negative"),
    ("One of the best films I have seen this year. Brilliant!", "positive"),
    ("Terrible movie. I want my time back.", "negative"),
]
texts, labels = zip(*data)
def preprocess_text(text):
    text = text.lower()
    text = re.sub(f"[{re.escape(string.punctuation)}]", "", text)
    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t not in stopwords.words('english')]
    return " ".join(tokens)
clean_texts = [preprocess_text(t) for t in texts]
X_train, X_test, y_train, y_test = train_test_split(clean_texts, labels, test_size=0.3, random_state=42)
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)
clf = MultinomialNB()
clf.fit(X_train_vec, y_train)
y_pred = clf.predict(X_test_vec)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification report:\n", classification_report(y_test, y_pred))
new_reviews = [
    "I absolutely loved the story and the acting was superb.",
    "It was a horrible experience — I hated every minute of it.",
    "Not bad, but could be better.",
    "What an incredible film! A must watch.",
    "The movie was disappointing and way too slow."
]
new_reviews_clean = [preprocess_text(r) for r in new_reviews]
new_vec = vectorizer.transform(new_reviews_clean)
predictions = clf.predict(new_vec)
for review, pred in zip(new_reviews, predictions):
    print(f"Review: {review}\nPredicted sentiment: {pred}\n")