#hi guys today in this tutorial i will show you how to detect sentiment from text lets start

#first lets import our library 

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


#lets creat function that detect postive and negative sentiment in text 

def sentiment_analyse(text):

    obj= SentimentIntensityAnalyzer()
    sentiment=obj.polarity_scores(text)

    print(sentiment)


#lets test our function 

txt="bad job boy"

sentiment_analyse(txt)

#like we see again our dunction detect a negative sentiment from our text so guys try this library by your self see you