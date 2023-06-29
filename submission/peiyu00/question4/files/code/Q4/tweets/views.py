from django.shortcuts import render
from tweets.models import Tweet
from textblob import TextBlob

def tweets_view(request):
    target_source = "web"
    tweets_mysql = Tweet.objects.using('default').filter(source=target_source)

    tweets_mongodb = Tweet.objects.using('mongodb').filter(source=target_source)

    context = {
        'tweets_mysql': tweets_mysql,
        'tweets_mongodb': tweets_mongodb,
    }
    return render(request, 'tweets.html', context)

def analyze_sentiment(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity

        if sentiment > 0:
            sentiment_label = 'Positive'
        elif sentiment < 0:
            sentiment_label = 'Negative'
        else:
            sentiment_label = 'Neutral'

        return render(request, 'analyze.html', {'sentiment_label': sentiment_label})

    return render(request, 'analyze.html')
