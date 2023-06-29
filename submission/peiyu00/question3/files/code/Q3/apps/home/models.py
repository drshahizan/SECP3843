# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.db import models

class Tweet(models.Model):
    _id = models.CharField(max_length=255)
    text = models.TextField()
    in_reply_to_status_id = models.CharField(max_length=255, null=True)
    retweet_count = models.IntegerField(null=True)
    contributors = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField()
    geo = models.CharField(max_length=255, null=True)
    source = models.CharField(max_length=255)
    coordinates = models.CharField(max_length=255, null=True)
    in_reply_to_screen_name = models.CharField(max_length=255, null=True)
    truncated = models.BooleanField()
    entities = models.JSONField()
    retweeted = models.BooleanField()
    place = models.CharField(max_length=255, null=True)
    user = models.JSONField()
    favorited = models.BooleanField()
    in_reply_to_user_id = models.CharField(max_length=255, null=True)
    id = models.CharField(max_length=255, primary_key=True)

