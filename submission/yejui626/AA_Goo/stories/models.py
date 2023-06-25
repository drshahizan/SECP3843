from django.db import models


class Container(models.Model):
    _DATABASE = "mongodb"
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=255)


class Topic(models.Model):
    _DATABASE = "mongodb"
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=255)


class User(models.Model):
    _DATABASE = "mongodb"
    name = models.CharField(max_length=255)
    registered = models.DateTimeField()
    fullname = models.CharField(max_length=255)
    icon = models.URLField()
    profileviews = models.IntegerField()


class ShortURL(models.Model):
    _DATABASE = "mongodb"
    short_url = models.URLField()
    view_count = models.IntegerField()


class Story(models.Model):
    _DATABASE = "mongodb"
    _id = models.CharField(max_length=255, unique=True)
    href = models.URLField()
    title = models.CharField(max_length=255)
    comments = models.IntegerField()
    container = models.ForeignKey(Container, on_delete=models.CASCADE)
    submit_date = models.DateTimeField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    promote_date = models.DateTimeField()
    id = models.CharField(max_length=255)
    media = models.CharField(max_length=255)
    diggs = models.IntegerField()
    description = models.TextField()
    link = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    shorturl = models.ManyToManyField(ShortURL)
