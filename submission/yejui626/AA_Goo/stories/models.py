from django.db import models
from jsonfield import JSONField

class Story(models.Model):
    href = models.URLField()
    title = models.CharField(max_length=255)
    comments = models.IntegerField()
    container = JSONField()
    submit_date = models.DateTimeField()
    topic = JSONField()
    promote_date = models.DateTimeField()
    idJSON = models.CharField(max_length=255)
    media = models.CharField(max_length=255)
    diggs = models.IntegerField()
    description = models.TextField()
    link = models.URLField()
    user = JSONField()
    status = models.CharField(max_length=255)
    shorturl = JSONField()
    replica = models.IntegerField(blank=True, null=True)  # Add the replica field

    class Meta:
        verbose_name = 'Story'
        app_label = 'stories'