from django.urls import path
from tweets.views import tweets_view
from tweets.views import analyze_sentiment


urlpatterns = [
    path('tweets/', tweets_view, name='tweets'),
    path('analyze/', analyze_sentiment, name='analyze_sentiment'),
]
