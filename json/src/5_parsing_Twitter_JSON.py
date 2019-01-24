import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import tweepy


def word_in_text(word, text):
    word = word.lower()
    text = tweet.lower()
    match = re.search(word, text)

    if match:
        return True
    return False

tweets_data = []

tweets_file = open('tweets.txt', 'r')

for line in tweets_file:
    tweet=json.loads(line)
    tweets_data.append(tweet)

tweets_file.close()

df = pd.DataFrame(tweets_data, columns=['text', 'lang'])

[clinton, trump, sanders, cruz] = [0, 0, 0, 0]

# counting the number of tweets in which each candidate is mentioned
for index, row in df.iterrows():
    clinton += word_in_text('clinton', row['text'])
    trump += word_in_text('trump', row['text'])
    sanders += word_in_text('sanders', row['text'])
    cruz += word_in_text('cruz', row['text'])

candidates = ['clinton', 'trump', 'sanders', 'cruz']
sns.set(color_codes=True)
_ = sns.barplot(candidates, [clinton, trump, sanders, cruz])
_.set(ylabel="count")
plt.show()
