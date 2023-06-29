from django.db import models

class Movies(models.Model):
    awards = models.JSONField()
    cast = models.JSONField()
    countries = models.JSONField()
    directors = models.JSONField()
    fullplot = models.TextField()
    genres = models.JSONField()
    imdb = models.JSONField()
    languages = models.JSONField()
    lastupdated = models.CharField(max_length=100)
    metacritic = models.IntegerField()
    num_mflix_comments = models.IntegerField()
    plot = models.TextField()
    poster = models.CharField(max_length=100)
    rated = models.CharField(max_length=100)
    released = models.DateTimeField()
    runtime = models.IntegerField()
    title = models.CharField(max_length=100)
    tomatoes = models.JSONField()
    type = models.CharField(max_length=100)
    writers = models.JSONField()
    year = models.IntegerField()

class Theaters(models.Model):
    location = models.CharField(max_length=100)
    theaterId = models.JSONField()

class Users(models.Model):
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Comments(models.Model):
    date = models.DateTimeField()
    email = models.CharField(max_length=100)
    movie_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    text = models.TextField()