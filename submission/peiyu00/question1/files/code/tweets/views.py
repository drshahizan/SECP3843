from django.shortcuts import render
from tweets.models import Tweet

def tweets_view(request):
    target_source = "web"
    tweets_mysql = Tweet.objects.using('default').filter(source=target_source)

    tweets_mongodb = Tweet.objects.using('mongodb').filter(source=target_source)

    context = {
        'tweets_mysql': tweets_mysql,
        'tweets_mongodb': tweets_mongodb,
    }
    return render(request, 'tweets.html', context)
