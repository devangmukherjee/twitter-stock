from textblob import TextBlob
import pandas as pd

df = pd.read_csv (r'/home/devang/twitter_project/stockerbot-export.csv', error_bad_lines=False)
print (df)


val = input("enter keyword: ")

polarity=0.00
no_of_tweets=0
for i in range(len(df)):
    if(df.symbols[i]==val):
        analysis = TextBlob(df.text[i])
        if(analysis.sentiment.subjectivity>=0.5):
            polarity+=analysis.sentiment.polarity
            no_of_tweets+=1

print("polarity of all tweets are:",polarity)
print("total no of tweets analyzed:", no_of_tweets)

