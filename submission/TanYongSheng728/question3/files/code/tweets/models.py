from django.db import models
from django.contrib.auth.models import AbstractUser, Permission

# Create your models here.
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
    id = models.CharField(max_length=255, primary_key=True, unique=True)

class User(AbstractUser):
    USER_TYPES = (
        ('customer', 'Customer'),
        ('technical_worker', 'Technical Worker'),
        ('senior_management', 'Senior Management'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPES)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )