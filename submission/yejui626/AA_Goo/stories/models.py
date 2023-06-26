from django.db import models


###MONGODB
class Container(models.Model):
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Container'
        app_label = 'stories'


class Topic(models.Model):
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Topic'
        app_label = 'stories'


class UserJSON(models.Model):
    name = models.CharField(max_length=255)
    registered = models.DateTimeField()
    fullname = models.CharField(max_length=255)
    icon = models.URLField()
    profileviews = models.IntegerField()

    class Meta:
        verbose_name = 'UserJSON'
        app_label = 'stories'


class ShortURL(models.Model):
    short_url = models.URLField()
    view_count = models.IntegerField()

    class Meta:
        verbose_name = 'ShortURL'
        app_label = 'stories'


class Story(models.Model):
    href = models.URLField()
    title = models.CharField(max_length=255)
    comments = models.IntegerField()
    container = models.ForeignKey(Container, on_delete=models.CASCADE)
    submit_date = models.DateTimeField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    promote_date = models.DateTimeField()
    idJSON = models.CharField(max_length=255)
    media = models.CharField(max_length=255)
    diggs = models.IntegerField()
    description = models.TextField()
    link = models.URLField()
    user = models.ForeignKey(UserJSON, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    shorturl = models.ManyToManyField(ShortURL)

    class Meta:
        verbose_name = 'Story'
        app_label = 'stories'
