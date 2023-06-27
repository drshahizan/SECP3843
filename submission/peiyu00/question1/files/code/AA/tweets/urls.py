from django.urls import path
from tweets.views import tweets_view

urlpatterns = [
    path('tweets/', tweets_view, name='tweets'),
]
