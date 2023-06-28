from django.db import models

# Create your models here.


class room_details(models.Model):
_DATABASE = "mongodb"
         _id = models.CharField(max_length=255, unique=True)
         listing_url = models.URLField()
         name = models.CharField(max_length=255)
         summary  = models.TextField()
         interaction = models.TextField()
         house_rules = models.TextField()
         property_type = models.CharField(max_length=255)
         room_type = models.CharField(max_length=255)
         bed_type = models.CharField(max_length=255)
         minimum_nights = models.CharField(max_length=255)
         maximum_nights = models.CharField(max_length=255)
         cancellation_policy = models.TextField()
         last_scraped = models.DateField()
         calendar_last_scraped =m odels.DateField()
         first_review = models.DateField()
         last_review = models.DateField()
         accommodates 	= models.IntegerField()
         bedrooms 	= models.IntegerField()
         beds 	= models.IntegerField()
         number_of_reviews 	= models.IntegerField()
         bathrooms 	= models.IntegerField()
         amenities 	= models.TextField()
         price 	= models.DecimalField()
         security_deposit 	= models.DecimalField()
         cleaning_fee 	= models.DecimalField()
         extra_people 	= models.DecimalField()
         guests_included 	= models.DecimalField()
         images 	Object 	= models.URLField()
         host 	Object 	 = models.CharField(max_length=255)
         address 	 = models.CharField(max_length=255)
         availability 	 = models.CharField(max_length=255)
         review_scores 	 = models.CharField(max_length=255)
         reviews = models.CharField(max_length=255)   






