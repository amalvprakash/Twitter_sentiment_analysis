import tweepy
import configparser
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
from collections import Counter
import re
import nltk
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords
# from nltk.stem.wordnet import WordNetLemmatizer
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')


config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

#print(api_key)

auth =tweepy.OAuthHandler(api_key,api_key_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

search_words = "{}-filter:retweets".format('rahul gandhi')

tweets = tweepy.Cursor(api.search_tweets, q=search_words, tweet_mode='extended').items(500)
tweets_list = []

# for tweet in tweets:
#     if(tweet.lang == 'en') and (not tweet.retweeted) and ('RT @' not in tweet.text):
#         print(tweet.text)
#         analysis = TextBlob(tweet.text, analyzer=NaiveBayesAnalyzer())
#         print(analysis.sentiment)
#         tweets.append(analysis.sentiment.classification)

for tweet in tweets:
        tweets_list.append(tweet.full_text)

counter = Counter()

nltk.download('vader_lexicon')

sid = SentimentIntensityAnalyzer()
l = []
for data in tweets_list:
    
    ss = sid.polarity_scores(data)
    l.append(ss)
    k = ss['compound']
    if k >= 0.05:
        counter['positive'] += 1
    elif k <= -0.05:
        counter['negative'] += 1
    else:
        counter['neutral'] += 1
        print('xxxxxxxxxxx',data)

positive = counter['positive']
negative = counter['negative']
neutral = counter['neutral']

colors = ['green', 'red', 'grey']
sizes = [positive, negative, neutral]
labels = 'Positive', 'Negative', 'Neutral'


print(positive)
print(negative)
print(neutral)

# use matplotlib to plot the chart
plt.pie(
    x=sizes,
    shadow=True,
    colors=colors,
    labels=labels,
    startangle=90,
    autopct='%.1f%%'
)

# plt.title("Sentiment of {} Tweets about {}".format(number, hash_tag))
plt.show()

# data = {'Tweet':tweets}
# data = pd.DataFrame(data)

# sns.set_style('darkgrid')
# print(data)
# g = sns.factorplot(x='Tweet', data=data, aspect=1.5, kind="count")
# #g = sns.catplot(data=data, x="Tweet", jitter=False)


# plt.show()


# inputFile = 'test.data'
# fd = open(inputFile, 'rb')
# dataset = pickle.load(fd)
# print(dataset)

# search tweets with some keywords
# results = api.search(hash_tag,
#                      count=number,
#                      since="2019-03-04",
# 					 until="2019-03-05",
#                      tweet_mode='extended',
#                      lang='en',
#                      place=places[0].id
#                      )

# print (results)

# tweets = results
# data = pd.DataFrame(data=[tweet.full_text for tweet in tweets], columns=['Tweets'])
# data.to_csv('output.csv')

# print the first 10 data
# print(data)

