import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = {
    'Date': ['2023-08-01', '2023-08-02', '2023-08-03', '2023-08-04', '2023-08-05'],
    'Positive_Sentiment': [120, 140, 110, 160, 180],
    'Neutral_Sentiment': [80, 90, 100, 85, 75],
    'Negative_Sentiment': [20, 30, 25, 35, 40]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])


df.set_index('Date', inplace=True)


plt.figure(figsize=(12, 8))


plt.subplot(2, 2, 1)
sns.lineplot(data=df['Positive_Sentiment'], marker='o', label='Positive Sentiment')
plt.title('Positive Sentiment Over Time')
plt.xlabel('Date')
plt.ylabel('Count')

plt.subplot(2, 2, 2)
sns.lineplot(data=df['Neutral_Sentiment'], marker='o', label='Neutral Sentiment')
plt.title('Neutral Sentiment Over Time')
plt.xlabel('Date')
plt.ylabel('Count')

plt.subplot(2, 2, 3)
sns.lineplot(data=df['Negative_Sentiment'], marker='o', label='Negative Sentiment')
plt.title('Negative Sentiment Over Time')
plt.xlabel('Date')
plt.ylabel('Count')

plt.subplot(2, 2, 4)
plt.stackplot(df.index, df['Positive_Sentiment'], df['Neutral_Sentiment'], df['Negative_Sentiment'], labels=['Positive', 'Neutral', 'Negative'], alpha=0.7)
plt.title('Stacked Sentiment Over Time')
plt.xlabel('Date')
plt.ylabel('Count')
plt.legend(loc='upper left')


plt.tight_layout()

plt.show()
