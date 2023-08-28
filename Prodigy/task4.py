import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# Load the CSV file containing Twitter data
csv_path = 'twitter_training.csv'  # Replace with the actual path
data = pd.read_csv(csv_path)

# Perform sentiment analysis using TextBlob
def get_sentiment(tweet):
    analysis = TextBlob(tweet)
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'

data['Sentiment'] = data['Tweet'].apply(get_sentiment)

# Plot sentiment distribution
sentiment_counts = data['Sentiment'].value_counts()
plt.bar(sentiment_counts.index, sentiment_counts)
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.title('Sentiment Distribution')
plt.show()
