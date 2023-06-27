from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class ListingAndReviews(models.Model):
    _id = models.CharField(max_length=255, null=True)
    listing_url = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255, null=True)
    summary = models.TextField(null=True)
    interaction = models.TextField(null=True)
    house_rules = models.TextField(null=True)
    property_type = models.CharField(max_length=255, null=True)
    room_type = models.CharField(max_length=255, null=True)
    bed_type = models.CharField(max_length=255, null=True)
    minimum_nights = models.CharField(max_length=255, null=True)
    maximum_nights = models.CharField(max_length=255, null=True)
    cancellation_policy = models.CharField(max_length=255, null=True)
    last_scraped = models.DateField(null=True)
    calendar_last_scraped = models.DateField(null=True)
    first_review = models.DateField(null=True)
    last_review = models.DateField(null=True)
    accommodates = models.IntegerField(null=True)
    bedrooms = models.IntegerField(null=True)
    beds = models.IntegerField(null=True)
    number_of_reviews = models.IntegerField(null=True)
    bathrooms = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    amenities = models.JSONField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    security_deposit = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    cleaning_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    extra_people = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    guests_included = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    images = models.JSONField(null=True)
    host = models.JSONField(null=True)
    address = models.JSONField(null=True)
    availability = models.JSONField(null=True)
    review_scores = models.JSONField(null=True)
    reviews = models.JSONField(null=True)

    class Meta:
        db_table = 'airbnbbookingportal_listingandreviews'


class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_technical_worker = models.BooleanField(default=False)
    is_senior_management = models.BooleanField(default=False)

    groups = models.ManyToManyField(Group, blank=True, related_name='custom_user_set')

    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='custom_user_set')


